import cv2  # image capture
import numpy as np  # work with images
import qimage2ndarray  # image type converter
from mss import mss  # screen capturer

import sys

from PyQt5 import QtCore, QtGui, QtWidgets  # GUI
from PyQt5 import uic

from Detector import Detector
from constants import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)
        self.init_UI_objects()

        self.screen_capture = mss()
        self.current_frame: np.array
        self.detector = Detector(TYPES_OF_CELLS)

        # self.frame_timer = QtCore.QTimer()
        # self.frame_timer.timeout.connect(self.take_screenshot)
        # self.frame_timer.start(int(1000 / FPS))

    def init_UI_objects(self):
        self.main_frame: QtWidgets.QLabel

        self.updateFieldButton: QtWidgets.QPushButton
        self.updateFieldButton.clicked.connect(self.take_screenshot)

    def take_screenshot(self):
        frame = self.screen_capture.grab({
            'top': TOP_COORDINATE,
            'left': LEFT_COORDINATE,
            'width': CELL_SIZE["width"] * MAP_SIZE["width"],
            'height': CELL_SIZE["height"] * MAP_SIZE["height"]
        })
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.current_frame = frame

        frame = qimage2ndarray.array2qimage(frame)
        self.main_frame.setPixmap(QtGui.QPixmap.fromImage(frame))


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(application.exec())
