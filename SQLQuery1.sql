CREATE TABLE KhachHang
(
    ID_KhachHang INTEGER PRIMARY KEY  ,
    Ten NVARCHAR(50),
    DiaChi NVARCHAR(100),
    Email NVARCHAR(50),
    SoDienThoai NVARCHAR(15)
);


INSERT INTO KhachHang
    (ID_KhachHang, Ten, DiaChi, Email, SoDienThoai)
VALUES
    (1, 'Nguyen Van A', '123 Le Loi', 'a@gmail.com', '0905123456'),
    (2, 'Le Thi B', '456 Tran Phu', 'b@gmail.com', '0905234567'),
    (3, 'Nguyen Thi Hong Phuc', '789 Nguyen Trai', 'hongphuc@gmail.com', '0905345678'),
    (4, 'Pham Tien Cong', '321 Le Loi', 'tiencong@gmail.com', '0905456789'),
    (5, 'Nguyen Tien Tuan', '654 Tran Phu', 'tientuan@gmail.com', '0905567890'),
    (6, 'Le Hai An', '987 Nguyen Trai', 'haian@gmail.com', '0905678901'),
    (7, 'Nguyen Viet Anh', '123 Tran Hung Dao', 'vietanh@gmail.com', '0905789012'),
    (8, 'Hoang Thi Hoa', '456 Le Duan', 'thihoa@gmail.com', '0905890123'),
    (9, 'Ta Dang Quan', '789 Phan Chu Trinh', 'dangquan@gmail.com', '0905901234'),
    (10, 'Dao Nhat Tan', '321 Tran Hung Dao', 'nhattan@gmail.com', '0905012345'),
    (11, 'Tran Ngoc Linh', '654 Le Duan', 'ngoclinh@gmail.com', '0905123456'),
    (12, 'Le Huu Chinh', '987 Phan Chu Trinh', 'huuchinh@gmail.com', '0905234567'),
    (13, 'Nguyen Thi Ha', '123 Dien Bien Phu', 'thiha@gmail.com', '0905345678'),
    (14, 'Vu Long Nhat', '456 Hoang Dieu', 'longnhat@gmail.com', '0905456789'),
    (15, 'Nguyen Thanh Dat', '789 Dien Bien Phu', 'thanhdat@gmail.com', '0905567890'),
    (16, 'Truong Quoc Khanh', '321 Hoang Dieu', 'quockhanh@gmail.com', '0905678901'),
    (17, 'Nguyen Viet Hung', '654 Le Hong Phong', 'viethung@gmail.com', '0905789012'),
    (18, 'Vu Thai Qui Long', '987 Ly Thuong Kiet', 'thailong@gmail.com', '0905890123'),
    (19, 'Tran Thanh Duy', '123 Le Hong Phong', 'thanhduy@gmail.com', '0905901234'),
    (20, 'Vu Tien Loc', '456 Ly Thuong Kiet', 'tienloc@gmail.com', '0905012345'),
    (21, 'Nguyen Van Quoc', '789 Nguyen Thi Minh Khai', 'vanquoc@gmail.com', '0905123456'),
    (22, 'Bui The Anh', '321 Nguyen Thi Minh Khai', 'theanh@gmail.com', '0905234567'),
    (23, 'Pham Sy Hiep', '654 Le Loi', 'syhiep@gmail.com', '0905345678'),
    (24, 'Nguyen Kha Phong', '987 Nguyen Trai', 'khaphong@gmail.com', '0905456789'),
    (25, 'Nguyen Thi Huyen Dieu', '123 Tran Phu', 'huyendieu@gmail.com', '0905567890'),
    (26, 'Do Trung Thong', '456 Nguyen Trai', 'trungthong@gmail.com', '0905678901'),
    (27, 'Luu Viet Hoang', '789 Le Loi', 'viethoang@gmail.com', '0905789012'),
    (28, 'Nguyen Hoang Anh', '321 Tran Phu', 'hoanganh@gmail.com', '0905890123'),
    (29, 'Luong Nhat Vu', '654 Tran Hung Dao', 'nhatvu@gmail.com', '0905901234'),
    (30, 'Hoang Manh Truong', '987 Le Duan', 'manhtruong@gmail.com', '0905012345');
SELECT *
FROM KhachHang;