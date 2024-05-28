-- Tạo bảng Tuyến đường
CREATE TABLE TuyenDuong (
    ID_TuyenDuong INT PRIMARY KEY,
    TenTuyenDuong NVARCHAR(50)
);

INSERT INTO TuyenDuong (ID_TuyenDuong, TenTuyenDuong) VALUES
(1, 'Tuyen 1: Hoan Kiem - Ba Dinh'),
(2, 'Tuyen 2: Hai Ba Trung - Dong Da'),
(3, 'Tuyen 3: Hoang Mai - Cau Giay'),
(4, 'Tuyen 4: Thanh Xuan - Tay Ho'),
(5, 'Tuyen 5: Bac Tu Liem - Nam Tu Liem'),
(6, 'Tuyen 6: Long Bien - Hoang Mai'),
(7, 'Tuyen 7: Gia Lam - Dong Anh'),
(8, 'Tuyen 8: Thanh Tri - Soc Son'),
(9, 'Tuyen 9: Me Linh - Son Tay'),
(10, 'Tuyen 10: Ba Vi - Phuc Tho'),
(11, 'Tuyen 11: Dan Phuong - Hoai Duc'),
(12, 'Tuyen 12: Thach That - Quoc Oai'),
(13, 'Tuyen 13: Chuong My - Thanh Oai'),
(14, 'Tuyen 14: Thuong Tin - Phu Xuyen'),
(15, 'Tuyen 15: Ung Hoa - My Duc'),
(16, 'Tuyen 16: Hoan Kiem - Gia Lam'),
(17, 'Tuyen 17: Ba Dinh - Dong Anh'),
(18, 'Tuyen 18: Hai Ba Trung - Soc Son'),
(19, 'Tuyen 19: Dong Da - Me Linh'),
(20, 'Tuyen 20: Hoang Mai - Son Tay'),
(21, 'Tuyen 21: Cau Giay - Ba Vi'),
(22, 'Tuyen 22: Tay Ho - Phuc Tho'),
(23, 'Tuyen 23: Bac Tu Liem - Hoai Duc'),
(24, 'Tuyen 24: Nam Tu Liem - Quoc Oai'),
(25, 'Tuyen 25: Long Bien - Chuong My'),
(26, 'Tuyen 26: Gia Lam - Thanh Oai'),
(27, 'Tuyen 27: Thanh Tri - Phu Xuyen'),
(28, 'Tuyen 28: Soc Son - My Duc'),
(29, 'Tuyen 29: Hoan Kiem - Dong Da'),
(30, 'Tuyen 30: Ba Dinh - Cau Giay');
SELECT * FROM TuyenDuong;
SELECT TenTuyenDuong FROM TuyenDuong WHERE ID_TuyenDuong = 1;
SELECT COUNT(*) AS SoLuongTuyenDuong FROM TuyenDuong;
