# Sổ Tay Quân Sư S2 – Tam Quốc Tứ Thời Ca

Sổ tay xây đội, quản lý kho tướng và tài nguyên cho server mới của **Tam Quốc Tứ Thời Ca**.

- **Bản GitHub Pages:** https://vienkendo.github.io/so-tay-quan-su-s2/ — Kho lưu trong trình duyệt; bật **Kho → Đồng bộ GitHub** để đồng bộ nhiều máy qua repo riêng tư (`kho.json`).
- **Bản web Claude:** cùng mã nguồn, Kho đồng bộ đám mây theo tài khoản Claude, có thêm đọc ảnh bằng Claude.

## Các mục

Trên điện thoại, bấm **Menu** để mở thanh bên và chọn nhóm chức năng.

| Nhóm | Dùng khi nào |
|---|---|
| Tổng quan | Kiểm tra kho, xem đội PVP và việc có thể làm; mở kế hoạch đầy đủ khi cần |
| Kho & nâng cấp | Quản lý tướng, sao và tài nguyên; xem điều kiện nâng sao |
| Đội hình & đối đầu | Xem và chọn đội PVP/Boss/PVE; phân tích đội địch và ghi nhật ký trận |
| Trợ trận | Công pháp, thần thú, linh phù, chiến hồn, tuyệt kỹ và trang bị |
| Tra cứu & sự kiện | Tra cứu tướng, quy tắc, cẩm nang; xem lịch sự kiện và Cổ Đế Viêm |

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
  5→6: 1 bản · 1×5★ · 0 — 6→7: 0 · 2×5★ · 1000 — 7→8: 0 · 1×6★ · 1000 — 8→9: 1 · 1×8★ · 2000 — 9→10: 0 · 1×6★ · 1000 — 10→11: 1 · 1×8★ · 3000 — 11→12: 0 · 1×6★ · 2000 — 12→13: 1 · 1×8★ · 5000 — 13→14: 0 · 2×6★ · 2500 — 15★→Nhập Thánh 1: 2 bản · 1×10★ · 5000 — NT2→NT3: 4 ô × 3000 cầu (bản trùng 6★ / tướng 8★ / 7★ / 10★ bất kỳ).
- **Ô công pháp theo sao:** 6★: 2 · 9★: 3 · 10★: 5 · 12★: 6 · 14★: 7 · 15★: 8.
- **Công pháp:** số người đeo = sao sách + 1. Bản trùng để lên sao: Tím 2→4→8→16→32; Cam/Đỏ 1→2→4→8→16 (mỗi sao gấp đôi).
- **Mảnh:** 50 mảnh = 1 tướng / 1 thần thú; 100 Mảnh Vạn Năng = chọn 1 tướng bất kỳ; ghép mảnh phe 5★ ra tướng ngẫu nhiên.
- **Trận:** PVP tối đa 20 hiệp, các phụ bản khác 15, Rèn luyện Bang 5 hiệp; hết hiệp chưa hạ hết địch là thua. PVP: **bên phòng thủ đi trước** – thần thú có kỹ năng ra chiêu của bên phòng thủ đánh đầu tiên, rồi ra đòn xen kẽ (địch 1 → ta 1 → địch 2…), PVE đội ta ra trước. Đòn đơn thể đánh cùng làn dọc (1–4, 2–5, 3–6), ô trước trước.
- **Lực chiến:** 1 vạn = 10.000 (ví dụ "290vạn6676" = 2.906.676).
- **Linh phù:** cộng cho toàn bộ tướng; Công Lam 1.000 → Tím 2.000 → Cam 4.000 → Đỏ 8.000 → Vàng 1★ 10.000 (+5%)…

Điểm 1–5 và radar vai trò là đánh giá suy ra từ mô tả kỹ năng, không phải số liệu game.
