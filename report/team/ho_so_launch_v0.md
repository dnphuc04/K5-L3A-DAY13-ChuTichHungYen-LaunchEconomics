# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ChuTichHungYen · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool (274,7 đ); trong phạm vi pilot (`noi_dia` + `hang_nang`) cộng chi phí cố định 40 tr/tháng là 4.599 đ [simulated] (ở quy mô 45.000 yc/tháng, 0,38× nhân viên) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%) [simulated]; hoá đơn token biến thiên chỉ ±5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống: 5.865 đ/yêu cầu = 0,49× mức 12.000 đ [simulated] (đã tính 222 ca nhân viên làm thay); theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `quoc_te` 1,88×, `doi_tac` 0,85× [simulated] | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử 1.200 yc: Chỉ số chính (đóng 24h & không mở lại 7 ngày) đạt 82,83%; Chỉ số dùng (tỉ lệ sửa + bỏ) là 27,12%; Chỉ số an toàn (lỗi lọt mở lại 7 ngày) là 4,25% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi được phân vào đủ 5 loại Google PAIR (đồng thuận 90%); 5 ca đại diện có ngưỡng đo bằng event và người phụ trách; xử lý dứt điểm lỗi sổ cái (ca 7, 20) trước khi pilot | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên (20 đối chứng + 20 can thiệp, 40 cụm), ngẫu nhiên phân tầng depot; 3 bước rollout (10% → 25% → 50%); MDE 6 điểm (chấp nhận power 0,64 ở mức 5 điểm); 3 luật dừng chuẩn NẾU – TRONG – THÌ – KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Nếu số ca làm lại gấp đôi: chi phí tăng +51,8% lên 6.787 đ [simulated]; Nếu xem lại 100% kéo dài: chi phí lên 11.743 đ (0,98×) đến 12.414 đ (1,03×) [simulated], xóa bỏ hoàn toàn lợi ích kinh tế | Giả lập | Giám đốc tài chính |

**Đề xuất:** Go có điều kiện (chỉ triển khai pilot cho 2 loại yêu cầu `noi_dia` và `hang_nang`; loại hoàn toàn `quoc_te` do chi phí 1,88× và `doi_tac` do 0,85× sát ngưỡng).

**Các điều kiện tiên quyết:**
1. **Kỹ thuật & An toàn tiền mặt:** Kỹ sư trưởng agent hoàn thành khóa chống trùng idempotency key và cơ chế đối soát tự động dịch vụ sổ cái (khắc phục ca 7, ca 20) trước ngày 01/12/2026; pilot không được khởi động nếu chưa có xác nhận từ Kế toán trưởng.
2. **Thiết kế Pilot & Đánh đổi thống kê:** Giám đốc vận hành phê duyệt bằng văn bản chấp nhận mức chênh tối thiểu phát hiện được là 6 điểm phần trăm (MDE = 0,06; tương đương statistical power 0,64 nếu tác động thực chỉ ở mức 5 điểm) do giới hạn toàn công ty chỉ có 40 nhân viên (20 cụm/nhánh).
3. **Giám sát & Dữ liệu thực tế:** Kỹ sư hệ thống kích hoạt đủ 10 event có gắn `trace_id`; ngay sau tuần 1 (bước rollout 10%), Kế toán trưởng phải thay thế số phút giả lập (`_simulated`) bằng số liệu đo lường thực tế từ nhật ký nhân viên để tái đánh giá chi phí mỗi việc thành công.
4. **Vận hành & Kiểm soát chi phí:** Trưởng nhóm CSKH ban hành quy trình giảm tỷ lệ xem lại theo bậc (từ 100% xuống dưới 30% khi tỷ lệ sửa + bỏ ổn định dưới 15%), tránh để rủi ro xem lại 100% kéo dài khiến chi phí vượt 12.000 đ/yêu cầu.
