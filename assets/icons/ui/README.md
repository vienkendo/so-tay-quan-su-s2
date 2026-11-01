# Biểu tượng giao diện (assets/icons/ui)

Web dùng các biểu tượng này trong giao diện chi tiết tướng. File nào chưa có thì web tự dùng bản vẽ HTML dự phòng.

## Cách thêm
1. Đặt file PNG nền trong suốt vào thư mục này, **đúng tên file** trong bảng.
2. Thêm dòng tương ứng vào `src/ui_icons.json`, ví dụ `"phe-3q": "assets/icons/ui/phe-3q.png"`.
3. Chạy `python3 src/make.py .` rồi commit.

## Danh sách (PNG, nền trong suốt)

| Khóa / tên file | Kích thước | Mô tả |
|---|---|---|
| `phe-3q.png` | 128×128 | Huy hiệu hình thoi phe Tam Quốc, chữ "3Q", nền xanh dương |
| `phe-han.png` | 128×128 | Hình thoi phe Hán, nền xanh lá |
| `phe-tan.png` | 128×128 | Hình thoi phe Tần, nền vàng cam |
| `phe-duong.png` | 128×128 | Hình thoi phe Đường, nền tím |
| `phe-co-de.png` | 128×128 | Hình thoi phe Cổ Đế, nền xanh ngọc |
| `nhom-tan-cong.png` | 128×128 | Hình thoi nhóm Công (biểu tượng kiếm), nền đỏ |
| `nhom-do-don.png` | 128×128 | Hình thoi nhóm Thủ (khiên) |
| `nhom-bo-tro.png` | 128×128 | Hình thoi nhóm Trợ (chữ thập hồi máu) |
| `nhom-thuat-si.png` | 128×128 | Hình thoi nhóm Thuật Sĩ (cuộn sách/bùa) |
| `nt-flame.png` | 64×64 | Ngọn lửa xanh lam–tím (mốc Nhập Thánh) |
| `st-cap.png` | 64×64 | Biểu tượng chỉ số Cấp (chữ "Lv") |
| `st-hp.png` | 64×64 | Biểu tượng HP (trái tim xanh lá) |
| `st-cong.png` | 64×64 | Biểu tượng Công (nắm đấm/kiếm cam) |
| `st-thu.png` | 64×64 | Biểu tượng Thủ (khiên xanh) |
| `sk-danh-thuong.png` | 192×192 | Nút tròn kỹ năng Đánh Thường (đường chém đỏ hồng) |
| `sk-tuyet-chieu.png` | 192×192 | Nút tròn Tuyệt Chiêu (vụ nổ năng lượng) |
| `sk-tiem-nang.png` | 192×192 | Nút tròn Tiềm Năng (vũ khí/biểu tượng đặc tính) |
| `btn-cong-phap.png` | 96×96 | Nút Công Pháp (cuộn sách) |
| `btn-tuyet-ky.png` | 96×96 | Nút Tuyệt Kỹ (ngọn lửa/ấn) |
| `btn-thuoc-tinh.png` | 96×96 | Nút Thuộc Tính (bảng chỉ số) |

## Prompt gợi ý cho ChatGPT
> Vẽ bộ icon game mobile phong cách Tam Quốc anime (viền vàng kim, đổ bóng nhẹ, nền trong suốt PNG) gồm: [liệt kê từ bảng trên]. Mỗi icon một file riêng, đúng kích thước, nhìn rõ ở cỡ nhỏ. Thiết kế mới, không sao chép icon của game có sẵn.
