-- Tạo bảng Sự cố
CREATE TABLE SuCo (
    ID_SuCo INT PRIMARY KEY,
    MoTaSuCo NVARCHAR(255),
    NgayXayRa DATE,
    BienPhapKhacPhuc NVARCHAR(255)
);
-- Bảng Sự cố
INSERT INTO SuCo (ID_SuCo, MoTaSuCo, NgayXayRa, BienPhapKhacPhuc) VALUES
(1, 'Xe bị hỏng động cơ', '2024-01-01', 'Sửa chữa động cơ'),
(2, 'Tai nạn giao thông', '2024-01-05', 'Liên hệ bảo hiểm và sửa chữa xe'),
(3, 'Hết xăng giữa đường', '2024-01-10', 'Đổ xăng bổ sung'),
(4, 'Hệ thống phanh bị lỗi', '2024-01-15', 'Kiểm tra và thay thế phanh'),
(5, 'Cửa xe không mở được', '2024-01-20', 'Sửa chữa hệ thống cửa'),
(6, 'Máy lạnh không hoạt động', '2024-01-25', 'Sửa chữa máy lạnh'),
(7, 'Vỡ kính chắn gió', '2024-01-30', 'Thay kính chắn gió mới'),
(8, 'Đèn xe không sáng', '2024-02-01', 'Thay đèn mới'),
(9, 'Xe bị thủng lốp', '2024-02-05', 'Thay lốp mới'),
(10, 'Hệ thống điện gặp trục trặc', '2024-02-10', 'Kiểm tra và sửa chữa hệ thống điện'),
(11, 'Động cơ quá nhiệt', '2024-02-15', 'Kiểm tra hệ thống làm mát'),
(12, 'Ghế ngồi bị hỏng', '2024-02-20', 'Sửa chữa ghế ngồi'),
(13, 'Mất hệ thống âm thanh', '2024-02-25', 'Sửa chữa hệ thống âm thanh'),
(14, 'Hệ thống treo gặp vấn đề', '2024-03-01', 'Kiểm tra và sửa chữa hệ thống treo'),
(15, 'Sự cố phần mềm điều khiển', '2024-03-05', 'Cập nhật phần mềm mới'),
(16, 'Rò rỉ dầu nhớt', '2024-03-10', 'Kiểm tra và sửa chữa rò rỉ'),
(17, 'Mất chìa khóa xe', '2024-03-15', 'Cấp lại chìa khóa mới'),
(18, 'Sự cố hệ thống lái', '2024-03-20', 'Kiểm tra và sửa chữa hệ thống lái'),
(19, 'Tiếng ồn lạ từ động cơ', '2024-03-25', 'Kiểm tra và sửa chữa động cơ'),
(20, 'Khói đen từ ống xả', '2024-03-30', 'Kiểm tra và sửa chữa ống xả'),
(21, 'Kẹt cửa sổ', '2024-04-01', 'Sửa chữa cửa sổ'),
(22, 'Đèn báo lỗi động cơ sáng', '2024-04-05', 'Kiểm tra và sửa chữa động cơ'),
(23, 'Hệ thống cảnh báo không hoạt động', '2024-04-10', 'Sửa chữa hệ thống cảnh báo'),
(24, 'Không thể khởi động xe', '2024-04-15', 'Kiểm tra và sửa chữa hệ thống khởi động'),
(25, 'Đèn phanh không hoạt động', '2024-04-20', 'Thay đèn phanh mới'),
(26, 'Sự cố với bộ lọc gió', '2024-04-25', 'Thay bộ lọc gió mới'),
(27, 'Hệ thống chống bó cứng phanh (ABS) gặp lỗi', '2024-04-30', 'Kiểm tra và sửa chữa hệ thống ABS'),
(28, 'Xe bị ngập nước', '2024-05-01', 'Làm khô và kiểm tra toàn bộ xe'),
(29, 'Hệ thống điều hòa không khí không làm lạnh', '2024-05-05', 'Sửa chữa hệ thống điều hòa'),
(30, 'Cần gạt nước không hoạt động', '2024-05-10', 'Sửa chữa hoặc thay cần gạt nước mới');
SELECT * FROM SuCo;
