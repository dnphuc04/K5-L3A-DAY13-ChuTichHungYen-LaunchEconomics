# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 = 1/p, k triệt tiêu (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công 4.472 đ [simulated] gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ).
- Khoản lớn nhất là làm lại **51,8%** [simulated], tiếp theo xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% tổng chi phí [simulated].
- So với 12.000 đ phải cộng 222 ca nhân viên làm thay: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

- `quoc_te` không đáng để trợ lý xử lý: 22.515 đ = 1,88× [simulated], thành công 27,3%.
- Chạy lại không giúp: tỉ lệ ok của quoc_te theo lần thử là 30,0% → 11,4% → 2,2%; lỗi lặp lại trên cùng yêu cầu nên lần 2, 3 chỉ tốn thêm tiền.
- `doi_tac` sát ngưỡng (0,85× [simulated]) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi: 982 yêu cầu, 900 thành công, tổng 3.072.513 đ → 3.414 đ/việc thành công [simulated]. Cố định 40 triệu đ/tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Ở 45.000 yêu cầu/tháng, cố định chỉ thêm 1.185 đ/việc, không đổi kết luận (0,38× [simulated]); khối lượng giảm một nửa thì cố định tăng gấp đôi lên 2.370 đ/việc (0,48× [simulated]), nên hồ sơ phải ghi rõ khối lượng.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [simulated], đúng bằng tổng hai tác động riêng (5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%) [simulated]. Giá token chỉ ±5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ (thấp nhất) [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | **6.901.220 đ (rẻ nhất)** [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]), không trùng giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ); tối ưu riêng chỉ số đó đẩy thêm 85 việc sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Phạm vi `noi_dia` + `hang_nang`: 948 yêu cầu có lần chạy ok × 5 phút = 9.480.000 đ, 48 ca làm lại × 9 phút = 864.000 đ, token + tool 224.513 đ → 10.568.513 đ / 900 = **11.743 đ = 0,98×** của 12.000 đ [simulated].
- Nếu dùng phút làm lại trung bình trong dữ liệu (15,3 phút/ca, trung vị 14,5): 12.415 đ = **1,03×** [simulated], tức đắt hơn nhân viên tự làm. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút) [simulated].
- Pilot cần học được tỉ lệ xem lại có thể giảm an toàn tới đâu và thời gian mỗi lần xem lại có dưới 5 phút không, vì xem lại chiếm khoảng 90% chi phí khi xem lại 100%.

## Kiểm tra tay (người kiểm số)

Người kiểm số: Nguyễn Việt Hưng. Số đầu vào đếm trực tiếp trên `src/logix_requests.csv` / `src/logix_runs.csv` (bộ lọc Excel hoặc đếm tay), không lấy từ output code. Ngưỡng chấp nhận: lệch ≤ 2%. Lệch (%) = (tay − code) / code × 100.

### Số đầu vào tự đếm

| Đại lượng | Cách đếm | Kết quả tự đếm | Code |
| --- | --- | ---: | ---: |
| Tổng phút xem lại | tổng cột `phut_xem_lai_simulated` | 890 | 890 |
| Tổng phút làm lại | tổng cột `phut_lam_lai_simulated` | 1132 | 1.132 |
| Tổng lần gọi tool | tổng cột `tool_calls` | 5600 | 5.600 |
| Số việc thành công | đếm `ket_qua` = `thanh_cong` | 978 | 978 |
| Số yêu cầu không thành công | 1.200 − số việc thành công | 222 | 222 |
| Tổng token đầu vào / đầu ra (1.624 lần chạy) | tổng cột `tokens_in`, `tokens_out` | 5.771.712 / 734.774 | |
| Tiền token | 5.771,712 × 26 + 734,774 × 130 | 245.585 đ | 245.585 đ |
| Phạm vi noi_dia + hang_nang | lọc `loai` | 982 yêu cầu, 900 thành công, token + tool 224.513 đ, 644 phút xem lại, 780 phút làm lại [simulated] | 982 · 900 |
| Phạm vi: yêu cầu có ≥ 1 lần chạy `ok` / ca `lam_lai` | lọc `status` = ok theo `request_id`; đếm `ket_qua` = `lam_lai` | 948 / 48 | 948 / 48 |
| Giới hạn 2 lần: việc thành công, tổng chi phí trợ lý | bỏ `attempt` > 2; yêu cầu `so_lan_chay` > 2 coi là chuyển nhân viên | 966; 291.220 + (855 + 1.046) × 2.000 = 4.093.220 đ [simulated] | 4.093.220 đ |

### Đối chiếu

| # | Số kiểm | Cách tính tay | Kết quả tay | Code | Lệch | Kết luận |
| --: | --- | --- | ---: | ---: | ---: | --- |
| 1 | A2 · Chi phí mỗi việc thành công [simulated] | (245.585 + 84.000 + 890 × 2.000 + 1.132 × 2.000) ÷ 978 = 4.373.585 ÷ 978 | 4.472 đ | 4.472 đ | 0,0% | Khớp |
| 2 | A2 · Gấp bao nhiêu lần hoá đơn/yêu cầu | (245.585 + 84.000) ÷ 1.200 = 274,65 đ ; 4.472 ÷ 274,65 | 16,3× | 16,3× | 0,0% | Khớp |
| 3 | A2 · So với nhân viên tự làm [simulated] | (4.373.585 + 222 × 12.000) ÷ 1.200 = 7.037.585 ÷ 1.200 ; 5.865 ÷ 12.000 | 5.865 đ = 0,49× | 5.865 đ = 0,49× | 0,0% | Khớp |
| 4 | A4 · Cố định mỗi việc, 45.000 yc/tháng | 45.000 × 900 ÷ 1.200 = 33.750 việc ; 40.000.000 ÷ 33.750 | 1.185 đ | 1.185 đ | 0,0% | Khớp |
| 5 | A4 · Chi phí + cố định [simulated] | (224.513 + 644 × 2.000 + 780 × 2.000) ÷ 900 = 3.072.513 ÷ 900 = 3.414 ; + 1.185 ; ÷ 12.000 | 4.599 đ = 0,38× | 4.599 đ = 0,38× | 0,0% | Khớp |
| 6 | B1 · Tự kiểm tra tuyến tính | phần của từng khoản trong tổng 4.373.585: token 245.585 → 5,6% (nửa 2,8%); xem lại 1.780.000 → 40,7% (nửa 20,3%); làm lại 2.264.000 → 51,8% (nửa 25,9%) | 5,6→2,8 · 40,7→20,3 · 51,8→25,9 | 5,6→2,8 · 40,7→20,3 · 51,8→25,9 | 0,0% | Khớp |
| 7 | B2 · Cặp token × 2 + xem lại × 2 [simulated] | (4.373.585 + 245.585 + 1.780.000) ÷ 978 = 6.399.170 ÷ 978 ; 5,6% + 40,7% | 6.543 đ (+46,3%) | 6.543 đ (+46,3%) | 0,0% | Khớp |
| 8 | B3 · Cả hệ thống, giới hạn 2 lần [simulated] | 4.093.220 + (1.200 − 966) × 12.000 = 4.093.220 + 234 × 12.000 | 6.901.220 đ | 6.901.220 đ | 0,0% | Khớp |
| 9 | B4 · Xem lại 100% [simulated] | (948 × 5 × 2.000 + 48 × 9 × 2.000 + 224.513) ÷ 900 = 10.568.513 ÷ 900 ; ÷ 12.000 | 11.743 đ = 0,98× | 11.743 đ = 0,98× | 0,0% | Khớp |

### Ghi chú khi lệch

- Không có dòng nào lệch quá 2%: cả 9 số tính tay khớp output của `src/lab13.py`, số đầu vào đếm trực tiếp từ hai file CSV.
