-- Tạo bảng Tài xế
CREATE TABLE TaiXe
(
    ID_TaiXe INT PRIMARY KEY,
    TenTaiXe NVARCHAR(50),

    NgaySinh DATE,
    GioiTinh NVARCHAR(10),
    SoDienThoai NVARCHAR(15)
);
INSERT INTO TaiXe
    (ID_TaiXe, TenTaiXe, NgaySinh, GioiTinh, SoDienThoai)
VALUES
    (1, 'Nguyen Van Binh', '1980-01-01', 'Nam', '0906000001'),
    (2, 'Tran Thi Hoa', '1982-02-02', 'Nu', '0906000002'),
    (3, 'Le Van An', '1983-03-03', 'Nam', '0906000003'),
    (4, 'Pham Thi Lan', '1984-04-04', 'Nu', '0906000004'),
    (5, 'Vu Van Minh', '1985-05-05', 'Nam', '0906000005'),
    (6, 'Do Thi Thao', '1986-06-06', 'Nu', '0906000006'),
    (7, 'Hoang Van Kien', '1987-07-07', 'Nam', '0906000007'),
    (8, 'Bui Thi Thu', '1988-08-08', 'Nu', '0906000008'),
    (9, 'Nguyen Van Nam', '1989-09-09', 'Nam', '0906000009'),
    (10, 'Tran Thi Bich', '1990-10-10', 'Nu', '0906000010'),
    (11, 'Le Van Long', '1981-01-01', 'Nam', '0906000011'),
    (12, 'Pham Thi Tuyet', '1982-02-02', 'Nu', '0906000012'),
    (13, 'Vu Van Quoc', '1983-03-03', 'Nam', '0906000013'),
    (14, 'Do Thi Kim', '1984-04-04', 'Nu', '0906000014'),
    (15, 'Hoang Van Cuong', '1985-05-05', 'Nam', '0906000015'),
    (16, 'Bui Thi Mai', '1986-06-06', 'Nu', '0906000016'),
    (17, 'Nguyen Van Phu', '1987-07-07', 'Nam', '0906000017'),
    (18, 'Tran Thi Hang', '1988-08-08', 'Nu', '0906000018'),
    (19, 'Le Van Khoa', '1989-09-09', 'Nam', '0906000019'),
    (20, 'Pham Thi Hong', '1990-10-10', 'Nu', '0906000020'),
    (21, 'Vu Van Bao', '1981-11-11', 'Nam', '0906000021'),
    (22, 'Do Thi Hoa', '1982-12-12', 'Nu', '0906000022'),
    (23, 'Hoang Van Thai', '1983-01-01', 'Nam', '0906000023'),
    (24, 'Bui Thi Ngoc', '1984-02-02', 'Nu', '0906000024'),
    (25, 'Nguyen Van Son', '1985-03-03', 'Nam', '0906000025'),
    (26, 'Tran Thi Dao', '1986-04-04', 'Nu', '0906000026'),
    (27, 'Le Van Dung', '1987-05-05', 'Nam', '0906000027'),
    (28, 'Pham Thi Minh', '1988-06-06', 'Nu', '0906000028'),
    (29, 'Vu Van Tuan', '1989-07-07', 'Nam', '0906000029'),
    (30, 'Do Thi Lan', '1990-08-08', 'Nu', '0906000030');
SELECT *
FROM TaiXe;
