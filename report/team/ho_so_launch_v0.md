# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: ChuTichHungYen · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool (274,7 đ); trong phạm vi pilot (`noi_dia` + `hang_nang`) cộng chi phí cố định 40 tr/tháng là 4.599 đ [simulated] (ở quy mô 45.000 yc/tháng, 0,38× nhân viên) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%) [simulated]; hoá đơn token biến thiên chỉ ±5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống: 5.865 đ/yêu cầu = 0,49× mức 12.000 đ [simulated] (đã tính 222 ca nhân viên làm thay); theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `quoc_te` 1,88×, `doi_tac` 0,85× [simulated] | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử 1.200 yc: Chỉ số chính (đóng 24h & không mở lại 7 ngày) đạt 82,83%; Chỉ số dùng (tỉ lệ sửa + bỏ) là 27,12%; Chỉ số an toàn (lỗi lọt mở lại 7 ngày) là 4,25% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi được phân vào đủ 5 loại Google PAIR (đồng thuận 90%); 5 ca đại diện có ngưỡng đo bằng event và người phụ trách; xử lý dứt điểm lỗi sổ cái (ca 7, 20) trước khi pilot | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 20 nhân viên mỗi nhánh, phân tầng theo depot, mục tiêu 5.980 yêu cầu mỗi nhánh (859 hiệu dụng, trung bình 299 mỗi nhân viên). MDE 6 điểm phần trăm, power khoảng 0,64 nếu tác động thực là 5 điểm. Xem [kế hoạch pilot](pilot_plan.yaml). | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Gấp đôi số ca làm lại làm chi phí tăng 51,8% lên 6.787 đ [simulated]. Xem lại 100% kéo dài đưa chi phí lên 11.743–12.415 đ/việc thành công [simulated], tương đương 0,98–1,03× mức thủ công. | Giả lập | Giám đốc tài chính |

**Điều kiện Gate 2a**

1. Đến 01/12/2026, Kỹ sư trưởng agent trình bằng chứng chống hoàn trùng và đối soát sổ cái (ca 7, 20) để Kế toán trưởng xác nhận trước khi chạy.
2. Trước ngày bắt đầu pilot, Giám đốc vận hành duyệt bằng văn bản MDE 6 điểm phần trăm và kiểm tra khả năng thu đủ mẫu trước mốc quyết định 05/01/2027.
3. Trước ngày bắt đầu, Kỹ sư hệ thống kiểm tra đủ 10 event có `trace_id`. Cuối tuần 1, Kế toán trưởng tính lại chi phí theo số phút đo thực tế.
4. Trước ngày bắt đầu, Trưởng nhóm CSKH ban hành quy trình giảm tỷ lệ xem lại theo bậc. Kiểm tra trước mỗi lần tăng bậc, với mục tiêu tỷ lệ xem lại dưới 30% khi tỷ lệ sửa hoặc bỏ ổn định dưới 15%.

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` và `hang_nang`. Chi phí tương đối của `quoc_te` là 1,88× và `doi_tac` là 0,85× mức thủ công [simulated], nên giữ hai loại này ngoài pilot.
