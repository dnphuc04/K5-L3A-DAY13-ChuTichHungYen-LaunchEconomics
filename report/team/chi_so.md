# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `(dong_trong_24h == 1 & mo_lai_trong_7_ngay == 0).mean()` | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()` trên các yêu cầu `duoc_xem_lai == 1` | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `(mo_lai_trong_7_ngay == 1).mean()` | 4,25% (51 / 1.200) |
| Dùng (đề xuất) | Tỉ lệ yêu cầu nhóm can thiệp được mở bằng trợ lý | Số yêu cầu phát sinh event `agent_suggestion_shown` chia tổng yêu cầu nhóm can thiệp | Không cần tính |
| An toàn (đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu ngẫu nhiên (bắt lỗi ngầm) | Số đơn có chênh lệch tiền hoàn chia tổng 100 đơn kiểm tra mẫu (audit) hàng tuần | Không cần tính |

*Ghi chú:* Chỉ số trong đợt chạy thử 1.200 yêu cầu là **82,83%**, không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử chưa có nhóm đối chứng đồng thời.

## Danh sách event

Gồm 10 event có gắn `trace_id` để liên kết đồng bộ với trace của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách hàng gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent trợ lý | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy agent (kể cả khi lỗi) |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `noi_dung_goi_y`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho CSKH |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên xác nhận gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai`, `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn thành xử lý lại ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent trợ lý | `reason`, `tom_tat_van_de`, `trace_id` | Khi agent vượt giới hạn hoặc lỗi cần chuyển người |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `so_gio_xu_ly`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng | `reopened_at`, `ly_do_mo_lai`, `trace_id` | Khi khách mở lại khiếu nại trong 7 ngày |
| `audit_sample_checked` | Kế toán trưởng | `so_tien_da_hoan`, `so_tien_chuan`, `lech`, `trace_id` | Định kỳ hàng tuần khi kiểm toán mẫu |

**Kiểm tra chéo:**
- **Chỉ số chính (% đóng 24h & không mở lại 7 ngày):** Tính từ `ticket_closed` (`so_gio_xu_ly <= 24`) và không có event `ticket_reopened` với cùng `trace_id` trong vòng 7 ngày.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Tính từ event `staff_review_decision` khi trường `quyet_dinh` nhận giá trị `sua` hoặc `bo`.
- **Chỉ số an toàn (Tỉ lệ mở lại 7 ngày):** Đếm số event `ticket_reopened` chia cho tổng số event `ticket_closed`.
- **Chỉ số dùng đề xuất:** Đếm số event `agent_suggestion_shown` chia cho tổng số event `refund_request_created` có `arm == 'intervention'`.
- **Chỉ số an toàn đề xuất:** Tính từ event `audit_sample_checked` với điều kiện `lech != 0`.

## E2 · Rủi ro kinh tế

Các số liệu lấy trực tiếp từ bảng phân tích độ nhạy (`bang_chi_phi.md`):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, lên **6.787 đ** [simulated] | Tỉ lệ làm lại theo tuần vượt quá 7% (đợt chạy thử: 4,9% trong phạm vi) | Tạm thời thu hẹp phạm vi về riêng `noi_dia`, rà soát 20 trace gần nhất có ca làm lại | PM trợ lý hoàn phí |
| Tình trạng xem lại 100% kéo dài | Chi phí lên **11.743 đ (0,98×)** đến **12.414 đ (1,03×)** [simulated], triệt tiêu lợi nhuận | Tỉ lệ yêu cầu được xem lại vẫn > 50% vào cuối giai đoạn rollout 25% | Kích hoạt lộ trình giảm xem lại theo bậc đối với nhân viên đạt tỉ lệ sửa/bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thực tế thấp | Chi phí cố định 40 tr/tháng làm tăng **+1.185 đ/việc** (ở 45.000 yc/tháng) và tăng **+2.370 đ/việc** nếu khối lượng giảm 50% [simulated] | Số yêu cầu thành công trung bình tuần đạt dưới 50% kế hoạch dự kiến | Dừng mở rộng quy mô pilot, đàm phán lại chi phí bản quyền/hạ tầng cố định | PM trợ lý hoàn phí |
