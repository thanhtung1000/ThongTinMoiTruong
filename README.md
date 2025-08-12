Bài làm này là một ứng dụng web đơn giản nhằm phục vụ mục tiêu thống kê và phân tích dữ liệu môi trường theo thời gian thực. Ý tưởng xuất phát từ nhu cầu theo dõi các chỉ số môi trường như nhiệt độ, độ ẩm, tốc độ gió và áp suất tại các trạm quan trắc khác nhau. Thông qua việc thu thập và xử lý dữ liệu, người dùng có thể đánh giá tình hình môi trường tại từng khu vực trong một khoảng thời gian cụ thể.

Ứng dụng được chia thành hai phần chính. Phần đầu tiên (App 1) có nhiệm vụ gửi dữ liệu môi trường lên cơ sở dữ liệu Firebase Firestore. Dữ liệu này có thể được lấy từ thiết bị IoT hoặc được mô phỏng thủ công để phục vụ mục đích thử nghiệm. Phần thứ hai (App 2) là giao diện web cho phép người dùng xem toàn bộ dữ liệu đã thu thập, lọc theo tên trạm và khoảng thời gian, đồng thời hiển thị các thống kê cơ bản như nhiệt độ trung bình, độ ẩm cao nhất và số lượng bản ghi phù hợp.

Về mặt công nghệ, ứng dụng sử dụng HTML, CSS và JavaScript để xây dựng giao diện và xử lý logic phía người dùng. Bootstrap 5 được tích hợp để tạo giao diện hiện đại, dễ sử dụng và tương thích với nhiều thiết bị. Firebase Firestore đóng vai trò là nền tảng lưu trữ dữ liệu thời gian thực, giúp việc truy xuất và cập nhật dữ liệu diễn ra nhanh chóng và hiệu quả.

Một số thuật toán đơn giản được áp dụng trong quá trình xử lý dữ liệu, bao gồm lọc dữ liệu theo điều kiện, tính trung bình cộng, tìm giá trị lớn nhất và xử lý thời gian bằng đối tượng Date trong JavaScript. Giao diện của App 2 được thiết kế trực quan, bao gồm biểu mẫu nhập liệu để lọc dữ liệu, bảng hiển thị thông tin chi tiết và khu vực thống kê kết quả.

Thông qua bài làm này, người thực hiện đã có cơ hội tiếp cận và làm quen với cách kết nối cơ sở dữ liệu Firebase, xử lý dữ liệu thời gian thực, xây dựng giao diện web có tính tương tác và áp dụng các kiến thức về lập trình web vào một bài toán thực tế. Đây là một bước khởi đầu hữu ích cho các ứng dụng giám sát môi trường quy mô lớn hơn trong tương lai.

<img width="964" height="682" alt="image" src="https://github.com/user-attachments/assets/0bc85da0-b1cf-4070-b0d1-ab47e08ecbeb" />
<img width="1228" height="582" alt="image" src="https://github.com/user-attachments/assets/e3131a5c-b1fa-49e9-8311-3dc49b37ca0b" />
<img width="1344" height="732" alt="image" src="https://github.com/user-attachments/assets/7abb6905-8f3c-4810-ad99-04b4df417e86" />
