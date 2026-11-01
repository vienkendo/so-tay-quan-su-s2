# AGENTS.md: hướng dẫn cho AI agent làm việc trên repo này

Sổ Tay Quân Sư S2 là web app tĩnh hỗ trợ chơi game mobile **Tam Quốc Tứ Thời Ca** (server S234) cho một người chơi. App quản lý kho tướng, nâng sao, công pháp, thần thú, linh phù, chiến hồn; gợi ý đội hình; phân tích đối thủ.

- Bản chạy: GitHub Pages, https://vienkendo.github.io/so-tay-quan-su-s2/
- Đọc thêm: `README.md` (tính năng, cơ chế game đã xác nhận) và `HANDOFF.md` (lịch sử thay đổi, cấu trúc lưu trữ).

## 1. Giao tiếp với người dùng

- Luôn trả lời bằng **tiếng Việt**. Giữ nguyên tiếng Anh cho code identifiers, file names, commands, Git/GitHub terms.
- **Không** kết thúc câu bằng "ạ".
- Câu hỏi về cơ chế game, tính toán, đội hình phải **chính xác**.
  - Thiếu dữ liệu thì ghi "chưa có dữ liệu" và hỏi lại người chơi, không đoán.
  - Logic sai thì phản biện, không đồng ý cho qua.
- Người chơi gửi ảnh chụp màn hình game làm nguồn dữ liệu. Phải đếm sao, đọc số trên ảnh cẩn thận (crop hoặc zoom khi cần). Phân biệt rõ số liệu đọc được và số suy luận.

## 2. Nguồn sự thật và build

```
src/tpl_s2.html     template DUY NHẤT (HTML + CSS + JS, ~2.1k dòng)
src/data_s2.py      tướng đang dùng, đội mẫu, thứ tự nâng sao
src/heroes_base.py  kỹ năng gốc các tướng
src/enemy_db.py     phân loại vai trò mọi tướng (tags: carry, tank, heal, ctrl, aoe…)
src/*.json          icon tướng/sách, card art, kho mặc định
src/make.py         build
index.html, script.js, style.css   SINH TỰ ĐỘNG – không sửa tay
```

- Build: `python3 src/make.py .` (chạy trong thư mục repo). Lệnh này ghi `index.html`, `style.css?v=hash`, `script.js?v=hash` (cache-busting) và bản offline vào `build/`. Thư mục `build/` không commit.
- Placeholder trong template bị `make.py` thay thế: `/*__DATA__*/null`, `/*__ICONS__*/{}`, `/*__BOOKICONS__*/{}`, `/*__KHO__*/[]`, `/*__KORB__*/0`, `/*__KX__*/null`, `/*__HEROART__*/{}`, `/*__EDB__*/[]`.
- Ảnh:
  - `assets/images/heroes/*.jpg`: card art 240×480, map trong `src/hero_art.json`.
  - `assets/icons/books/*.jpg`: icon công pháp 96×96, map trong `src/book_icons.json`.
- **Bản web Claude (artifact) đang tạm ngưng.** Chỉ cập nhật GitHub Pages; không publish artifact trừ khi người chơi yêu cầu.

## 3. Quy trình bắt buộc

1. Sửa trong `src/`, chạy build.
2. Kiểm thử bằng Playwright (`playwright@1.56.1`, Chromium có sẵn ở `/opt/pw-browsers`), qua `python3 -m http.server 8766` ở gốc repo:
   - mở đủ các tab chính và tab con ở viewport 390×844 và 1280×900;
   - không có `pageerror` hay console error;
   - không tràn ngang (`scrollWidth` bằng chiều rộng viewport);
   - tính năng mới thì thử thao tác thật: nhập, lưu, tải lại trang, Hoàn tác;
   - sửa bộ tối ưu đội thì chạy `node tests/optimizer_test.js` (B&B so với brute force, xếp vị trí) – phải PASS hết.
3. Commit lên `main` rồi push.
4. Báo người chơi bằng tiếng Việt, phân biệt rõ "đã commit" và "đã kiểm thử".

## 4. Dữ liệu người chơi (quan trọng)

- **Kho thật không nằm trong repo này.** Nó ở `localStorage.kho2` của trình duyệt, đồng bộ qua repo riêng tư `vienkendo/so-tay-data` (`kho.json`) bằng token fine-grained.
  - Agent **không có quyền** vào repo đó.
  - **Không bao giờ** yêu cầu, nhận, ghi hay gửi token qua chat.
- `src/kho_default.json` chỉ là kho mặc định cho trình duyệt chưa có dữ liệu. Sửa file này **không** thay đổi kho thật của người chơi.
- Muốn cập nhật kho thật theo ảnh người chơi gửi: thêm một mục vào **`KPATCH`** trong `tpl_s2.html`.
  - Mỗi mục có `id` duy nhất, dạng `YYYY-MM-DD-<mô tả>`.
  - Các trường hỗ trợ:
    - `top: {tên: [sao các bản cao nhất]}`
    - `lv` (cấp chung) và `hlv: {tên: cấp}`, `clearHlv`
    - `books: [[tên, "Tím"|"Cam"|"Đỏ", sao]]`
    - `bdlv` (cấp Bảo Điển)
  - Patch chạy **một lần** mỗi kho (id lưu trong `X.patches`), ghi nhật ký và bấm Hoàn tác được.
  - Giá trị là tuyệt đối, nên chạy lại cũng không sai.
  - Không đụng vào phần người chơi nói sẽ tự chỉnh.
- Cấu trúc kho: `{k, log, undo, orb, m5, lv, atk, x}`.
  - `X` gồm: `battles`, `books`, `alloc`, `hlv`, `tt` (thần thú), `lp` (linh phù), `ch` (chiến hồn), `cdv`, `ev`, `teamOv`, `bdlv`, `patches`…
  - Đổi cấu trúc thì phải tương thích ngược với kho cũ.

## 5. Quy ước game đã xác nhận

- **Sao:** vàng 1–5★, đỏ 6–10★, cầu vồng 11–15★.
  - **Nhập Thánh lưu nối tiếp**: 16 = 1 lửa, 17 = 2 lửa…; hiển thị bằng lửa xanh lam.
  - `stars(s)` hiển thị "15★+NT2".
- **Chỉ SSR+ là tướng thật.**
  - SSR (cam) là nguyên liệu nâng sao.
  - Kỹ năng của SSR, SR, R chỉ dùng để phân tích đội địch.
  - Quy tắc và gợi ý đội chỉ xét SSR+.
- **Chi phí nâng sao:** bảng `RULE` trong template. Dữ liệu mới có tới 13→14★; 14→15★ và Nhập Thánh chưa có.
- **Công pháp:**
  - Số người đeo = sao sách + 1.
  - Bản trùng để lên sao: Tím 2/4/8/16/32; Cam/Đỏ 1/2/4/8/16.
  - Số ô công pháp theo sao tướng: `SLOTN`.
  - Sách Chung Vô Diệm chỉ tướng nữ đeo được (`FEMALE`, `BOOKFEM`).
- **Lực chiến:** 1 vạn = 10.000 (`parseLC` đọc được "69.3vạn", "290vạn6676", "8.48ức").
- **Trận:**
  - PVP ra đòn xen kẽ.
  - Đòn đơn thể đánh cùng làn dọc 1–4, 2–5, 3–6, ô trước trước.
  - Số hiệp tùy chế độ (thấy cả 5, 20, 30).
- **Đội người chơi:** xoay quanh **Lữ Bố** (carry đánh thường, mạnh theo Nộ, phải giữ **Công cao nhất đội**). Các buff "tướng Công cao nhất" của Vương Chiêu Quân, Quỷ Cốc Tử, Điêu Thuyền cần rơi vào Lữ Bố.

## 6. Nguyên tắc thuật toán

- Quy tắc và gợi ý phải **động**, suy từ Kho và kỹ năng; không gán cứng tên tướng vào logic, trừ các bảng dữ liệu như `BOOKPREF`.
- **Tối ưu đội** (`bestTeams`): branch & bound, kết quả phải khớp brute force; random có seed để kết quả cố định.
  - Đặc tính đã mở nặng ký hơn Tình Nghĩa.
  - Có 3 profile `bal`, `dmg`, `tough`, và đội lâu dài khi max sao (`lateGame`).
- **Kế hoạch** (`computePlan`): phân loại SSR+ thành giữ / dự bị / nguyên liệu (`KEEPSET`). Chỉ gợi ý nâng sao và chia sách cho tướng "giữ".
- **Phân sách** (`suggestBooks`): tướng theo thứ tự đội ở tab Kế hoạch, ưu tiên `BOOKPREF`, sau đó một lượt lấp ô trống theo vai trò.
- `EDB` là object `{tên: {name, phe, tags, desc}}`, không phải mảng.
