import cv2
from constants import *


class Detector():
    def __init__(self, templates: dict):
        self.min_hsv = tuple(MIN_HSV)
        self.max_hsv = tuple(MAX_HSV)
        self.original_templates = templates
        self.wrapped_templates = {key: self.put_mask(self.original_templates[key]) for key in self.original_templates}

    def put_mask(self, img):
        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        img = cv2.inRange(img, self.min_hsv, self.max_hsv)
        return img

    def get_amount_of_colors(self, img):
        res = set()
        for x in range(len(img)):
            for y in range(len(img[0])):
                res.add(img[x, y])
        return len(res)

    def find_template(self, img):
        mask = self.put_mask(img)
        result = []
        for key in self.wrapped_templates:
            template = self.wrapped_templates[key]
            result.append((key, cv2.matchTemplate(mask, template, cv2.TM_SQDIFF)[0][0]))
        return min(result, key=lambda x: x[1])[0]

    def get_cell(self, img, x, y):
        x, y = y, x
        return img[
               x * CELL_SIZE["width"] + CUTTING:(x + 1) * CELL_SIZE["width"] - CUTTING,
               y * CELL_SIZE["height"] + CUTTING:(y + 1) * CELL_SIZE["height"] - CUTTING,
               ]
