-- Tạo bảng Giá vé
CREATE TABLE GiaVe (
    ID_GiaVe INT PRIMARY KEY,
    ID_TuyenDuong INT,
    GiaVe DECIMAL(10, 2),
    FOREIGN KEY (ID_TuyenDuong) REFERENCES TuyenDuong(ID_TuyenDuong)
);
-- Bảng Giá vé
INSERT INTO GiaVe (ID_GiaVe, ID_TuyenDuong, GiaVe) VALUES
(1, 1, 7000),
(2, 2, 8000),
(3, 3, 9000),
(4, 4, 10000),
(5, 5, 11000),
(6, 6, 12000),
(7, 7, 13000),
(8, 8, 14000),
(9, 9, 15000),
(10, 10, 16000),
(11, 11, 17000),
(12, 12, 18000),
(13, 13, 19000),
(14, 14, 20000),
(15, 15, 21000),
(16, 16, 22000),
(17, 17, 23000),
(18, 18, 24000),
(19, 19, 25000),
(20, 20, 26000),
(21, 21, 27000),
(22, 22, 28000),
(23, 23, 29000),
(24, 24, 30000),
(25, 25, 31000),
(26, 26, 32000),
(27, 27, 33000),
(28, 28, 34000),
(29, 29, 35000),
(30, 30, 36000);
SELECT * FROM GiaVe;