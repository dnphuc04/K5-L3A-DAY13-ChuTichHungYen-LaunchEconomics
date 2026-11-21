# Báo cáo nhóm · LogiX-VN Gate 2a

Báo cáo ngắn gọn tổng kết hồ sơ launch v0 của nhóm ChuTichHungYen.

## 1. Thông tin nhóm

- Tên nhóm: ChuTichHungYen
- Lớp: L3A
- Repo: `K5-L3A-DAY13-ChuTichHungYen-LaunchEconomics`
- Thành viên: xem chi tiết tại [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ hồ sơ launch v0 và kế hoạch pilot bảo vệ trước hội đồng Gate 2a nhằm giải quyết 4 bài toán cốt lõi:
1. **Hiệu quả kinh tế:** Tính toán chi phí thực tế cho mỗi yêu cầu được giải quyết thành công (Cost-of-Pass), so sánh với chi phí nhân viên tự xử lý thủ công (12.000 đ/yêu cầu).
2. **Hành vi sử dụng:** Đo lường tỷ lệ nhân viên bỏ qua gợi ý và xác định danh sách các event log cần thiết để theo dõi.
3. **Quản trị rủi ro & Lỗi:** Phân loại 20 ca lỗi thực tế theo 5 nhóm nguyên nhân gốc của Google PAIR, gán cơ chế phát hiện đo được và chỉ định người chịu trách nhiệm.
4. **Thiết kế thử nghiệm có đối chứng (A/B Test / Pilot):** Đảm bảo thử nghiệm phân tách được tác động độc lập của agent, đủ cỡ mẫu hiệu dụng và có luật dừng an toàn viết trước.

## 3. Giải pháp thực hiện

- **Nhiệm vụ A (Mô hình chi phí):** Viết code `src/lab13.py` vượt qua 3 phép thử kiểm định A1 (1,20 · 1,25 · 1,25). Tính toán từ trace 1.624 lượt chạy và 1.200 yêu cầu; phân rã chi phí theo 4 loại yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và cộng chi phí cố định 40 triệu đ/tháng. Báo cáo chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (Phân tích độ nhạy):** Chạy 9 kịch bản thay đổi tham số đơn lẻ, 1 kịch bản tác động cặp (chứng minh tính cộng tuyến tính); đánh giá điểm tối ưu chi phí toàn hệ thống theo số lần chạy lại (giới hạn 2 lần rẻ nhất) và kịch bản xem lại 100%. Báo cáo chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi và cách khắc phục):** Hai người gắn nhãn độc lập (Lê Thái Dương và Vũ Văn Hảo) phân loại 20 ca lỗi vào 5 nhóm của Google PAIR, đạt tỉ lệ đồng thuận 90% (18/20 ca); hoàn thiện bảng khắc phục 5 ca đại diện có event, ngưỡng cảnh báo và vai trò phụ trách. Báo cáo chi tiết: [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính toán cỡ mẫu D1 (1.251 theo yêu cầu, 3.103 theo nhân viên); lựa chọn phân cụm ngẫu nhiên theo nhân viên (20 đối chứng + 20 can thiệp, phân tầng 12 depot) với MDE 6 điểm phần trăm; hoàn thiện kế hoạch với 3 luật dừng chuẩn NẾU – TRONG – THÌ – KHÔNG THÌ. Báo cáo chi tiết: [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, rủi ro & Hồ sơ launch v0):** Tổng hợp 3 chỉ số chạy thử, bổ sung 2 chỉ số đề xuất, đặc tả 10 event có `trace_id`, lượng hóa 3 rủi ro kinh tế và đóng gói hồ sơ launch v0 trong 1 trang chuẩn. Báo cáo chi tiết: [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả chính

- **Chi phí mỗi việc thành công:** Đạt **4.472 đ** [simulated] (gấp 16,3 lần hoá đơn token + tool 274,7 đ; giờ nhân viên xem lại và làm lại chiếm 92,5% chi phí). Khi cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở quy mô 45.000 yêu cầu/tháng là **4.599 đ = 0,38×** [simulated].
- **Chi phí toàn hệ thống:** Đạt **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ của nhân viên tự làm [simulated] (đã tính chi phí nhân viên làm thay 222 ca không thành công).
- **Phạm vi pilot tối ưu:** Đề xuất chỉ chạy cho `noi_dia` (0,22×) và `hang_nang` (0,69×); loại bỏ hoàn toàn `quoc_te` (1,88×, chạy lại không hiệu quả) và `doi_tac` (0,85× sát ngưỡng).
- **Độ nhạy:** Số ca làm lại (±51,8%) và tỉ lệ xem lại (±40,7%) là hai yếu tố chi phối mạnh nhất; giá token chỉ tác động ±5,6%.
- **Đề xuất cuối cùng:** **Go có điều kiện** tại Gate 2a kèm 4 điều kiện tiên quyết (sửa lỗi sổ cái trước khi chạy, Giám đốc vận hành chấp nhận MDE 6 điểm, đo thật số phút nhân viên sau tuần 1 và ban hành lộ trình giảm tỷ lệ xem lại theo bậc).

## 5. Khó khăn và cách xử lý

- *Tính toán cỡ mẫu khi phân cụm nhân viên:* Với 40 nhân viên, nhóm chọn MDE 6 điểm phần trăm ở power 0,80. Mỗi nhánh cần 859 yêu cầu hiệu dụng, tương ứng mục tiêu thu 5.980 yêu cầu (20 nhân viên × 299 yêu cầu). Nếu tác động thực là 5 điểm phần trăm, power giảm còn khoảng 0,64.
- *Nguy cơ chi phí vượt ngưỡng khi xem lại 100%:* Kết quả B4 chỉ ra nếu phải xem lại 100% với thời gian làm lại thực tế (15,3 phút), chi phí tăng lên 12.415 đ (1,03×), đắt hơn nhân viên tự làm. Nhóm đã đưa điều kiện xây dựng lộ trình giảm tỷ lệ xem lại theo bậc vào điều kiện bắt buộc của Gate 2a.

## 6. Tổng hợp đóng góp

- Thành viên phân vai rõ ràng, phối hợp theo đúng checklist và hoàn thành 100% đúng hạn. Chi tiết phân công và đóng góp cá nhân được ghi cụ thể tại [TEAM.md](../../TEAM.md) và báo cáo cá nhân từng thành viên.

## 7. Hạn chế và hướng cải thiện

- Toàn bộ thời gian xem lại và làm lại hiện đang dựa trên dữ liệu mô phỏng (`_simulated`). Cần nhanh chóng thu thập dữ liệu đo thật từ hệ thống ngay sau tuần đầu tiên của pilot (rollout 10%).
- Hiện tượng chạy lại nhiều lần không cải thiện được tỷ lệ thành công cho nhóm đơn quốc tế, cần nghiên cứu agent chuyên biệt hoặc tài liệu hóa quy trình cho nhân viên thay vì dùng chung agent.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*.
- Thư viện Python `statsmodels` (phân tích kiểm định tỷ lệ và cỡ mẫu `NormalIndPower`).
