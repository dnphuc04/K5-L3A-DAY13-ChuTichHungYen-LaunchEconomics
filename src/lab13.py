"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

CO_DINH_THANG = 40_000_000      # chi phí cố định của trợ lý, đồng / tháng
YEU_CAU_THANG = 45_000          # khoảng 1.500 yêu cầu / ngày
PHAM_VI = ['noi_dia', 'hang_nang']  # phạm vi pilot đề xuất (A3)
SIM = '[simulated]'             # nhãn cho mọi số tính từ cột *_simulated


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: E = sum_{i=1..k} (1-p)^(i-1) = (1-(1-p)^k)/p
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = E[số lần chạy] / P(thành công) = 1/p với mọi k (k triệt tiêu)
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ lần chạy thuộc các yêu cầu đang xét (để gọi lại cho từng loại ở A3)
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên,
        # không còn phút xem lại / làm lại của trợ lý.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    tien_chay = tien_token + tien_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated

    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai   # tử số: MỌI lần chạy
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())        # mẫu số: chỉ việc thành công
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=tien_chay[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=tien_chay.sum() / len(reqs),
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ (z chính xác)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb))
         + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc):
    """c cụm, m yêu cầu mỗi cụm → cỡ mẫu hiệu dụng (luôn < c / icc)."""
    return c * m / he_so_thiet_ke(m, icc)


def m_toi_thieu(c, n_can, icc):
    """m nhỏ nhất để c*m/(1+(m-1)icc) >= n_can; vô nghiệm nếu n_can >= c/icc."""
    if n_can >= c / icc:
        return None
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def in_dong(ten, gia_tri, nhan=''):
    print(f'  {ten:40s} {gia_tri:>14,.1f} {nhan}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ===== A1 =====
    print('=== A1 · Ba phép thử (p = 0,8) ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'  tối đa 2 lần: {so_lan_chay_ky_vong(0.8, 2):.2f} · đến khi đúng: {so_lan_chay_ky_vong(0.8):.2f}'
          f' · hệ số chi phí k=3: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    # ===== A2 =====
    print('\n=== A2 · Mô hình chi phí từ trace (toàn bộ 1.200 yêu cầu) ===')
    goc = mo_hinh(runs, reqs)
    nhan = dict(token='đo từ trace', tool='đo từ trace', chay_lai='đo từ trace (attempt > 1)',
                xem_lai=SIM, lam_lai=SIM, tong='có phần ' + SIM, thanh_cong='',
                cps=SIM, hoa_don_moi_yc='đo từ trace')
    for ten, gia_tri in goc.items():
        in_dong(ten, gia_tri, nhan[ten])
    print(f'  Số lần gọi tool: {runs.tool_calls.sum():,} · phút xem lại: {reqs.phut_xem_lai_simulated.sum():,}'
          f' · phút làm lại: {reqs.phut_lam_lai_simulated.sum():,} {SIM}')
    print(f'  cps gấp {goc["cps"] / goc["hoa_don_moi_yc"]:.1f} lần hoá đơn token+tool / yêu cầu')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  Tỉ trọng {k:8s}: {goc[k] / goc["tong"] * 100:5.1f}%' + (f' {SIM}' if k in ('xem_lai', 'lam_lai') else ''))
    print(f'  Giờ nhân viên chiếm {(goc["xem_lai"] + goc["lam_lai"]) / goc["tong"] * 100:.1f}% tổng chi phí {SIM}')
    khong_tc = len(reqs) - goc['thanh_cong']
    he_thong = (goc['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'  Chi phí cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ):'
          f' {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× {SIM}')

    # ===== A3 =====
    print(f'\n=== A3 · Theo loại yêu cầu {SIM} ===')
    print(f'  {"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"so_12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        m = mo_hinh(runs, r)
        print(f'  {loai:10s} {len(r):6d} {m["thanh_cong"] / len(r) * 100:8.1f}% '
              f'{r.so_lan_chay.mean():7.2f} {m["cps"]:9,.0f} {m["cps"] / BASELINE:6.2f}×')
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: (d.status == 'ok').astype(float))
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('  Tỉ lệ status = ok theo lần thử (chạy lại có giúp không?):')
    print('    ' + (ok_theo_lan * 100).round(1).to_string().replace('\n', '\n    '))

    # ===== A4 =====
    print(f'\n=== A4 · Chi phí cố định, phạm vi {" + ".join(PHAM_VI)} {SIM} ===')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    m_pv = mo_hinh(runs, pv)
    print(f'  Phạm vi: {len(pv)} yêu cầu, {m_pv["thanh_cong"]} thành công, tổng {m_pv["tong"]:,.0f} đ,'
          f' cps {m_pv["cps"]:,.0f} đ')
    for ten, he_so_kl in [('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YEU_CAU_THANG * he_so_kl * m_pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = m_pv['cps'] + co_dinh
        print(f'  {ten:22s} việc TC/tháng {tc_thang:9,.0f} · cố định/việc {co_dinh:7,.0f} đ'
              f' · cps + cố định {tong_viec:7,.0f} đ = {tong_viec / BASELINE:.2f}×')

    # ===== B1 =====
    print(f'\n=== B1 · Độ nhạy, đổi từng yếu tố {SIM} ===')
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    cps_goc = goc['cps']
    print(f'  {"Gốc (A2)":30s} {cps_goc:8,.0f}')
    tac_dong = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        tac_dong[ten] = cps / cps_goc - 1
        print(f'  {ten:30s} {cps:8,.0f} {tac_dong[ten] * 100:+6.1f}%')

    # ===== B2 =====
    print(f'\n=== B2 · Đổi một cặp {SIM} ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = tac_dong['Giá token gấp đôi'] + tac_dong['Tỉ lệ xem lại gấp đôi']
    print(f'  Giá token ×2 + xem lại ×2: {cap:,.0f} đ ({(cap / cps_goc - 1) * 100:+.1f}%);'
          f' tổng hai tác động riêng {tong_rieng * 100:+.1f}%')
    # Xếp hạng theo YẾU TỐ: lấy |thay đổi| lớn nhất trong các kịch bản của cùng một yếu tố
    yeu_to = {'Số ca làm lại': ['Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa'],
              'Tỉ lệ xem lại': ['Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'],
              'Lương nhân viên': ['Lương nhân viên tăng 25%'],
              'Giới hạn số lần chạy': ['Chỉ cho chạy tối đa 2 lần', 'Chỉ cho chạy 1 lần'],
              'Giá token': ['Giá token gấp đôi', 'Giá token giảm một nửa']}
    muc = {yt: max(abs(tac_dong[t]) for t in ds) for yt, ds in yeu_to.items()}
    xep_hang = sorted(muc.items(), key=lambda kv: -kv[1])
    print('  Xếp hạng yếu tố:', ' · '.join(f'{i}. {yt} ({v * 100:.1f}%)' for i, (yt, v) in enumerate(xep_hang, 1)))

    # ===== B3 =====
    print(f'\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống {SIM} ===')
    for k in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong = len(reqs) - m['thanh_cong']
        print(f'  {k} lần: tổng trợ lý {m["tong"]:>11,.0f} · không TC {khong:4d}'
              f' · cả hệ thống {m["tong"] + khong * BASELINE:>11,.0f} · cps {m["cps"]:,.0f}')

    # ===== B4 =====
    print(f'\n=== B4 · Xem lại 100% cho {" + ".join(PHAM_VI)} {SIM} ===')
    runs_pv = runs[runs.request_id.isin(pv.request_id)]
    co_ok = runs_pv.loc[runs_pv.status == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    tien_chay_pv = m_pv['token'] + m_pv['tool']
    phut_lam_lai_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'  Yêu cầu có ≥1 lần ok: {co_ok} · ca lam_lai: {so_lam_lai} · token+tool: {tien_chay_pv:,.0f} đ')
    print(f'  phut_lam_lai_simulated trên mọi ca lam_lai: TB {phut_lam_lai_tb.mean():.1f} · trung vị {phut_lam_lai_tb.median():.1f}')
    for phut_ll in [9, round(phut_lam_lai_tb.mean(), 1)]:
        tien_xl = co_ok * 5 * LUONG_PHUT
        tien_ll = so_lam_lai * phut_ll * LUONG_PHUT
        tong = tien_chay_pv + tien_xl + tien_ll
        cps = tong / m_pv['thanh_cong']
        hoa_von = (BASELINE * m_pv['thanh_cong'] - tien_chay_pv - tien_ll) / (co_ok * LUONG_PHUT)
        print(f'  làm lại {phut_ll:>4} phút/ca: tổng {tong:,.0f} đ · cps {cps:,.0f} đ = {cps / BASELINE:.2f}×'
              f' · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút/yêu cầu')

    # ===== D1 =====
    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    ICC = 0.02
    n5 = co_mau(0.70, 0.75)
    print(f'  a) Theo yêu cầu: {n5:,} yêu cầu mỗi nhóm')
    de75 = he_so_thiet_ke(75, ICC)
    n_b = math.ceil(n5 * de75)
    print(f'  b) Theo nhân viên, m = 75: DE = {de75:.2f}; n = {n_b:,} mỗi nhóm → {math.ceil(n_b / 75)} người/nhóm,'
          f' tổng {2 * math.ceil(n_b / 75)} > 40: không đủ người')
    print(f'  c) 20 nhân viên/nhóm: tối đa c/ICC = {20 / ICC:,.0f} < {n5:,}: không đạt')
    print(f'  d) 6 depot/nhóm: tối đa c/ICC = {6 / ICC:,.0f}')
    n6 = co_mau(0.70, 0.76)
    m6 = m_toi_thieu(20, n6, ICC)
    print(f'  e) Mức chênh 6 điểm: {n6} mỗi nhóm; 20 người/nhóm cần m ≥ {m6} yêu cầu/người'
          f' (DE {he_so_thiet_ke(m6, ICC):.2f}, n hiệu dụng {co_mau_hieu_dung(20, m6, ICC):.0f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        pw = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05)
        print(f'  Nếu tác động thật chỉ 5 điểm mà n = {n6}/nhóm: power ≈ {pw:.2f}')
    except ImportError:
        print('  (cài statsmodels để tính power ở mức 5 điểm)')

    # ===== D3 · tỉ lệ an toàn hiện tại =====
    print('\n=== D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại ===')
    print(f'  Toàn bộ: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})'
          f' · phạm vi {"+".join(PHAM_VI)}: {pv.mo_lai_trong_7_ngay.mean() * 100:.2f}%')

    # ===== E1 · Tính thử ba chỉ số =====
    print('\n=== E1 · Ba chỉ số trong đợt chạy thử (1.200 yêu cầu) ===')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    print(f'  Chính (đóng 24h, không mở lại 7 ngày): {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'  Dùng (bỏ qua gợi ý = sua+bo / được xem lại): {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f'  An toàn (mở lại trong 7 ngày): {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}%'
          f' ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})')
    ll_pv = (pv.ket_qua == 'lam_lai').mean()
    print(f'  Tỉ lệ làm lại trong phạm vi: {ll_pv * 100:.1f}% (dùng cho dấu hiệu rủi ro E2)')
