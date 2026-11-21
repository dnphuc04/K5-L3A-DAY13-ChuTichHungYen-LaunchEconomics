# Báo cáo cá nhân — NguyenHuyHoang-MSSV


## 1. Thông tin thành viên

- Họ tên: Nguyễn Huy Hoàng
- MSSV: 2A202603366
- Email: nguyenhuyhoangtuho@gmail.com
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

- Viết và chạy `src/lab13.py` cho các nhiệm vụ A (A1–A4), B (B1–B4), D1 (cỡ mẫu) và tính thử ba chỉ số E1, tỉ lệ mở lại 7 ngày cho D3.
- Cùng người kiểm số điền `report/team/bang_chi_phi.md` từ output của code.

## 3. Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: `mo_hinh(...)` cộng token + tool trên **mọi** lần chạy (kể cả lỗi), xem lại + làm lại từ cột `_simulated`, chia cho số việc `thanh_cong` (978) → 4.472 đ [simulated], gấp 16,3 lần hoá đơn/yêu cầu (274,7 đ).
- A3, A4: tách theo `loai` (quoc_te 1,88× [simulated], tỉ lệ ok theo lần thử 30,0% → 11,4% → 2,2%); cộng chi phí cố định cho phạm vi noi_dia + hang_nang → 4.599 đ = 0,38× [simulated].
- B1–B4: 9 kịch bản độ nhạy, cặp B2 (+46,3%), xếp hạng yếu tố tự động, chi phí cả hệ thống theo giới hạn chạy (2 lần rẻ nhất, 6.901.220 đ [simulated]), xem lại 100% → 11.743 đ = 0,98× (1,03× với 15,3 phút làm lại) [simulated] và mức hoà vốn 5,1 / 4,8 phút.
- D1: `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu` → 1.251 · 3.103 (42 người/nhóm) · 1.000 · 300 · m ≥ 299; power ≈ 0,64 ở mức 5 điểm với n = 859 (statsmodels).
- E1/D3: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200), trong phạm vi 3,97%.

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`.
- Lệnh: `cd src && python lab13.py` in đủ các khối A1, A2, A3, A4, B1–B4, D1, D3, E1.
- Mọi số A2, A3, B1, B3, B4, D1, E1 khớp số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch < 0,1%, trong ngưỡng 2%).
- Commit: (điền hash sau khi commit).

## 5. Công cụ AI đã dùng

- Claude Code: hỗ trợ viết code `lab13.py` theo công thức trong `docs/du_lieu_va_cong_thuc.md` và điền bảng chi phí từ output.
- Cách tự kiểm tra: chạy ba phép thử A1; so từng số với bảng đối chiếu trong hướng dẫn; kiểm tra quy tắc "giảm một nửa = nửa mức tăng của gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9); kiểm tra B2 bằng tổng hai tác động riêng; giải tay câu D1e (2,82m ≥ 841,82 → m ≥ 299).
- Không dùng AI để bịa số: mọi con số trong bảng do `src/lab13.py` in ra.

## 6. Tự đánh giá

- Giải thích được: tử số tính mọi lần chạy vì lần lỗi vẫn tốn token/tool; mẫu số chỉ đếm việc thành công vì đó là thứ công ty thực sự nhận được.
- Giải thích được cỡ mẫu hiệu dụng khi chia theo cụm luôn < c / ICC, nên 20 nhân viên mỗi nhóm tối đa chỉ được 1.000 < 1.251.
- Cần cải thiện: thay phút simulated bằng phút đo thật khi có dữ liệu pilot.
