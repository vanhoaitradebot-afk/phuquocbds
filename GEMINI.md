# HỒ SƠ BÀN GIAO CHO AI (ANTIGRAVITY) KHI CHUYỂN SANG THIẾT BỊ MỚI

> File `GEMINI.md` này giúp Antigravity trên máy tính mới tự động đọc và nhớ toàn bộ ngữ cảnh, mật khẩu máy chủ, cấu trúc code và quy trình đăng bài của dự án **PhuquocBDS.com**.

## 1. Thông tin Chủ sở hữu & Dự án
- **Thương hiệu:** PhuquocBDS.com — Chuyên trang Bất động sản Phú Quốc (Thổ cư, Hàng ngộp, Dòng tiền, Quy hoạch 2040).
- **Chủ sở hữu:** Lê Văn Hoài
- **Hotline / Zalo:** `079.228.1999` (`https://zalo.me/0792281999`)
- **Kho lưu trữ GitHub (Repository):** `https://github.com/vanhoaitradebot-afk/phuquocbds`
- **Link web đang chạy thực tế (Production):** https://phuquocbds.surge.sh
- **Mục tiêu tên miền chính thức:** `phuquocbds.com` (Chiến lược chi tiết nằm trong file `nhat_ky_tu_van_seo_phuquocbds.md`).

## 2. Vai trò của Antigravity (Cam kết với người dùng)
- Bạn là **người phụ trách kỹ thuật, đăng tin BĐS và viết bài SEO tự động** cho anh Lê Văn Hoài.
- Mỗi khi người dùng gửi:
  1. Hình ảnh thực tế / sổ đỏ,
  2. Link video TikTok (nếu có),
  3. Giá bán, diện tích, khu vực, pháp lý, mô tả...
  -> Bạn sẽ biên tập chuẩn đẹp, cập nhật vào mảng `propertiesData` trong `index.html` (nén ảnh sang base64 hoặc `.webp` nhẹ), và chạy lệnh đẩy thẳng lên máy chủ `https://phuquocbds.surge.sh` (hoặc GitHub) ngay lập tức.

## 3. Thông tin Đăng nhập & Lệnh Đẩy Web (Deploy 1 chạm)
Trang web đang được host miễn phí trên **Surge CDN** với tài khoản đã xác thực sẵn (không cần đăng nhập lại trên máy mới):
- `SURGE_LOGIN`: `phuquocbds4878@fldubai.com`
- `SURGE_TOKEN`: `2ba1fad35a72227eb6fe2dae2afdac00`
- `Domain`: `phuquocbds.surge.sh`

### Lệnh PowerShell để đẩy web lên mạng ngay lập tức:
```powershell
$env:SURGE_LOGIN = "phuquocbds4878@fldubai.com"
$env:SURGE_TOKEN = "2ba1fad35a72227eb6fe2dae2afdac00"
npx.cmd surge . phuquocbds.surge.sh
```
*(Hoặc chạy trực tiếp file `./deploy.ps1` / `CHAY_CAP_NHAT_WEB.bat` trong thư mục này).*

## 4. Các tính năng đã hoàn thiện trong `index.html`
1. **Menu Header Chuẩn Responsive:** 3 khối tách biệt (Logo, Menu giữa `hidden lg:flex`, Cụm nút phải `whitespace-nowrap flex-shrink-0`), không bị rớt chữ hay đè nút Trái tim khi thu nhỏ màn hình.
2. **Hai nút nổi Zalo & Gọi điện (`079.228.1999`):** Nằm góc dưới bên trái (`fixed bottom-6 left-6`), cả 2 nút đều có hiệu ứng nhún nhảy (`animate-bounce`) thu hút khách hàng.
3. **Cửa sổ Đăng tin rao bán BĐS (`#postModal`):**
   - Hỗ trợ chọn nhiều ảnh từ máy tính/điện thoại (`#postImageInput`), tự động nén qua `<canvas>` (`compressImageFile`) và hiển thị lưới xem trước (`#postImagePreviewGrid`).
   - Hỗ trợ dán **Link Video TikTok** (`#postTiktokUrl`) kèm nút `▶ Xem thử`.
   - Lưu tin vào `localStorage` (`bpq_custom_listings`) và hiển thị bộ sưu tập nhiều ảnh trong cửa sổ chi tiết (`openDetailModal`).
4. **Cửa sổ Xem nhanh Video TikTok (`#tiktokQuickModal`):**
   - Phát trực tiếp video TikTok ngay trên web (`openTiktokQuickModal`) qua `https://www.tiktok.com/embed/v2/{videoId}` hoặc tự động giải mã link rút gọn qua `oembed`.
5. **Bản đồ Tra cứu Quy hoạch Phú Quốc trực tuyến (`#valuationModal`):**
   - Tích hợp 4 lớp bản đồ tương tác: Quy hoạch chung 2040 (QĐ 150/QĐ-TTg), Quy hoạch sử dụng đất 2030, Kế hoạch sử dụng đất mới nhất, Phân khu An Thới, kèm công cụ Thẩm định giá nhanh.
6. **Bảng tính lãi vay ngân hàng (`updateSidebarMortgage`):**
   - Tự động tính và cập nhật trực tiếp cả số tổng trả tháng đầu và dòng chi tiết `Gốc + Lãi tháng đầu` khi kéo thanh trượt.
