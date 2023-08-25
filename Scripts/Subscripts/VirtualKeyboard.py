import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: black;")
        label.setStyleSheet("color: white;")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1373, 778, 510, 300)
        self.entry = QLineEdit(self)
        self.entry.setStyleSheet("color: white;")

        # Tastaturtasten
        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<-',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            '^', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>',
            ' ', 'Save'
        ]

        grid = QGridLayout()
        grid.addWidget(self.entry, 0, 0, 1, 15)

        row = 1
        col = 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("QPushButton { color: white; }")
            btn.clicked.connect(lambda _, b=button: self.button_click(b))
            grid.addWidget(btn, row, col)
            
            col += 1
            if col > 10:
                col = 0
                row += 1

        self.setLayout(grid)

    def button_click(self, char):
        if char == 'Save':
            self.copy_to_clipboard()
        elif char == '<-':
            current_text = self.entry.text()
            self.entry.setText(current_text[:-1])
        else:
            self.entry.setText(self.entry.text() + char)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.entry.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    label = QWidget(main_window)
    main_window.setCentralWidget(label)

    keyboard = VirtualKeyboard()
    keyboard.show()

    sys.exit(app.exec_())


