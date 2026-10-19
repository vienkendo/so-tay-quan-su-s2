# Handoff – Sổ Tay Quân Sư (Tam Quốc Tứ Thời Ca)

Cập nhật: 11/10/2026. Người chơi: Viên (nick Vienkendo). Mục tiêu: xây đội hình PVP / Boss / PVE tối ưu theo **tiềm năng tối đa** (không theo sao hiện tại), xuất ra trang guide HTML chạy offline.

## 1. Sản phẩm hiện có

| File | Nội dung |
|---|---|
| `So_tay_quan_su.html` | Guide offline 1 file (~370 KB, ảnh nhúng base64). 5 tab: Đội hình, Tướng, Công pháp, Nâng sao, Quy tắc. Không gọi mạng, nhớ tab/bộ lọc bằng localStorage. |
| `Doi_hinh_Tam_Quoc.xlsx` | Bản Excel cũ (4 sheet). **Chưa có** dữ liệu công pháp, ô công pháp, icon. |
| `src/build.py` | Nguồn dữ liệu tướng: list `H` (27 tướng), `TEAMS` (4 đội), `UP` (chi phí nâng sao), `PR` (thứ tự mốc). Chạy ra file xlsx. |
| `src/books_data.py` | `BOOKS` (22 công pháp), `ALLOC` (phân sách 7 tướng chính), `WHY` (lý do). |
| `src/guide_tpl.html` | Template HTML/CSS/JS. Placeholder: `/*__DATA__*/null`, `/*__ICONS__*/{}`, `/*__BOOKICONS__*/{}`. |
| `src/gen_html.py` | Ghép dữ liệu + icon vào template → `So_tay_quan_su.html`. |
| `src/icons.json`, `src/books.json` | Icon tướng (27) và icon công pháp (22), JPEG base64. |

**Build lại:** sửa đường dẫn tuyệt đối trong `gen_html.py` (đang trỏ tới `/tmp/claude-0/.../scratchpad/` và `/home/claude/icons_work/`) rồi `python3 gen_html.py`. Sửa dữ liệu ở `build.py` / `books_data.py`, không sửa trực tiếp file HTML đầu ra.

## 2. Cơ chế game đã xác nhận (từ ảnh)

- **Màu sao:** vàng 1–5 = 1–5★, đỏ 1–5 = 6–10★, cầu vồng 1–5 = 11–15★, sau đó Nhập Thánh.
- **Mốc Đặc tính:** 9★, 11★, 13★, Nhập Thánh. Các mốc còn lại chỉ cộng chỉ số. 6★ luôn là Nộ cơ bản +2.
- **Ô công pháp theo sao:** 6★: 2 · 9★: 3 · 10★: 5 · 12★: 6 · 14★: 7 · 15★: 8.
- **Nâng sao tướng:** tốn nguyên liệu (quả cầu cam) + có thể cần 1 bản sao + tướng cùng phe đạt số sao yêu cầu (bị tiêu hao). Nguyên liệu hiện có: 1022.
- **Công pháp:** sao của sách quyết định số người đeo cùng lúc (ví dụ cam 0★=1, 1★=2, 2★=3; tím 3★=4, 4★=5). "Sở hữu" = bản dư để nâng sao sách. Mỗi sao sách cộng cấp Bảo Điển (Tím +1, Cam +5, Đỏ +10). Bảo Điển hiện Lv163; Lv200 = +7% Tăng ST, +7% Giảm ST.
- **Phe:** 3Q, Hán, Tần, Đường. **Nhóm:** Công, Thủ, Trợ, Thuật Sĩ.
- **Đội hình:** 6 tướng, 2 hàng × 3 cột (hàng trước / hàng sau).

## 3. Đội hình đã chốt

| Chế độ | Hàng trước (cột 1–3) | Hàng sau (cột 1–3) |
|---|---|---|
| PVP | Lý Long Cơ, Vương Chiêu Quân, Võ Tắc Thiên | Lữ Bố, Tây Thi, Điêu Thuyền |
| Boss | Lý Long Cơ, Ban Chiêu, Vương Chiêu Quân | Lữ Bố, Tây Thi, Điêu Thuyền |
| PVE (Tần, Huyết Tích) | Bạch Khởi, Can Tương, Chung Vô Diệm | Tần Thủy Hoàng, Quỷ Cốc Tử, Biển Thước |
| Hán (Boss 2) | Hàn Tín, Vệ Thanh, Vương Chiêu Quân | Lưu Bang, Ngu Cơ, Ban Chiêu |

Dự bị đổi theo đối thủ PVP: Gia Cát Lượng (choáng), Lỗ Trí Thâm (khiêu khích), Chân Cơ (khiên), Biển Thước.

## 4. Quy tắc cốt lõi

1. **Carry (Lữ Bố) phải có Công cao nhất đội, vượt trội.** Các hiệu ứng nhắm "tướng Công cao nhất": liên kết Điêu Thuyền 9★, chuyển Nộ Quỷ Cốc Tử 9★, Nhập Thánh Tây Thi, ra đòn thêm Vương Chiêu Quân 9★. Không đeo Tuân Úc (Lực Công) cho hỗ trợ; cẩn thận Lý Long Cơ 14–15★ (+Công).
2. Lữ Bố: mỗi Nộ +15% ST chung cuộc, không bao giờ dùng kỹ năng → mọi nguồn Nộ đều quý.
3. Lữ Bố đứng cùng cột với Lý Long Cơ để cùng đánh mục tiêu mang [Trường Hận].
4. Một đội chỉ một carry dựa vào Công; hỗ trợ/tank build HP, Thủ, Miễn ST.
5. Dồn tài nguyên một đội trước; ưu tiên mốc Đặc tính gần đạt.

## 5. Thứ tự nâng sao

1. Vương Chiêu Quân 9★ (Lữ Bố ra đòn thêm; +1 ô công pháp)
2. Võ Tắc Thiên 9★ (cả đội +1 Nộ; +1 ô)
3. Ban Chiêu 11★ (+30% Bạo Kích, +18% ST). Cần 3000 nguyên liệu + tướng Hán 8★ — **không dùng Vương Chiêu Quân làm nguyên liệu.**
4. Tây Thi 13★ → 15★ → Nhập Thánh (Lữ Bố tới +6 Nộ mỗi lần Tây Thi thi triển). 13★ cần 5000 + tướng Tần 8★.
5. Vương Chiêu Quân 11★ → 13★; Lý Long Cơ Nhập Thánh; Gia Cát Lượng 9★; đội Tần/Hán sau cùng.

## 6. Phân công pháp (đã kiểm tra không vượt giới hạn người đeo)

| Tướng (sao · ô) | Công pháp |
|---|---|
| Lữ Bố (12★ · 6) | Tây Thi, Tôn Sách, Lý Long Cơ, Chân Cơ, Vệ Thanh, Trương Công Cẩn |
| Lý Long Cơ (13★ · 6) | Triệu Vân, Hoắc Khứ Bệnh, Tôn Sách, Bạch Khởi, Liêm Pha, Thái Bình Công Chúa |
| Tây Thi (12★ · 6) | Thái Văn Cơ, Thượng Quan Uyển Nhi, Thái Bình Công Chúa, Liêm Pha, Thuần Vu Quỳnh, Trương Mạn Thành |
| Điêu Thuyền (11★ · 5) | Hồng Phất Nữ, Ban Chiêu, Thượng Quan Uyển Nhi, Thái Bình Công Chúa, Liêm Pha |
| Ban Chiêu (10★ · 5) | Hồng Phất Nữ, Thái Bình Công Chúa, Thuần Vu Quỳnh, Trương Mạn Thành, Liêm Pha |
| Vương Chiêu Quân (8★ · 2) | Thái Bình Công Chúa, Trương Mạn Thành (9★: thêm Liêm Pha/Triệu Vân — lưu ý Liêm Pha đã 4/4) |
| Võ Tắc Thiên (8★ · 2) | Bạch Khởi, Trương Mạn Thành |

Đã hết chỗ: Thái Bình Công Chúa 5/5, Liêm Pha 4/4, Tôn Sách 2/2, Bạch Khởi 2/2, Hồng Phất Nữ 2/2, Thượng Quan 2/2, Hoắc Khứ Bệnh, Thái Văn Cơ, Ban Chiêu, Vệ Thanh 1/1. Còn trống: Tây Thi 2, Triệu Vân 2, Trương Công Cẩn 3, Thuần Vu Quỳnh 2, Trương Mạn Thành 1, Tuân Úc 4, Bách Lý Hề 4, Khương Duy 3, Lý Tú Ninh 2, Lỗ Ban 1, Lý Long Cơ 1, Chân Cơ 1.

## 7. Việc còn mở

- **Chưa có dữ liệu (ảnh bị cắt):** Lữ Bố 13★, Võ Tắc Thiên 13★, Quỷ Cốc Tử 13★, Can Tương (vế sau tuyệt chiêu), Điêu Thuyền 13★ & Nhập Thánh, Chân Cơ 13★ & Nhập Thánh.
- **Chưa có ảnh kỹ năng:** Hồng Phất Nữ, Thương Ưởng → chưa chấm điểm.
- **Cần kiểm tra trong trận:** ST Bạo 130% là tổng hay phần cộng thêm; Nộ tối đa của Lữ Bố; Ban Chiêu 11★ buff cả đội hay chỉ người được hồi; boss có miễn khống chế không; khiêu khích có chặn đòn diện rộng không; game có cho dùng chung tướng giữa các đội không (ảnh hưởng đội Hán).
- **Excel chưa đồng bộ** với HTML (thiếu công pháp, ô công pháp).
- Điểm 1–5 là đánh giá của Claude dựa trên mô tả kỹ năng, không phải số liệu game.
