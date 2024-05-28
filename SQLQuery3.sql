-- Tạo bảng Xe bus
CREATE TABLE XeBus (
    ID_XeBus INT PRIMARY KEY,
    BienSoXe NVARCHAR(15),
    SoChoNgoi INT,
    LoaiXe NVARCHAR(50),
    TrangThaiHoatDong NVARCHAR(20)
);
-- Bảng Xe bus
INSERT INTO XeBus (ID_XeBus, BienSoXe, SoChoNgoi, LoaiXe, TrangThaiHoatDong) VALUES
(1, '29A-12345', 45, 'Xe 45 cho', 'Dang hoat dong'),
(2, '29B-23456', 30, 'Xe 30 cho', 'Dang bao tri'),
(3, '29C-34567', 40, 'Xe 40 cho', 'Dang hoat dong'),
(4, '29D-45678', 50, 'Xe 50 cho', 'Dang hoat dong'),
(5, '29E-56789', 35, 'Xe 35 cho', 'Dang bao tri'),
(6, '29F-67890', 25, 'Xe 25 cho', 'Dang hoat dong'),
(7, '29G-78901', 20, 'Xe 20 cho', 'Dang bao tri'),
(8, '29H-89012', 55, 'Xe 55 cho', 'Dang hoat dong'),
(9, '29K-90123', 60, 'Xe 60 cho', 'Dang hoat dong'),
(10, '29L-01234', 45, 'Xe 45 cho', 'Dang bao tri'),
(11, '29M-12345', 30, 'Xe 30 cho', 'Dang hoat dong'),
(12, '29N-23456', 40, 'Xe 40 cho', 'Dang bao tri'),
(13, '29P-34567', 50, 'Xe 50 cho', 'Dang hoat dong'),
(14, '29Q-45678', 35, 'Xe 35 cho', 'Dang hoat dong'),
(15, '29R-56789', 25, 'Xe 25 cho', 'Dang bao tri'),
(16, '29S-67890', 20, 'Xe 20 cho', 'Dang hoat dong'),
(17, '29T-78901', 55, 'Xe 55 cho', 'Dang bao tri'),
(18, '29U-89012', 60, 'Xe 60 cho', 'Dang hoat dong'),
(19, '29V-90123', 45, 'Xe 45 cho', 'Dang hoat dong'),
(20, '29X-01234', 30, 'Xe 30 cho', 'Dang bao tri'),
(21, '29Y-12345', 40, 'Xe 40 cho', 'Dang hoat dong'),
(22, '29Z-23456', 50, 'Xe 50 cho', 'Dang bao tri'),
(23, '30A-34567', 35, 'Xe 35 cho', 'Dang hoat dong'),
(24, '30B-45678', 25, 'Xe 25 cho', 'Dang bao tri'),
(25, '30C-56789', 20, 'Xe 20 cho', 'Dang hoat dong'),
(26, '30D-67890', 55, 'Xe 55 cho', 'Dang bao tri'),
(27, '30E-78901', 60, 'Xe 60 cho', 'Dang hoat dong'),
(28, '30F-89012', 45, 'Xe 45 cho', 'Dang hoat dong'),
(29, '30G-90123', 30, 'Xe 30 cho', 'Dang bao tri'),
(30, '30H-01234', 40, 'Xe 40 cho', 'Dang hoat dong');
SELECT * FROM XeBus;
SELECT BienSoXe FROM XeBus WHERE ID_XeBus = 3;

