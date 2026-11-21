# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Lê Thái Dương · Người gắn nhãn 2: Vũ Văn Hảo (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Hệ thống | Do người dùng | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90% (đạt yêu cầu ≥ 80%)

## Quy tắc phân biệt cho các ca không trùng

- **Ca 6:** Thống nhất là **Do người dùng** vì nguyên nhân gốc là khách hàng chọn sai danh mục hoàn tiền; việc giao diện trợ lý chưa có bộ lọc gợi ý ngăn ngừa là giải pháp cải tiến (thuộc cột khắc phục), không phải nguyên nhân phát sinh lỗi.
- **Ca 8:** Thống nhất là **Hệ thống** vì lỗi trích dẫn điều khoản cũ đã hiển thị rõ ràng trên màn hình giao diện (lỗi đã lộ ra và nhân viên bắt được); nhãn **Ngầm** chỉ áp dụng khi cả khách hàng lẫn hệ thống đều hoàn toàn không phát hiện ra sai sót cho đến khi kiểm toán mẫu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ vượt quá 2% số yêu cầu/ngày | Tự động nhận diện định dạng mã sàn TMĐT và đối chiếu sang mã vận đơn LogiX; nếu không khớp thì hiển thị hướng dẫn kèm hình ảnh minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: event tin nhắn báo "đã hoàn" nhưng không tìm thấy bản ghi sổ cái ghi nhận thành công cùng `trace_id`; ngưỡng cảnh báo: 0 ca | Chỉ gửi thông báo "đã hoàn" khi dịch vụ sổ cái trả về mã thành công; nếu gặp lỗi timeout/503 quá 3 lần thì chuyển trạng thái "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Đo lường tỷ lệ yêu cầu mở lại vì thắc mắc số tiền nhưng kết quả kiểm tra lại xác nhận tính đúng theo chính sách; theo dõi theo tuần, ngưỡng > 2% | Cập nhật mẫu tin nhắn phản hồi luôn hiển thị công thức tính minh bạch: "Số tiền hoàn = 30.000 đ × 50% = 15.000 đ" kèm lý do chi tiết | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `thieu_du_lieu_doi_tac`, theo dõi theo từng loại yêu cầu; ngưỡng cảnh báo > 15% | Duy trì luồng bàn giao tự động kèm tóm tắt yêu cầu sang nhân viên chuyên trách; đồng thời loại bỏ nhóm đơn quốc tế ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên (audit) 100 đơn/tuần so với bảng giá cước ban hành hiện hành; ngưỡng cảnh báo khi có > 1% số đơn phát hiện chênh lệch | Tự động xóa bộ nhớ đệm (cache) khi hệ thống cập nhật bảng giá cước mới; bắt buộc ghi phiên bản bảng giá vào thuộc tính của `trace_id` | Kế toán trưởng |
