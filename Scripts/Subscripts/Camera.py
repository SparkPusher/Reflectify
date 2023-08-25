import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt
import picamera
import picamera.array
from datetime import datetime

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(1270,300)
        
        # UI-Elemente
        self.image_label = QLabel(self)
        layout = QVBoxLayout()
        
        self.capture_button = QPushButton('Take Photo', self)
        self.capture_button.setStyleSheet("QPushButton { color: white; border: 2px solid white; }")
        self.capture_button.clicked.connect(self.capture_image)

        layout.addWidget(self.image_label)
        layout.addWidget(self.capture_button)
        self.setLayout(layout)

        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24
        self.raw_capture = picamera.array.PiRGBArray(self.camera, size=(640, 480))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(int(1000./24))
        
        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_value = 0

    def update_frame(self):
        self.camera.capture(self.raw_capture, format="rgb", use_video_port=True)
        image = self.raw_capture.array

        q_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_img))

        self.raw_capture.truncate(0)

    def capture_image(self):
        # Startet den Countdown, bevor das Bild aufgenommen wird
        self.start_countdown()

    def capture_image_now(self):
        now = datetime.now()
        date = now.strftime("%d%m%Y")
        time = now.strftime("%H%M%S")
        file = str(date) + str("_") + str(time) + str(".jpg")
        filename = "/home/julian/Desktop/Reflectify/Images/" + file
        self.camera.capture(filename)

        self.show_popup("Image saved!")

    def show_popup(self, message):
        self.popup = QFrame(self)
        popup_width, popup_height = 200, 100
        self.popup.setGeometry(0, 0, popup_width, popup_height)
        self.popup.setStyleSheet("background-color: white;")

        x_position = (self.width() - popup_width) // 2
        y_position = (self.height() - popup_height) // 2
        self.popup.move(x_position, y_position)

        label = QLabel(message, self.popup)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, popup_width, popup_height)

        self.popup.show()
        QTimer.singleShot(3000, self.popup.close) 

    def start_countdown(self):
        self.countdown_value = 5
        self.show_popup(str(self.countdown_value))
        self.countdown_timer.start(1000) 

    def update_countdown(self):
        self.countdown_value -= 1
        if self.countdown_value == 0:
            self.countdown_timer.stop()
            self.popup.close()
            self.capture_image_now()
        elif self.countdown_value == 1:
            self.show_popup("Smile please!")
        else:
            self.show_popup(str(self.countdown_value))

            
    def closeEvent(self, event):
        self.camera.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CameraApp()
    main_window.show()
    sys.exit(app.exec_())