# Chính sách bảo mật (Security Policy)

## Phạm vi

Sổ Tay Quân Sư S2 là **web tĩnh** chạy trên GitHub Pages: HTML, CSS và JavaScript, không có backend, không có tài khoản người dùng. Trang không tải script, font hay CDN từ bên ngoài.

Kết nối mạng duy nhất là tới **GitHub REST API** (`https://api.github.com/repos/...`), và chỉ khi người dùng bật **Kho → Đồng bộ GitHub**.

| Thành phần | Có hỗ trợ bảo mật |
|---|---|
| Nhánh `main` (bản đang chạy trên GitHub Pages) | ✅ |
| Bản offline 1 file sinh từ `src/make.py` | ✅ (cùng mã nguồn) |
| Bản web Claude (artifact) | ⏸ tạm ngưng, không cập nhật |
| Commit và nhánh cũ | ❌ |

## Dữ liệu và token

- **Kho tướng** (tướng, sao, công pháp, nhật ký trận…) lưu trong `localStorage` của trình duyệt. Khi bật đồng bộ, Kho được lưu thêm vào file `kho.json` của một **repo riêng tư do chính người chơi sở hữu** (mặc định `so-tay-data`).
- **GitHub token:**
  - Dùng **fine-grained personal access token**. Chỉ chọn đúng repo dữ liệu (*Only select repositories*), chỉ cấp quyền **Contents: Read and write**. Không cấp quyền nào khác, không dùng classic token.
  - Token chỉ lưu trong `localStorage.ghsync` của từng máy và chỉ gửi tới `api.github.com`. Trang không ghi token vào Kho, vào `kho.json` hay vào file sao lưu.
  - **Không gửi token qua chat**, kể cả Zalo, Messenger hay chat với AI. Để chuyển sang máy khác, dùng nút *Sao chép token* rồi dán trực tiếp.
  - Nghi lộ token: vào GitHub → Settings → Developer settings → Fine-grained tokens, bấm **Revoke** (hoặc Regenerate), rồi nhập token mới trên từng máy.
  - Nên đặt hạn dùng cho token, ví dụ 90 ngày.
- Repo mã nguồn này **không chứa** token hay dữ liệu Kho thật. `src/kho_default.json` chỉ là kho mẫu ban đầu.
- Máy dùng chung với người khác: bấm **Ngắt đồng bộ trên máy này** để xóa token khỏi trình duyệt.

## Nguyên tắc cho người đóng góp (và AI agent)

- Không commit token, mật khẩu, khóa API hay dữ liệu cá nhân. Không thêm token vào mã, log hay URL.
- Mọi dữ liệu do người dùng nhập (tên tướng, ghi chú, nội dung `kho.json` tải về…) phải đi qua `esc()` trước khi đưa vào `innerHTML`.
- Không thêm script, font hay CDN bên ngoài. Không gửi dữ liệu tới bất kỳ máy chủ nào khác ngoài `api.github.com`.
- Không mở rộng quyền token mà trang yêu cầu ngoài *Contents: Read and write*.
- Đọc `AGENTS.md` trước khi sửa mã.

## Báo cáo lỗ hổng

Nếu phát hiện lỗ hổng, ví dụ XSS qua dữ liệu Kho, lộ token hay ghi đè dữ liệu đồng bộ:

1. **Không** mở issue công khai mô tả chi tiết cách khai thác.
2. Gửi báo cáo riêng qua **GitHub → tab Security → Report a vulnerability** (Private vulnerability reporting) của repo này. Nếu tính năng này chưa bật, liên hệ riêng chủ repo `@vienkendo` qua GitHub.
3. Báo cáo nên có:
   - mô tả lỗi;
   - các bước tái hiện;
   - trình duyệt và thiết bị;
   - mức ảnh hưởng (lộ token, mất hoặc sai dữ liệu Kho…).

Đây là dự án cá nhân nên không có cam kết thời gian xử lý cố định. Lỗi liên quan đến token hoặc dữ liệu được ưu tiên sửa trước. Sau khi bản sửa lên `main`, báo cáo sẽ được công khai nếu phù hợp.
