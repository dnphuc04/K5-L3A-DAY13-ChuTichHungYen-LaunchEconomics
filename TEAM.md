# Team

## Thông tin nhóm

- Tên nhóm: ChuTichHungYen
- Lớp: L3A 
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |   Đồng Ngọc Phúc     |   2A202603399   |   dnphuc04@gmail.com    |    dnphuc04    |    Trưởng nhóm, giữ hồ sơ và kiểm tra từng giai đoạn     |
|   2 |    Nguyễn Việt Hưng    |   2A2026   |       |        |    Người kiểm số     |
|   3 |    Vũ Văn Hảo    |      |       |        |    Người gán nhãn 2     |
|   4 |   Lê Thái Dương    |      |       |        |    Người gán nhãn 1     |
|   5 |   Nguyễn Huy Hoàng    |   2A202603366   |  nguyenhuyhoangtuho@gmail.com     |    nguyen-huy-hoang-1708    |    Người viết code     | 

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## VuVanHao

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ: Gắn nhãn độc lập 20 ca lỗi ở CP3; hoàn thiện và giữ hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`) cho Gate 2a; đồng phụ trách `report/team/bang_loi.md` và `report/team/chi_so.md`.

### Đóng góp cụ thể

- Hoàn thành bộ nhãn người 2 cho 20 ca lỗi đạt tỷ lệ đồng thuận 90% (18/20 ca) với người 1; xây dựng quy tắc phân biệt cho ca 6 và ca 8.
- Xây dựng bảng khắc phục 5 ca lỗi đủ 5 nhóm Google PAIR với cách phát hiện đo được bằng event và vai trò phụ trách cụ thể.
- Tổng hợp và hoàn thiện `ho_so_launch_v0.md` chuẩn 1 trang, đủ 7 mục, 100% số giả lập gắn nhãn `[simulated]` và trạng thái Giả lập, không dùng từ "production", đề xuất "Go có điều kiện" kèm 4 điều kiện khả thi.
- Soạn thảo đặc tả 10 event có `trace_id` và 3 dòng rủi ro kinh tế trong `chi_so.md`.

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/chi_so.md`, `report/team/group_report.md`, `report/team/MSSV_VuVanHao.md`.

## NguyenHuyHoang-2A202603366

### Phần việc phụ trách

- Người viết code: `src/lab13.py` (A1–A4, B1–B4, D1, tính thử E1 và tỉ lệ mở lại cho D3); cùng người kiểm số điền `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Ba hàm A1 (ĐẠT 1,20 · 1,25 · 1,25), `mo_hinh` (4.472 đ/việc thành công [simulated], 16,3× hoá đơn/yêu cầu), bảng A3 theo loại, A4 cố định, 9 kịch bản B1, B2, B3, B4, cỡ mẫu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299).

### Bằng chứng

- `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/MSSV_NguyenHuyHoang.md`; output `cd src && python lab13.py`.
