import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl, Qt

class BrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        self.browser = QWebView()
        self.browser.setUrl(QUrl("https://soundcloud.com/ammowitsch/sets/ruhig-und-so"))
        self.browser.setZoomFactor(0.5)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1420, 480, 510, 300)

        self.show()


app = QApplication(sys.argv)
window = BrowserApp()
sys.exit(app.exec_())
