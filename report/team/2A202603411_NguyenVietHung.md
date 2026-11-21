# Báo cáo cá nhân — NguyenVietHung-2A202603411

## 1. Thông tin thành viên

- Họ tên: Nguyễn Việt Hưng
- MSSV: 2A202603411
- Email: robinnguyen2004@gmail.com
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- Tính tay để đối chiếu các con số chính do `src/lab13.py` in ra ở nhiệm vụ A, B và D1. Số đầu vào đếm trực tiếp từ `src/logix_runs.csv` và `src/logix_requests.csv`, không lấy từ output code.
- Cùng người viết code điền và soát `report/team/bang_chi_phi.md`; điền phần chú thích D1 trong `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Dựng mục "Kiểm tra tay (người kiểm số)" trong `report/team/bang_chi_phi.md`, gồm bảng số đầu vào tự đếm và bảng đối chiếu 9 dòng.
- Số đầu vào tự đếm: 890 phút xem lại và 1.132 phút làm lại [simulated], 5.600 lần gọi tool, 978 việc thành công, 222 ca không thành công. Thêm 5.771.712 / 734.774 token cho ra tiền token 245.585 đ; phạm vi noi_dia + hang_nang có 982 yêu cầu, 900 thành công, 948 yêu cầu có lần chạy ok, 48 ca làm lại.
- Đối chiếu 9 con số, cả 9 khớp code (lệch 0%, ngưỡng 2%):
  - A2: 4.373.585 ÷ 978 = 4.472 đ [simulated]; gấp 16,3× hoá đơn/yêu cầu (274,65 đ); so với nhân viên tự làm 5.865 đ = 0,49× [simulated].
  - A4: 40.000.000 ÷ 33.750 = 1.185 đ cố định/việc; 3.414 + 1.185 = 4.599 đ = 0,38× [simulated].
  - B1: kiểm tra tuyến tính 5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9. B2: 6.543 đ (+46,3%) [simulated].
  - B3: 4.093.220 + 234 × 12.000 = 6.901.220 đ [simulated]. B4: 10.568.513 ÷ 900 = 11.743 đ = 0,98× [simulated].
- D1 giải tay trong chú thích `pilot_plan.yaml`: 1.251 · DE 2,48 → 3.103 (42 người mỗi nhóm, tổng 84 > 40) · tối đa 1.000 · tối đa 300 · m ≥ 299 (DE 6,96; kiểm lại 20 × 299 ÷ 6,96 = 859,2 ≥ 859).

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`, mục "Kiểm tra tay (người kiểm số)".
- `report/team/pilot_plan.yaml`, phần chú thích D1 (a–e).
- Commit: (điền hash sau khi commit).

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề để xác định phần việc của người kiểm số, dựng khung bảng đối chiếu, giải thích từng công thức (tử số tính mọi lần chạy, mẫu số chỉ đếm việc thành công; hệ số thiết kế và trần c ÷ ICC khi chia theo cụm).
- AI đã đếm một phần số đầu vào bằng script riêng đọc thẳng hai file CSV (không gọi `lab13.py`) và điền các phép tính vào bảng đối chiếu.
- Tự kiểm tra: tự đếm các số đầu vào cơ bản (tổng phút xem lại, phút làm lại, lần gọi tool, việc thành công) và so khớp với kết quả của AI; bấm máy lại dòng A2 (4.472 đ) và câu D1-e (m ≥ 299); so mọi số với bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.

## 6. Tự đánh giá

- Hoàn thành vai người kiểm số: 9 con số A, B và 5 câu D1 đều có cách tính ghi rõ và khớp code trong ngưỡng 2%.
- Hiểu và giải thích được vì sao chi phí mỗi việc thành công gấp 16,3× hoá đơn token (giờ nhân viên chiếm 92,5% tổng chi phí [simulated]) và vì sao số cụm, không phải tổng số yêu cầu, quyết định cỡ mẫu.
