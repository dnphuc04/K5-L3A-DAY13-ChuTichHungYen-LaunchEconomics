# Phiếu chấm hội đồng Gate 2a

- Nhóm chấm: ChuTichHungYen · L3A
- Nhóm được chấm: DKKT · L3A
- Căn cứ: [Hồ sơ Launch v0 của DKKT](https://chatgpt.com/library?file_id=libfile_63aa8dae586881918531a5229aa58fdd&account_id=personal)
- Trạng thái: chấm sơ bộ trên hồ sơ Launch v0.

| Tiêu chí | Điểm | Lý do |
| --- | ---: | --- |
| Đề xuất khớp bằng chứng | 10/10 | Giới hạn pilot ở nội địa và hàng nặng. Khi xem lại 100%, chi phí ước tính lên 0,98–1,03 lần mức thủ công [simulated]. Nhóm yêu cầu xử lý lỗi hoàn trùng và đối soát sổ cái trước khi chạy. |
| Số giả lập và phạm vi | 10/10 | Ước tính chi phí có nhãn [simulated]. Yêu cầu quốc tế bị loại khỏi phạm vi vì chi phí 1,88 lần mức thủ công [simulated] và tỷ lệ thành công 27,3%. Có mốc thay thời gian giả lập bằng số đo thực tế sau tuần đầu. |
| Pilot ra được quyết định | 5/10 | Có đối chứng, 20 nhân viên mỗi nhánh và ngưỡng dừng cụ thể. Cần đối chiếu kế hoạch thu ít nhất 299 yêu cầu đủ điều kiện mỗi nhân viên, thời hạn áp dụng và người có quyền kích hoạt từng luật dừng trong pilot_plan.yaml. |
| **Tổng sơ bộ** | **25/30** | |

**Quyết định đề xuất của hội đồng — Go có điều kiện.**

**Lý do** — Phạm vi pilot có cơ sở kinh tế. Trước khi chạy, cần xác nhận đã sửa lỗi hoàn trùng và đối soát sổ cái, có lịch đủ mẫu và có người chịu trách nhiệm cho từng luật dừng. Với 40 nhân viên, thiết kế cần ít nhất 11.960 yêu cầu đủ điều kiện nếu phân bổ đều. Cần chừa đủ 7 ngày theo dõi mở lại sau khi đóng yêu cầu để kịp mốc 05/01/2027.

**Câu hỏi cho đội trình** — Với lịch tăng dần của pilot, mỗi nhân viên dự kiến nhận bao nhiêu yêu cầu nội địa và hàng nặng mỗi tuần? Nếu đến hạn chốt mẫu vẫn thiếu 859 yêu cầu hiệu dụng mỗi nhánh, nhóm sẽ gia hạn hay kết luận chưa đủ bằng chứng?

**Câu trả lời của đội trình** — Với 1.500 yêu cầu/ngày (81,8% thuộc noi_dia + hang_nang, tức ~1.227 yêu cầu/ngày), mỗi nhân viên xử lý trung bình ~215 yêu cầu đủ điều kiện/tuần, nên ở bước rollout 0,50 (20 + 20 nhân viên) sẽ đạt m >= 299 sau ~1,4 tuần (cộng thêm 7 ngày theo dõi mở lại là đủ kịp mốc nếu kéo dài đo hết 2 tuần ở bước 0,50). Nếu đến hạn chốt mẫu vẫn thiếu 859 yêu cầu hiệu dụng mỗi nhánh (và chưa vi phạm luật dừng), nhóm sẽ gia hạn thêm 1 tuần thu mẫu thay vì ép kết luận; nếu hết thời hạn gia hạn vẫn thiếu thì kết luận chưa đủ bằng chứng (không mở rộng).
