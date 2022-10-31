import cv2  # image capture
import numpy as np  # work with images
import qimage2ndarray  # image type converter
from mss import mss  # screen capturer

import sys

from PyQt5 import QtCore, QtGui, QtWidgets  # GUI
from PyQt5 import uic

from Detector import Detector
from Map import Map
from constants import *

from PIL import Image


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)
        self.init_UI_objects()

        self.screen_capture = mss()
        self.current_frame: np.array

        self.detector = Detector(TYPES_OF_CELLS)
        self.map = Map()

        self.frame_timer = QtCore.QTimer()
        self.frame_timer.timeout.connect(self.take_screenshot)
        self.frame_timer.start(int(1000 / FPS))

    def get_image(self):
        im = self.detector.get_cell(self.current_frame, 12,2)
        Image.fromarray(im).save('templates/opened_cell_6_l.png')

    def init_UI_objects(self):
        self.main_frame: QtWidgets.QLabel

        self.updateFieldButton: QtWidgets.QPushButton
        self.updateFieldButton.clicked.connect(self.get_image)

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

        frame = self.analyse_frame(frame)
        frame = qimage2ndarray.array2qimage(frame)
        self.main_frame.setPixmap(QtGui.QPixmap.fromImage(frame))

    def analyse_frame(self, frame):
        try:
            frame = frame.copy()
            self.map.upload_map(self.detector.detect_frame(self.current_frame))
            scanning_result = self.map.analyse()

            #flag_image = cv2.imread('templates/flag.png')

            for flag_coordinate in scanning_result['flag']:
                coord = flag_coordinate
                for i in range(45):
                    for j in range(45):
                        frame[coord[1]*45 + i, coord[0]*45 + j] = np.array([0, 0, 0])

            for open_coordinates in scanning_result['open']:
                coord = open_coordinates
                for i in range(45):
                    for j in range(45):
                        frame[coord[1] * 45 + i, coord[0] * 45 + j] = np.array([255,255,255])

            return frame
        except Exception as e:
            print(e)


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(application.exec())
