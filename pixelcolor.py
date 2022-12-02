import sys
import pyautogui
import threading as tr

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton


class PixelColor(QWidget):
    def __init__(self):
        super().__init__()
        self.p = None
        self.save_data = None
        self.setMouseTracking(True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: #FF7F27; color: #fff;")
        self.pixelColor = ''
        self.resize(200, 100)
        self.rgb = QLabel(self)
        self.rgb.move(10, 30)
        save_info = QLabel(self)
        save_info.setText('Click "x" for save HEX to buffer')
        save_info.resize(180, 10)
        save_info.move(10, 8)
        self.hex = QLabel(self)
        self.hex.move(10, 50)
        self.close_button = QPushButton(self)
        self.close_button.setText('X')
        self.close_button.resize(15, 15)
        self.close_button.move(180, 5)
        self.close_button.clicked.connect(self.stop)
        self.run_pic_color = True
        self.color_sqr = QLabel(self)
        self.color_sqr.resize(50, 50)
        self.color_sqr.move(140, 40)
        self.save_data = ''

        self.show()

    def stop(self):
        self.close()
        self.p.on_work = False

    def stop_thread(self):
        self.p = p

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self._move()
            return super().mousePressEvent(e)

    def _move(self):
        window = self.window().windowHandle()
        window.startSystemMove()

    def keyPressEvent(self, e):
        if e.key() == 88:
            app.clipboard().setText(self.save_data)


class GetPix:
    def __init__(self):
        super().__init__()
        self.save_data = None
        self.pixelColor = ''
        self.run_pic_color = w.run_pic_color
        self.rgb = w.rgb
        self.hex = w.hex
        self.color = w.pixelColor
        self.color_sqr = w.color_sqr
        self.rgb.resize(100, 20)
        self.hex.resize(100, 20)
        self.on_work = True

    def get_pix(self):
        try:
            while self.on_work:
                x, y = pyautogui.position()
                pixel_color = pyautogui.screenshot().getpixel((x, y))
                self.rgb.pixelColor = str(pixel_color)
                self.rgb.setText('RGB: ' + self.rgb.pixelColor)
                self.hex.setText('HEX: ' + '#%02X%02X%02X' % pixel_color)
                w.save_data = '#%02X%02X%02X' % pixel_color
                self.color_sqr.setStyleSheet(f"background-color: {'rgb' + self.rgb.pixelColor}")
        except IndexError:
            self.get_pix()


app = QApplication(sys.argv)

w = PixelColor()
p = GetPix()
w.stop_thread()
pp = tr.Thread(target=p.get_pix, args=())
pp.start()

sys.exit(app.exec())
