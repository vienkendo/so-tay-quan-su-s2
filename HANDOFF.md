# HANDOFF — Sổ Tay Quân Sư S2

> **21/10/2026 – tạm ngưng bản web Claude (artifact).** Chỉ cập nhật bản GitHub Pages; Kho chính nằm ở repo riêng `so-tay-data`. `make.py` vẫn sinh `build/so_tay_quan_su_s2_web.html` nhưng không publish cho tới khi người chơi yêu cầu lại.

> Bàn giao cho agent/phiên làm việc tiếp theo. Cập nhật: 2026-10-21.

## 1. Nguồn sự thật duy nhất

- Mọi thay đổi sửa trong `src/` rồi chạy `python3 src/make.py`.
- `index.html`, `script.js`, `style.css` ở gốc repo là **file sinh tự động**: sửa tay sẽ bị ghi đè ở lần build sau.
- Cùng một template sinh ra 3 bản:
  1. **GitHub Pages:** Kho lưu `localStorage`.
  2. **Web Claude (artifact):** Kho đồng bộ đám mây qua `window.claude` (`db`, `user`), đọc ảnh qua `sample`, tải ảnh qua `downloads`.
  3. **File offline:** một file duy nhất.
- Mọi tính năng phụ thuộc `window.claude` đều tự tắt khi không có (nút đọc ảnh ẩn; tải ảnh rơi về thẻ `<a download>`).

## 2. Thay đổi 21/10/2026 (gộp hai nhánh phát triển)

Trước đó repo (khởi tạo từ một bản HTML cũ ngày 19/10) và bản web Claude phát triển song song. Đã gộp lại:

- **Sửa lỗi nghiêm trọng:** `renderInventoryMatrix()` dùng `SAMPLE_HERO_STATS` trước khi khai báo, gây ReferenceError ở dòng khởi tạo nên Kho, Nâng sao, Đối đầu không chạy.
- **Lấy bản web Claude làm gốc:** phụ bản, lực chiến, thứ tự ra đòn, làn, Chiến Sách, nhật ký trận, kho công pháp, chi phí bản trùng, tướng mới (Mạc Tà, Lữ Hậu…).
- **Giữ lại từ repo:** theme vàng–đỏ rượu, logo `site-icon-fantasy.jpg`, header gọn khi xoay ngang, tab **Phân tích**, **Cổ Đế Viêm** (ghi chú giờ lưu cùng Kho), **Cẩm nang**.
- **Radar viết lại theo dữ liệu thật.** Bản cũ chấm điểm từ chỉ số giả (`SAMPLE_HERO_STATS`: Thủ suy từ Công, HP = sao×1000, tên tướng gán cứng). Radar mới tính 7 trục từ phân loại kỹ năng trong `enemy_db.py` và số ô công pháp theo sao trong Kho. Đã bỏ hẳn `CURRENT_STARS`, `SAMPLE_*`, gợi ý đội từ điểm giả.
- **Menu Trợ trận** gồm 4 tab con:
  - Công pháp.
  - Thần thú: tướng đang có, mảnh, thứ tự chọn, thiên phú Lộc Thục.
  - Linh phù: phẩm từng ô, tổng chỉ số.
  - Trang bị: chưa có dữ liệu.
- **Kho mặc định** = kho thật lúc 21/10 (135 bản, 12.473 cầu cam), trong `src/kho_default.json`.

## 3. Đồng bộ trên bản GitHub

- **Cách hoạt động:** Kho → **Đồng bộ GitHub** lưu `kho.json` vào repo riêng tư (mặc định `vienkendo/so-tay-data`) qua GitHub Contents API.
- **Token:** fine-grained, chỉ cấp quyền *Contents: Read and write* cho đúng repo đó. Mỗi máy nhập 1 lần, lưu ở `localStorage.ghsync`.
- **Khi mở trang:** đọc bản trên GitHub.
  - Nếu máy này có thay đổi chưa đẩy (`gh_dirty`) mà bản GitHub không mới hơn lần đồng bộ trước (`gh_ts`), máy này đẩy lên.
  - Nếu bản GitHub mới hơn, trang lấy bản đó; dữ liệu cũ của máy vẫn lấy lại được bằng nút Hoàn tác.
- **Ghi:** mỗi lần lưu, sau 0,6 giây đẩy lên (1 commit). Nếu sha lệch thì đọc lại sha rồi thử lại 1 lần.
- **Tự kéo bản mới:** mỗi 60 giây khi tab đang mở và khi quay lại tab (có dùng ETag).
- **Kiểm thử:** giả lập API bằng Playwright với 2 máy (kết nối, sửa, máy kia nhận) và token sai.

## 3b. Lưu trữ

| Khóa | Nội dung |
|---|---|
| `localStorage.kho2` | `{k, log, undo, orb, m5, lv, atk, x}` |
| `x.books` / `x.alloc` | Kho công pháp / phân sách |
| `x.battles`, `x.orbDay`, `x.hlv` | Nhật ký trận, cầu cam mỗi ngày, cấp từng tướng |
| `x.tt` | Thần thú: `{own, manh, camPick, food}` |
| `x.lp` | Linh phù: `{<thú>: [HP, Công, Thủ, Tăng/Giảm ST]}`, chỉ số phẩm −1..9 |
| `x.cdv` | Ghi chú Cổ Đế Viêm |
| `x.bdlv` | Cấp Bảo Điển (Lv130 ngày 21/10) |
| `localStorage.vs2` | Đội địch đang nhập ở Đối đầu |

Trên web Claude, cùng cấu trúc được lưu ở `data/users/me/kho`.

## 4. Còn thiếu dữ liệu (cần ảnh từ người chơi)

- Kỹ năng các tướng SR: Tuân Úc, Mị Nguyệt, Liêm Pha, Võ Tòng, Thái Bình Công Chúa, Khương Duy…
- Linh phù: số phù cùng bậc để ghép, giá trị ô Tăng/Giảm ST, điều kiện mở kỹ năng linh thú.
- Thần thú: hiệu quả ở các mốc sao thấp (hiện chỉ có mốc 15★), cách nâng sao/bậc.
- Trang bị: toàn bộ.
- Icon Hạng Vũ.

## 5. Kiểm thử đã chạy (Playwright, Chromium headless)

- Viewport 390×844 và 1280×900: mở đủ 10 tab chính và 4 tab con Trợ trận.
  - Không có lỗi JS.
  - Không tràn ngang.
- Đổi đội so sánh trên radar; sửa mảnh Li Vẫn; đổi phẩm linh phù; lưu ghi chú Cổ Đế Viêm. Tải lại trang: dữ liệu còn nguyên.
- Mở hộp Sao lưu / Khôi phục.
- File offline (`file://`) cũng không có lỗi.

## 6. Quy tắc làm việc

1. Không suy đoán cơ chế game. Thiếu căn cứ thì ghi "chưa có dữ liệu" và hỏi người chơi.
2. Sửa trong `src/`, build, chạy kiểm thử trình duyệt rồi mới commit.
3. Phân biệt rõ "đã commit" và "đã kiểm thử".
