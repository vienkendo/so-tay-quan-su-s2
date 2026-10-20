# HANDOFF — Sổ Tay Quân Sư S2

> Tài liệu bàn giao trạng thái dự án cho agent tiếp theo. Cập nhật: 2026-10-20.
> Đây là ghi nhận tiến độ và các điểm cần kiểm chứng, không phải xác nhận mọi chức năng đã được kiểm thử trên trình duyệt.

## 1. Thông tin dự án

- Repository: `vienkendo/so-tay-quan-su-s2`
- Nhánh chính: `main`
- Ứng dụng: website HTML/CSS/JavaScript một file, `index.html`
- Website: https://vienkendo.github.io/so-tay-quan-su-s2/
- File nguồn: https://github.com/vienkendo/so-tay-quan-su-s2/blob/main/index.html
- Commit gần nhất đã xác minh khi tạo handoff: `e0ea9614cec5e509135dc1785446fe7629b2bc18`
- Blob SHA của `index.html`: `c0e9004a0520588ee4260199b0f64174493a02cb`
- Kích thước nội dung file đã đọc lại: 454,839 ký tự.
- Kiến trúc hiện tại: ứng dụng tập trung trong `index.html`, dữ liệu và logic phần lớn nằm trong JavaScript; trạng thái người dùng lưu trên trình duyệt.

## 2. Mục tiêu gần nhất

Người dùng yêu cầu rà soát việc số sao trong Kho tướng đã đồng bộ với các tab/trang khác chưa, sau đó yêu cầu sửa.

### Đã làm

Commit `e0ea9614cec5e509135dc1785446fe7629b2bc18` — `Sync hero stars across guide tabs`.

Đã đọc lại `index.html` từ `main` và xác nhận các thay đổi có trong file:
- `syncHeroes()` cập nhật sao/bản sở hữu từ dữ liệu kho.
- Khi tướng không còn bản trong kho, sao được đưa về giá trị nền `_baseSao` thay vì giữ số sao kho cũ.
- Đồng bộ lại phần bảng ô công pháp đội chính (`#slotplan`) theo sao hiện tại.
- Đồng bộ nhãn số sao/số ô và ô trống trong khu vực phân bổ công pháp (`#alloc`).
- Đội hình mẫu dùng sao và số ô từ dữ liệu tướng đang có khi tên tướng khớp trong `byName`; tướng không có trong danh sách chính thì vẫn dùng dữ liệu mẫu.
- Lộ trình nâng cấp và phần tính nâng sao mẫu đọc sao hiện tại từ `byName` khi có tướng tương ứng.

### Giới hạn đã thông báo cho người dùng

- Đã xác minh commit và đọc lại file trên GitHub.
- Chưa chạy kiểm thử tương tác trên trình duyệt sau commit.
- Các chỉ số như công, chi phí, một số thông tin công pháp, quy tắc/nguyên liệu và phân bổ gợi ý vẫn có dữ liệu cố định; commit này chủ yếu đồng bộ sao và các thông tin trực tiếp phụ thuộc số sao.
- Không được tuyên bố kiểm thử UI đã thành công nếu agent chưa thực sự chạy kiểm thử.

## 3. Bối cảnh thay đổi trước đó

Commit trước đó: `bd1b26af8a36dde8f9824a301bbfdd83d46e1a7e` — thêm thao tác trong từng thẻ tướng ở Kho:
- Nút sửa sao cho bản tướng, nhận số nguyên 1–20.
- Nút thêm nhanh bản trùng.
- Mặc định bản thêm nhanh: SSR+ 5 sao, SSR 4 sao (cần kiểm tra lại quy tắc này trước khi thay đổi; đây là mặc định tiện dụng, không nên mặc nhiên coi là chuẩn game).
- Lưu/sync/log thao tác theo logic hiện hữu của ứng dụng.

## 4. Quy tắc làm việc cho agent tiếp theo

1. Trước khi sửa, fetch `index.html` trên `main` để lấy blob SHA mới nhất. Không dùng SHA ghi trong tài liệu này nếu repo đã có commit mới hơn.
2. Đọc đúng khu vực liên quan trong file trước khi chỉnh sửa. Đây là file lớn và có nhiều logic phụ thuộc lẫn nhau.
3. Thực hiện thay đổi tối thiểu, tránh ghi đè các thay đổi mới của người dùng/agent khác.
4. Khi gọi cập nhật file GitHub, dùng SHA vừa fetch; sau đó fetch lại để xác minh nội dung và commit.
5. Phân biệt rõ: “đã commit/đọc lại” khác với “đã chạy kiểm thử”.
6. Không thay đổi dữ liệu đội hình, sao nền, chi phí, quy tắc game hoặc phân bổ công pháp chỉ dựa trên suy đoán. Nếu thiếu căn cứ, ghi rõ là dữ liệu tham khảo hoặc hỏi người dùng.
7. Giữ giao diện, ngôn ngữ và quy ước hiện hữu trừ khi yêu cầu có nêu khác.

## 5. Việc còn tồn đọng / đề xuất thứ tự

### P0 — Kiểm thử hồi quy trên trình duyệt
- Mở website và kiểm tra lỗi JavaScript/console.
- Sửa sao trong Kho; kiểm tra danh sách tướng, chi tiết tướng, đội hình chính, bảng công pháp, lộ trình nâng cấp và đội hình mẫu.
- Thêm bản trùng; kiểm tra số bản và sao được hiển thị.
- Xóa bản cuối cùng của một tướng; kiểm tra sao quay về giá trị nền, không giữ sao cũ.
- Tải lại trang; xác nhận dữ liệu kho vẫn được lưu.
- Kiểm tra cả tướng có trong `H` và tướng chỉ có trong dữ liệu đội hình mẫu.

### P1 — Kiểm tra luồng đồng bộ
- Xác minh tất cả thao tác sửa sao/thêm/xóa bản đều gọi đúng luồng lưu và `syncHeroes()`.
- Kiểm tra thứ tự khởi tạo dữ liệu: giá trị nền `_baseSao` phải được thiết lập sau khi áp dụng `CURRENT_STARS` và trước khi đồng bộ kho.
- Kiểm tra cập nhật `#slotplan` bằng thứ tự hàng có còn khớp với danh sách `core` hay không; nếu cấu trúc bảng thay đổi, nên tìm hàng theo tên tướng thay vì dựa vào chỉ số hàng.
- Kiểm tra khu vực `#alloc` khi số ô cần thiết ít hơn số công pháp đã khai báo; hiện tại logic bổ sung ô trống không tự loại công pháp đang có.

### P2 — Nguồn dữ liệu và logic nghiệp vụ
- Tách rõ dữ liệu “thực tế trong kho” khỏi dữ liệu “gợi ý/tĩnh” (công, chi phí, nguyên liệu, sách gợi ý).
- Rà soát các tướng không có trong `DATA.heroes` nhưng xuất hiện trong đội hình mẫu.
- Xác minh quy tắc sao tối đa, mốc mở ô, nguyên liệu và chi phí bằng nguồn game/tài liệu do người dùng cung cấp trước khi tự động hóa.
- Cân nhắc thêm phiên bản/schema cho dữ liệu localStorage và cách sao lưu/khôi phục trước các thay đổi cấu trúc lớn.

## 6. Khu vực và tên định danh đáng chú ý

Các tên định danh được xác nhận trong phiên sửa gần nhất:
- `H`, `byName`, `CURRENT_STARS`
- `syncHeroes()`
- `renderGrid()`, `renderTeam()`, `renderUp()`
- `#slotplan`, `#alloc`
- `renderSampleTeam(sampleTeamMode)`, `renderSampleUpgrade()`
- `SAMPLE_HERO_STATS`, `DATA.teams`, `DATA.alloc`

Agent phải kiểm tra tên/logic hiện tại trong file trước khi dùng vì các định danh có thể thay đổi theo commit mới.

## 7. Nhật ký commit liên quan

| Commit | Nội dung | Trạng thái xác minh |
|---|---|---|
| `bd1b26af8a36dde8f9824a301bbfdd83d46e1a7e` | Thêm sửa sao và thêm nhanh bản trùng trong Kho tướng | Đã được ghi nhận từ tiến độ trước; kiểm tra lại lịch sử repo nếu cần |
| `e0ea9614cec5e509135dc1785446fe7629b2bc18` | Đồng bộ sao với các khu vực/tab liên quan | Đã fetch lại `index.html` và xác nhận nội dung |

## 8. Cách báo cáo tiến độ

Mỗi lần làm việc, agent nên ghi:
- **Đã kiểm tra:** file/logic/luồng nào, SHA nào.
- **Đã thay đổi:** hành vi cụ thể và lý do.
- **Bằng chứng:** commit SHA, blob SHA, kết quả fetch lại.
- **Đã kiểm thử:** môi trường, các bước đã chạy, kết quả thực tế.
- **Chưa kiểm chứng / rủi ro:** ghi rõ, không suy diễn thành đã hoàn tất.

## 9. Trạng thái tổng kết

**Đã cập nhật mã nguồn và xác minh nội dung trên GitHub. Chưa có bằng chứng kiểm thử trình duyệt cho commit đồng bộ sao. Ưu tiên tiếp theo là kiểm thử hồi quy, sau đó mới mở rộng đồng bộ sang dữ liệu nghiệp vụ khác.**
