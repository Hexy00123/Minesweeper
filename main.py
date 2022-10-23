import cv2 # image capture
import numpy as np # work with images
import qimage2ndarray # image type converter
import PIL # image wrapper
from PIL import ImageGrab
import sys
from PyQt5 import QtCore, QtGui, QtWidgets # GUI
from PyQt5 import uic

from constants import *

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main_window.ui', self)

        self.frame_timer = QtCore.QTimer()
        self.frame_timer.timeout.connect(self.take_screenshot)
        self.frame_timer.start(int(1000 / fps))
        self.moving_frame_origin_x.setText("63")
        self.moving_frame_origin_y.setText("303")


    def take_screenshot(self):
        try: # 63, 290
            x, y = int(self.moving_frame_origin_x.text()), int(self.moving_frame_origin_y.text())
            img = ImageGrab.grab(bbox=(x, y, x + ceil_size[1] * map_size[1], y + ceil_size[0] * map_size[0]))

            frame = np.array(img)
            image = qimage2ndarray.array2qimage(frame)
            self.main_frame.setPixmap(QtGui.QPixmap.fromImage(image))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(application.exec())


