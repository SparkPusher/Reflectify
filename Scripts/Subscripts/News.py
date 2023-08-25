import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl, Qt

class BrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        self.browser = QWebView()
        self.browser.setUrl(QUrl("https://www.tagesschau.de/archiv/allemeldungen"))
        self.browser.setZoomFactor(0.7)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1570, 300, 350, 600)

        self.show()


app = QApplication(sys.argv)
window = BrowserApp()
sys.exit(app.exec_())
