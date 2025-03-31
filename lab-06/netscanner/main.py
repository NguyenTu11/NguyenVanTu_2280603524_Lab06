import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_main_window import Ui_MainWindow
from network_scanner import local_network_scan as scan  # Sửa import

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối nút Scan với phương thức scan_network
        self.ui.scanButton.clicked.connect(self.scan_network)

    def scan_network(self):
        # Lấy phạm vi IP từ ô nhập liệu
        ip_range = self.ui.ipRangeInput.text()

        if not ip_range:
            self.ui.resultsTable.setRowCount(0)
            return

        # Thực hiện quét mạng
        devices = scan(ip_range)

        # Hiển thị kết quả trong bảng
        self.ui.resultsTable.setRowCount(len(devices))
        for row, device in enumerate(devices):
            self.ui.resultsTable.setItem(row, 0, QTableWidgetItem(device["ip"]))
            self.ui.resultsTable.setItem(row, 1, QTableWidgetItem(device["mac"]))
            self.ui.resultsTable.setItem(row, 2, QTableWidgetItem(device["vendor"]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())