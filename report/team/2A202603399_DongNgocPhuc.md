# Báo cáo cá nhân — Đồng Ngọc Phúc

## 1. Thông tin thành viên

- Họ tên: Đồng Ngọc Phúc
- MSSV: 2A202603399
- Email: dnphuc04@gmail.com
- Nhóm: ChuTichHungYen, lớp L3A
- Vai trò: Trưởng nhóm, giữ hồ sơ Launch v0 và kiểm tra từng giai đoạn.

## 2. Phần việc phụ trách

Phân công thành viên theo checkpoint, theo dõi đầu ra A–E, tổng hợp hồ sơ Launch v0 và chuẩn bị phương án pilot để nhóm xem xét tại Gate 2a.

## 3. Đóng góp cụ thể

- Ghi phân công trong `TEAM.md`, gồm người viết code, người kiểm số và hai người gắn nhãn.
- Chuẩn bị bản nháp hồ sơ Launch v0 với hỗ trợ của Codex. Bản nháp tổng hợp chi phí A–B, ba chỉ số từ đợt chạy thử và hai rủi ro kinh tế. Chi phí mỗi việc thành công là 4.472 đ [simulated] theo bảng A2.
- Chuẩn bị bản nháp pilot phân ngẫu nhiên theo yêu cầu với 1.251 yêu cầu mỗi nhánh, dựa trên kết quả D1 của nhóm. Bản nháp ghi các điều kiện dừng về an toàn, chi phí và mức sử dụng. Đây là phương án từng được đưa ra để rà soát. Bản nhóm trên GitHub dùng phương án phân ngẫu nhiên theo nhân viên, 20 cụm mỗi nhánh, MDE 6 điểm phần trăm. Nếu tác động thực là 5 điểm, lực kiểm định theo hồ sơ nhóm khoảng 0,64.
- Kiểm tra tiến độ trên GitHub. Bảng lỗi do Dương và Hảo thực hiện ghi hai bộ nhãn trùng 18/20 ca (90%), đạt ngưỡng 80%.
- Rà soát bản nhóm tại commit `df21f62`. Làm rõ cỡ mẫu hiệu dụng 859 mỗi nhánh tương ứng mục tiêu thu 5.980 yêu cầu mỗi nhánh với 20 nhân viên và trung bình 299 yêu cầu mỗi người. Cập nhật thời điểm kiểm tra các điều kiện Gate 2a và cách xử lý nếu thiếu mẫu vào ngày quyết định.

## 4. Bằng chứng

- Commit [cf9ab4a — assigned tasks](https://github.com/dnphuc04/K5-L3A-DAY13-ChuTichHungYen-LaunchEconomics/commit/cf9ab4a) ghi phân công nhóm.
- [Hồ sơ Launch v0](ho_so_launch_v0.md) và [kế hoạch pilot](pilot_plan.yaml) là các đầu ra đã chuẩn bị bản nháp. Bản nháp và bản nhóm khác nhau về đơn vị phân nhóm. Tôi đối chiếu với [hồ sơ Launch v0 của nhóm trên GitHub](https://github.com/dnphuc04/K5-L3A-DAY13-ChuTichHungYen-LaunchEconomics/blob/07a1523f25c4e8bba0324ebd771f7fa3c4a098a0/report/team/ho_so_launch_v0.md).
- [Bảng chi phí](bang_chi_phi.md) và [bảng lỗi](bang_loi.md) là nguồn đối chiếu kết quả A–C của các thành viên.

## 5. Công cụ AI đã dùng

Dùng Codex để hệ thống hóa checkpoint, soạn bản nháp và đối chiếu hồ sơ. Codex chạy `lab13.py`, xác nhận ba phép thử A1 đạt và đối chiếu các tỷ lệ E1 với CSV (994/1.200, 48/177 và 51/1.200). Kế hoạch pilot đọc được bằng `yaml.safe_load`, không còn dấu hỏi và có ba luật dừng đủ bốn vế.

## 6. Tự đánh giá

Đã ghi rõ phân công và chuẩn bị được bản nháp có số liệu để nhóm thảo luận. Bản nhóm đề xuất Go có điều kiện, giới hạn ở nội địa và hàng nặng, yêu cầu xử lý lỗi hoàn trùng và đối soát sổ cái trước khi chạy pilot. Đánh đổi cần giải thích khi bảo vệ là chọn chia theo nhân viên để giảm giao thoa, đồng thời chấp nhận khả năng phát hiện thấp hơn nếu tác động chỉ đạt 5 điểm. Kết quả duyệt chéo sẽ được ghi khi có bằng chứng từ buổi chấm.
