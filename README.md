# Sổ Tay Quân Sư S2 – Tam Quốc Tứ Thời Ca

Sổ tay xây đội, quản lý kho tướng và tài nguyên cho server mới của **Tam Quốc Tứ Thời Ca**.

- **Bản GitHub Pages:** https://vienkendo.github.io/so-tay-quan-su-s2/ — Kho lưu trong trình duyệt; bật **Kho → Đồng bộ GitHub** để đồng bộ nhiều máy qua repo riêng tư (`kho.json`).
- **Bản web Claude:** cùng mã nguồn, Kho đồng bộ đám mây theo tài khoản Claude, có thêm đọc ảnh bằng Claude.

## Các mục

| Menu | Nội dung |
|---|---|
| Đội hình | Đội PVP/Tháp, Boss, PVE; Tình nghĩa, Chiến Sách, mốc sao kế tiếp, tải ảnh đội; **radar vai trò** và so sánh 2 đội |
| Tướng | Danh sách, lọc phe/nhóm/giữ, chi tiết kỹ năng 9★/11★/13★/Nhập Thánh |
| Phân tích | Lọc theo phe, nhóm, từ khóa kỹ năng; so sánh 2 tướng |
| Đối đầu | 9 phụ bản (PVP 20 hiệp, Tháp, PVE ngày, Trấn thủ, Nam chinh, Rèn luyện Bang 5 hiệp…), cấp/sao từng ô địch, lực chiến, thứ tự ra đòn, đánh theo làn, gợi ý khắc chế từ kho, nhật ký trận |
| Kho | Thẻ từng bản tướng, nâng sao theo bảng chi phí thật, thêm nhanh/nhập nhanh, hoàn tác, sao lưu; độ phủ vai trò |
| Trợ trận | **Công pháp** (kho sách, phân sách, chi phí bản trùng) · **Thần thú** · **Linh phù** · **Trang bị** (chờ dữ liệu) |
| Nâng sao | Kế hoạch nâng sao lấy trực tiếp từ Kho |
| Quy tắc | Nguyên tắc xây đội |
| Cổ Đế Viêm | Số liệu trận boss sự kiện + ghi chú |
| Cẩm nang | Phe, vai trò, phẩm chất, các bước dựng đội |

## Cấu trúc

```
index.html, script.js, style.css   ← SINH TỰ ĐỘNG, không sửa tay
assets/                            ← favicon, ảnh; assets/icons/books/*.jpg = icon công pháp (96×96)
src/
  tpl_s2.html       template duy nhất (HTML + CSS + JS)
  data_s2.py        tướng đang dùng, đội hình, thứ tự nâng sao
  heroes_base.py    dữ liệu kỹ năng gốc 27 tướng
  enemy_db.py       phân loại vai trò mọi tướng (dùng cho Đối đầu, radar)
  icons_s2.json     icon tướng (base64)
  book_icons.json   tên công pháp → đường dẫn icon trong assets/icons/books/
  kho_default.json  kho mặc định khi trình duyệt chưa có dữ liệu
  make.py           build
```

## Build

```bash
python3 src/make.py            # ghi index.html/script.js/style.css ở gốc repo
                               # + build/So_tay_quan_su_S2.html (offline 1 file)
                               # + build/so_tay_quan_su_s2_web.html (bản web Claude)
```

Chỉ cần Python 3, không phụ thuộc thư viện ngoài. Thư mục `build/` không commit.

## Cơ chế game đã xác nhận

- **Sao:** vàng 1–5 = 1–5★, đỏ 1–5 = 6–10★, cầu vồng = 11–15★, sau đó Nhập Thánh.
- **Mặc định khi nhận:** SSR+ 5★, SSR (cam, nguyên liệu) 5★, SR (tím) 4★, R (xanh) 3★.
- **Chỉ SSR+ là tướng thật:** SSR cam chỉ dùng làm nguyên liệu nâng sao; kỹ năng/tiềm năng của SSR, SR, R chỉ để phân tích đội địch (Đối đầu). Quy tắc, gợi ý đội, radar kho chỉ xét SSR+.
- **Chi phí nâng sao** (bản trùng · tướng cùng phe làm nguyên liệu · cầu cam):
  5→6: 1 bản · 1×5★ · 0 — 6→7: 0 · 2×5★ · 1000 — 7→8: 0 · 1×6★ · 1000 — 8→9: 1 · 1×8★ · 2000 — 9→10: 0 · 1×6★ · 1000 — 10→11: 1 · 1×8★ · 3000 — 11→12: 0 · 1×6★ · 2000 — 12→13: 1 · 1×8★ · 5000 — 13→14: 0 · 2×6★ · 2500.
- **Ô công pháp theo sao:** 6★: 2 · 9★: 3 · 10★: 5 · 12★: 6 · 14★: 7 · 15★: 8.
- **Công pháp:** số người đeo = sao sách + 1. Bản trùng để lên sao: Tím 2→4→8→16→32; Cam/Đỏ 1→2→4→8→16 (mỗi sao gấp đôi).
- **Mảnh:** 50 mảnh = 1 tướng / 1 thần thú; 100 Mảnh Vạn Năng = chọn 1 tướng bất kỳ; ghép mảnh phe 5★ ra tướng ngẫu nhiên.
- **Trận:** PVP tối đa 20 hiệp, các phụ bản khác 15, Rèn luyện Bang 5 hiệp; hết hiệp chưa hạ hết địch là thua. PVP ra đòn xen kẽ (địch 1 → ta 1 → địch 2…), PVE đội ta ra trước. Đòn đơn thể đánh cùng làn dọc (1–4, 2–5, 3–6), ô trước trước.
- **Lực chiến:** 1 vạn = 10.000 (ví dụ "290vạn6676" = 2.906.676).
- **Linh phù:** cộng cho toàn bộ tướng; Công Lam 1.000 → Tím 2.000 → Cam 4.000 → Đỏ 8.000 → Vàng 1★ 10.000 (+5%)…

Điểm 1–5 và radar vai trò là đánh giá suy ra từ mô tả kỹ năng, không phải số liệu game.
