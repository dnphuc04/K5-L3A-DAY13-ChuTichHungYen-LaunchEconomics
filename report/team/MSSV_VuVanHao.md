# Báo cáo cá nhân — Vũ Văn Hảo

> **Lưu ý:** Đổi tên file này thành `<MSSV>_VuVanHao.md` (ví dụ: `2A2026xxxx_VuVanHao.md`) trước khi nộp bài.

## 1. Thông tin thành viên

- Họ tên: Vũ Văn Hảo
- MSSV: (Điền MSSV của bạn vào đây)
- Email: (Điền email của bạn vào đây)
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Chịu trách nhiệm thực hiện gắn nhãn độc lập 20 ca lỗi ở Checkpoint 3 (Nhiệm vụ C) theo chuẩn Google PAIR.
- So sánh bộ nhãn với Người gắn nhãn 1 (Lê Thái Dương), tính tỷ lệ đồng thuận và xây dựng quy tắc phân biệt cho các ca không trùng.
- Đồng xây dựng bảng khắc phục 5 ca đại diện với đầy đủ event phát hiện đo được, ngưỡng cảnh báo và vai trò phụ trách.
- Chủ trì tổng hợp, đồng bộ số liệu và hoàn thiện hồ sơ launch v0 tại [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) (Nhiệm vụ E) đúng hạn 17:00 phục vụ phiên duyệt chéo Gate 2a.
- Phối hợp xây dựng đặc tả chỉ số, danh sách 10 event có `trace_id` và phân tích rủi ro kinh tế trong [report/team/chi_so.md](chi_so.md).

## 3. Đóng góp cụ thể

- Hoàn thành bộ nhãn độc lập (cột "Nhãn người 2") cho cả 20 ca lỗi trong [bang_loi.md](bang_loi.md), đạt tỷ lệ đồng thuận 90% (18/20 ca) so với Người gắn nhãn 1.
- Soạn thảo quy tắc phân loại ranh giới giữa lỗi "Do người dùng" vs "Hệ thống" (ca 6) và lỗi "Hệ thống" vs "Ngầm" (ca 8).
- Điền đầy đủ 7 mục trong [ho_so_launch_v0.md](ho_so_launch_v0.md) chuẩn 1 trang:
  - Đảm bảo gán đúng nhãn `[simulated]` và trạng thái `Giả lập` cho mọi số liệu từ cột `_simulated`.
  - Phân định rõ vai trò chịu trách nhiệm cụ thể cho từng mục (không dùng "cả đội").
  - Xây dựng 4 điều kiện tiên quyết cho đề xuất "Go có điều kiện" sát với dữ liệu thực nghiệm.
  - Tuyệt đối không sử dụng từ ngữ bị cấm (chỉ dùng "pilot", không dùng từ chỉ chạy chính thức theo Quy tắc 5).

## 4. Bằng chứng

- File [report/team/bang_loi.md](bang_loi.md) (bộ nhãn người 2, tỷ lệ đồng thuận 90%, bảng 5 ca khắc phục).
- File [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) (hồ sơ launch v0 hoàn chỉnh 1 trang sẵn sàng trước 17:00).
- File [report/team/chi_so.md](chi_so.md) (đặc tả 10 event có `trace_id` và 3 dòng rủi ro kinh tế).
- File [report/team/group_report.md](group_report.md) (đồng tham gia soạn thảo báo cáo tổng kết nhóm).

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity AI Assistant.
- Mục đích: Hỗ trợ rà soát các tiêu chí rubric chấm điểm (C1–C8), kiểm tra lỗi định dạng file Markdown, đối chiếu chéo các event log tương ứng với từng chỉ số đo lường và soát lỗi quy chuẩn (tránh từ khóa bị cấm của Quy tắc 5, kiểm tra nhãn simulated).
- Cách tự kiểm tra: Chạy lệnh kiểm tra cú pháp yaml, kiểm tra sự tồn tại của từ khóa cấm qua lệnh tìm kiếm trong repo và đối chiếu thủ công từng con số với kết quả chạy từ `src/lab13.py`.

## 6. Tự đánh giá

- Hoàn thành xuất sắc nhiệm vụ: 10/10 điểm.
- Đảm bảo tiến độ mốc thời gian 17:00 của lớp và tuân thủ 100% các quy định liêm chính học thuật của lab.
