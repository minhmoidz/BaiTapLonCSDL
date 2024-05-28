import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sqlite3


class BusStationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quản lý Bến xe bus')
        self.setWindowIcon(QIcon('ptit.png'))
        self.conn = sqlite3.connect('buss.db')
        self.cursor = self.conn.cursor()
        self.initUI()

    def initUI(self):
        # Khách hàng
        self.customer_layout = QVBoxLayout()
        self.customer_label = QLabel('Quản lý khách hàng:')
        self.customer_label.setAlignment(Qt.AlignCenter)
        self.customer_table = QTableWidget()
        self.customer_table.setColumnCount(3)
        self.customer_table.setHorizontalHeaderLabels(
            ['ID_KhachHang', 'Tên khách hàng', 'Địa chỉ'])
        self.customer_add_layout = QHBoxLayout()
        self.customer_name = QLineEdit()
        self.customer_phone = QLineEdit()
        self.customer_add_btn = QPushButton('Thêm')
        self.customer_delete_btn = QPushButton('Xóa')
        self.customer_search_btn = QPushButton('Tìm kiếm')
        self.customer_refresh_btn = QPushButton('Cập nhật')
        self.customer_add_layout.addWidget(self.customer_name)
        self.customer_add_layout.addWidget(self.customer_phone)
        self.customer_add_layout.addWidget(self.customer_add_btn)
        self.customer_add_layout.addWidget(self.customer_delete_btn)
        self.customer_add_layout.addWidget(self.customer_search_btn)
        self.customer_add_layout.addWidget(self.customer_refresh_btn)
        self.customer_layout.addWidget(self.customer_label)
        self.customer_layout.addWidget(self.customer_table)
        self.customer_layout.addLayout(self.customer_add_layout)

        # Chuyến đi
        self.trip_layout = QVBoxLayout()
        self.trip_label = QLabel('Quản lý chuyến đi:')
        self.trip_label.setAlignment(Qt.AlignCenter)
        self.trip_table = QTableWidget()
        self.trip_table.setColumnCount(5)
        self.trip_table.setHorizontalHeaderLabels(
            ['ID_ChuyenDi', 'ID_LichTrinh', 'ID_KhachHang', 'Ngày đi', 'Số lượng hành khách'])
        self.trip_add_layout = QHBoxLayout()
        self.trip_date = QLineEdit()
        self.trip_time = QLineEdit()
        self.trip_from = QLineEdit()
        self.trip_to = QLineEdit()
        self.trip_add_btn = QPushButton('Thêm')
        self.trip_delete_btn = QPushButton('Xóa')
        self.trip_search_btn = QPushButton('Tìm kiếm')
        self.trip_refresh_btn = QPushButton('Cập nhật')
        self.trip_add_layout.addWidget(self.trip_date)
        self.trip_add_layout.addWidget(self.trip_time)
        self.trip_add_layout.addWidget(self.trip_from)
        self.trip_add_layout.addWidget(self.trip_to)
        self.trip_add_layout.addWidget(self.trip_add_btn)
        self.trip_add_layout.addWidget(self.trip_delete_btn)
        self.trip_add_layout.addWidget(self.trip_search_btn)
        self.trip_add_layout.addWidget(self.trip_refresh_btn)
        self.trip_layout.addWidget(self.trip_label)
        self.trip_layout.addWidget(self.trip_table)
        self.trip_layout.addLayout(self.trip_add_layout)

        # Tài xế
        self.driver_layout = QVBoxLayout()
        self.driver_label = QLabel('Quản lý tài xế:')
        self.driver_label.setAlignment(Qt.AlignCenter)
        self.driver_table = QTableWidget()
        self.driver_table.setColumnCount(3)
        self.driver_table.setHorizontalHeaderLabels(
            ['ID_TaiXe', 'Tên tài xế', 'Ngày sinh'])
        self.driver_add_layout = QHBoxLayout()
        self.driver_name = QLineEdit()
        self.driver_phone = QLineEdit()
        self.driver_add_btn = QPushButton('Thêm')
        self.driver_delete_btn = QPushButton('Xóa')
        self.driver_search_btn = QPushButton('Tìm kiếm')
        self.driver_refresh_btn = QPushButton('Cập nhật')
        self.driver_add_layout.addWidget(self.driver_name)
        self.driver_add_layout.addWidget(self.driver_phone)
        self.driver_add_layout.addWidget(self.driver_add_btn)
        self.driver_add_layout.addWidget(self.driver_delete_btn)
        self.driver_add_layout.addWidget(self.driver_search_btn)
        self.driver_add_layout.addWidget(self.driver_refresh_btn)
        self.driver_layout.addWidget(self.driver_label)
        self.driver_layout.addWidget(self.driver_table)
        self.driver_layout.addLayout(self.driver_add_layout)

        # Sắp xếp giao diện chính
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.customer_layout)
        self.layout.addLayout(self.trip_layout)
        self.layout.addLayout(self.driver_layout)
        self.setLayout(self.layout)

        # Kết nối sự kiện
        self.customer_add_btn.clicked.connect(self.add_customer)
        self.customer_delete_btn.clicked.connect(self.delete_customer)
        self.customer_search_btn.clicked.connect(self.search_customer)
        self.customer_refresh_btn.clicked.connect(self.load_data)
        self.trip_add_btn.clicked.connect(self.add_trip)
        self.trip_delete_btn.clicked.connect(self.delete_trip)
        self.trip_search_btn.clicked.connect(self.search_driver)
        self.trip_refresh_btn.clicked.connect(self.load_data)
        self.driver_add_btn.clicked.connect(self.add_driver)
        self.driver_delete_btn.clicked.connect(self.delete_driver)
        self.driver_search_btn.clicked.connect(self.search_driver)
        self.driver_refresh_btn.clicked.connect(self.load_data)

        # Load dữ liệu ban đầu
        self.load_data()

        # Tùy chỉnh giao diện
        self.setStyleSheet("""
            QWidget {
                background-color: #ffb6c;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                font-weight: bold;
            }
            QPushButton {
                background-color: #ff7373;
                border: none;
                color: white;
                padding: 8px 16px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
                color: white;
            }
            QTableWidget {
                background-color: black;
                border: 1px solid #ddd;
                border-collapse: collapse;
            }
            QTableWidget th {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
            QTableWidget td {
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
        """)

    def load_data(self):
        # Load dữ liệu khách hàng
        self.customer_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM KhachHang")
        for row_index, row_data in enumerate(self.cursor.fetchall()):
            self.customer_table.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.customer_table.setItem(
                    row_index, col_index, QTableWidgetItem(str(col_data)))

        # Load dữ liệu chuyến đi
        self.trip_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM ChuyenDi")
        for row_index, row_data in enumerate(self.cursor.fetchall()):
            self.trip_table.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.trip_table.setItem(
                    row_index, col_index, QTableWidgetItem(str(col_data)))

        # Load dữ liệu tài xế
        self.driver_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM TaiXe")
        for row_index, row_data in enumerate(self.cursor.fetchall()):
            self.driver_table.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.driver_table.setItem(
                    row_index, col_index, QTableWidgetItem(str(col_data)))

    def create_button_animation(self, button):
        # Tạo hiệu ứng to nhỏ nhấp nháy liên tục cho nút button
        animation = QPropertyAnimation(button, b'size')
        animation.setDuration(300)
        animation.setStartValue(QRect(0, 0, button.width(), button.height()))
        animation.setEndValue(
            QRect(0, 0, button.width() * 1.1, button.height() * 1.1))
        animation.setLoopCount(-1)
        animation.setDirection(QPropertyAnimation.Backward)
        animation.start()

    def add_customer(self):
        customer_id, ok = QInputDialog.getInt(
            self, 'Thêm khách hàng', 'Nhập ID khách hàng:')
        if ok:
            customer_name, ok = QInputDialog.getText(
                self, 'Thêm khách hàng', 'Nhập tên khách hàng:')
            if ok and customer_name:
                customer_phone, ok = QInputDialog.getText(
                    self, 'Thêm khách hàng', 'Nhập số điện thoại khách hàng:')
                if ok and customer_phone:
                    customer_email, ok = QInputDialog.getText(
                        self, 'Thêm khách hàng', 'Nhập email khách hàng:')
                    if ok:
                        customer_address, ok = QInputDialog.getText(
                            self, 'Thêm khách hàng', 'Nhập địa chỉ khách hàng:')
                        if ok:
                            self.cursor.execute(
                                "INSERT INTO KhachHang (ID_KhachHang, Ten, SoDienThoai, Email, DiaChi) VALUES (?, ?, ?, ?, ?)",
                                (customer_id, customer_name, customer_phone,
                                 customer_email, customer_address)
                            )
                            self.conn.commit()
                            self.load_data()
                        else:
                            QMessageBox.warning(
                                self, 'Cảnh báo', 'Vui lòng nhập địa chỉ khách hàng!')
                    else:
                        QMessageBox.warning(
                            self, 'Cảnh báo', 'Vui lòng nhập email khách hàng!')
                else:
                    QMessageBox.warning(
                        self, 'Cảnh báo', 'Vui lòng nhập số điện thoại khách hàng!')
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Vui lòng nhập tên khách hàng!')

    def delete_customer(self):
        selected_row = self.customer_table.currentRow()
        if selected_row >= 0:
            customer_id = self.customer_table.item(selected_row, 0).text()
            self.cursor.execute(
                "SELECT COUNT(*) FROM ChuyenDi WHERE ID_KhachHang = ?", (customer_id,))
            trip_count = self.cursor.fetchone()[0]
            if trip_count == 0:
                self.cursor.execute(
                    "DELETE FROM KhachHang WHERE ID_KhachHang = ?", (customer_id,))
                self.conn.commit()
                self.load_data()
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Không thể xóa khách hàng này vì đã có chuyến đi!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng chọn một khách hàng để xóa!')

    def search_customer(self):
        customer_id, ok = QInputDialog.getInt(
            self, 'Tìm khách hàng', 'Nhập ID khách hàng:')
        if ok:
            self.cursor.execute(
                "SELECT Ten, SoDienThoai FROM KhachHang WHERE ID_KhachHang = ?", (customer_id,))
            customer_info = self.cursor.fetchone()
            if customer_info:
                customer_name, phone = customer_info
                self.cursor.execute(
                    "SELECT COUNT(*) FROM ChuyenDi WHERE ID_KhachHang = ?", (customer_id,))
                trip_count = self.cursor.fetchone()[0]
                self.cursor.execute(
                    "SELECT TaiXe.TenTaiXe FROM ChuyenDi INNER JOIN TaiXe ON ChuyenDi.ID_TaiXe = TaiXe.ID_TaiXe WHERE ChuyenDi.ID_KhachHang = ?", (customer_id,))
                driver_names = [row[0] for row in self.cursor.fetchall()]

                # Thêm truy vấn để lấy giá vé
                self.cursor.execute(
                    "SELECT GiaVe FROM GiaVe WHERE ID_GiaVe = ?", (customer_id,))
                ticket_prices = [row[0] for row in self.cursor.fetchall()]

                QMessageBox.information(
                    self, 'Thông tin', f"ID khách hàng: {customer_id}\nTên khách hàng: {customer_name}\nSố điện thoại: {phone}\nSố chuyến đi: {trip_count}\nTên tài xế: {', '.join(driver_names)}\nGiá vé: {', '.join(map(str, ticket_prices))}")
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Khách hàng không tồn tại!')

    def add_trip(self):
        trip_id, ok = QInputDialog.getInt(
            self, 'Thêm chuyến đi', 'Nhập ID chuyến đi:')
        if ok:
            schedule_id, ok = QInputDialog.getInt(
                self, 'Thêm chuyến đi', 'Nhập ID lịch trình:')
            if ok:
                customer_id, ok = QInputDialog.getInt(
                    self, 'Thêm chuyến đi', 'Nhập ID khách hàng:')
                if ok:
                    driver_id, ok = QInputDialog.getInt(
                        self, 'Thêm chuyến đi', 'Nhập ID tài xế:')
                    if ok:
                        date, ok = QInputDialog.getText(
                            self, 'Thêm chuyến đi', 'Nhập ngày đi (YYYY-MM-DD):')
                        if ok and date:
                            passenger_count, ok = QInputDialog.getInt(
                                self, 'Thêm chuyến đi', 'Nhập số lượng hành khách:')
                            if ok:
                                self.cursor.execute(
                                    "INSERT INTO ChuyenDi (ID_ChuyenDi, ID_LichTrinh, ID_KhachHang, ID_TaiXe, NgayDi, SoLuongHanhKhach) VALUES (?, ?, ?, ?, ?, ?)",
                                    (trip_id, schedule_id, customer_id,
                                     driver_id, date, passenger_count)
                                )
                                self.conn.commit()
                                self.load_data()
                            else:
                                QMessageBox.warning(
                                    self, 'Cảnh báo', 'Vui lòng nhập số lượng hành khách!')
                        else:
                            QMessageBox.warning(
                                self, 'Cảnh báo', 'Vui lòng nhập ngày đi!')
                    else:
                        QMessageBox.warning(
                            self, 'Cảnh báo', 'Vui lòng nhập ID tài xế!')
                else:
                    QMessageBox.warning(
                        self, 'Cảnh báo', 'Vui lòng nhập ID khách hàng!')
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Vui lòng nhập ID lịch trình!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng nhập ID chuyến đi!')

    def delete_trip(self):
        selected_row = self.trip_table.currentRow()
        if selected_row >= 0:
            trip_id = self.trip_table.item(selected_row, 0).text()
            self.cursor.execute(
                "SELECT NgayDi FROM ChuyenDi WHERE ID_ChuyenDi = ?", (trip_id,))
            trip_date = self.cursor.fetchone()[0]
            if trip_date > '2024-05-28':
                self.cursor.execute(
                    "DELETE FROM ChuyenDi WHERE ID_ChuyenDi = ?", (trip_id,))
                self.conn.commit()
                self.load_data()
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Không thể xóa chuyến đi đã diễn ra!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng chọn một chuyến đi để xóa!')

    def search_driver(self):
        search_text, ok = QInputDialog.getText(
            self, 'Tìm tài xế', 'Nhập ID hoặc tên tài xế:')
        if ok and search_text:
            try:
                driver_id = int(search_text)
                self.cursor.execute(
                    "SELECT TaiXe.ID_TaiXe, TaiXe.TenTaiXe, TaiXe.SoDienThoai, ChuyenDi.NgayDi, COUNT(ChuyenDi.ID_KhachHang) AS SoHanhKhach FROM TaiXe LEFT JOIN ChuyenDi ON TaiXe.ID_TaiXe = ChuyenDi.ID_TaiXe WHERE TaiXe.ID_TaiXe = ? GROUP BY TaiXe.ID_TaiXe", (driver_id,))
            except ValueError:
                driver_name = f"%{search_text}%"
                self.cursor.execute(
                    "SELECT TaiXe.ID_TaiXe, TaiXe.TenTaiXe, TaiXe.SoDienThoai, ChuyenDi.NgayDi, COUNT(ChuyenDi.ID_KhachHang) AS SoHanhKhach FROM TaiXe LEFT JOIN ChuyenDi ON TaiXe.ID_TaiXe = ChuyenDi.ID_TaiXe WHERE TaiXe.TenTaiXe LIKE ? GROUP BY TaiXe.ID_TaiXe", (driver_name,))

            drivers = self.cursor.fetchall()
            if drivers:
                results = "\n".join(
                    [f"ID: {driver[0]}, Tên: {driver[1]}, Số điện thoại: {driver[2]}, Ngày đi: {driver[3]}, Số hành khách: {driver[4]}" for driver in drivers])
                QMessageBox.information(self, 'Kết quả tìm kiếm', results)
            else:
                QMessageBox.warning(self, 'Cảnh báo', 'Không tìm thấy tài xế!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng nhập ID hoặc tên tài xế!')

    def add_driver(self):
        driver_id, ok = QInputDialog.getInt(
            self, 'Thêm tài xế', 'Nhập ID tài xế:')
        if ok:
            name, ok = QInputDialog.getText(
                self, 'Thêm tài xế', 'Nhập tên tài xế:')
            if ok and name:
                dob, ok = QInputDialog.getText(
                    self, 'Thêm tài xế', 'Nhập ngày sinh (YYYY-MM-DD):')
                if ok and dob:
                    gender, ok = QInputDialog.getText(
                        self, 'Thêm tài xế', 'Nhập giới tính:')
                    if ok and gender:
                        phone, ok = QInputDialog.getText(
                            self, 'Thêm tài xế', 'Nhập số điện thoại:')
                        if ok and phone:
                            self.cursor.execute(
                                "INSERT INTO TaiXe (ID_TaiXe, TenTaiXe, NgaySinh, GioiTinh, SoDienThoai) VALUES (?, ?, ?, ?, ?)",
                                (driver_id, name, dob, gender, phone)
                            )
                            self.conn.commit()
                            self.load_data()
                        else:
                            QMessageBox.warning(
                                self, 'Cảnh báo', 'Vui lòng nhập số điện thoại!')
                    else:
                        QMessageBox.warning(
                            self, 'Cảnh báo', 'Vui lòng nhập giới tính!')
                else:
                    QMessageBox.warning(
                        self, 'Cảnh báo', 'Vui lòng nhập ngày sinh!')
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Vui lòng nhập tên tài xế!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng nhập ID tài xế!')

    def delete_driver(self):
        selected_row = self.driver_table.currentRow()
        if selected_row >= 0:
            driver_id = self.driver_table.item(selected_row, 0).text()
            self.cursor.execute(
                "SELECT COUNT(*) FROM ChuyenDi WHERE ID_TaiXe = ?", (driver_id,))
            trip_count = self.cursor.fetchone()[0]
            if trip_count == 0:
                self.cursor.execute(
                    "DELETE FROM TaiXe WHERE ID_TaiXe = ?", (driver_id,))
                self.conn.commit()
                self.load_data()
            else:
                QMessageBox.warning(
                    self, 'Cảnh báo', 'Không thể xóa tài xế này vì đã có chuyến đi!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng chọn một tài xế để xóa!')

    def search_driver(self):
        search_text, ok = QInputDialog.getText(
            self, 'Tìm tài xế', 'Nhập ID hoặc tên tài xế:')
        if ok and search_text:
            try:
                driver_id = int(search_text)
                self.cursor.execute(
                    "SELECT TaiXe.ID_TaiXe, TaiXe.TenTaiXe, TaiXe.SoDienThoai, ChuyenDi.NgayDi, COUNT(ChuyenDi.ID_KhachHang) AS SoHanhKhach FROM TaiXe LEFT JOIN ChuyenDi ON TaiXe.ID_TaiXe = ChuyenDi.ID_TaiXe WHERE TaiXe.ID_TaiXe = ? GROUP BY TaiXe.ID_TaiXe", (driver_id,))
            except ValueError:
                driver_name = f"%{search_text}%"
                self.cursor.execute(
                    "SELECT TaiXe.ID_TaiXe, TaiXe.TenTaiXe, TaiXe.SoDienThoai, ChuyenDi.NgayDi, COUNT(ChuyenDi.ID_KhachHang) AS SoHanhKhach FROM TaiXe LEFT JOIN ChuyenDi ON TaiXe.ID_TaiXe = ChuyenDi.ID_TaiXe WHERE TaiXe.TenTaiXe LIKE ? GROUP BY TaiXe.ID_TaiXe", (driver_name,))

            drivers = self.cursor.fetchall()
            if drivers:
                results = "\n".join(
                    [f"ID: {driver[0]}, Tên: {driver[1]}, Số điện thoại: {driver[2]}, Ngày đi: {driver[3]}, Số hành khách: {driver[4]}" for driver in drivers])
                QMessageBox.information(self, 'Kết quả tìm kiếm', results)
            else:
                QMessageBox.warning(self, 'Cảnh báo', 'Không tìm thấy tài xế!')
        else:
            QMessageBox.warning(
                self, 'Cảnh báo', 'Vui lòng nhập ID hoặc tên tài xế!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BusStationApp()
    window.show()
    sys.exit(app.exec_())
