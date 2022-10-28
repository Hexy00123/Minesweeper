from json import loads
from cv2 import imread

file = open("constants.json", mode="rt")
constants = loads(file.read())

UI_PATH = constants["UI_PATH"]

TYPES_OF_CELLS = {key: imread(constants["CELLS"][key]) for key in constants["CELLS"]}

FPS = constants["FPS"]

CELL_SIZE = constants["CELL_SIZE"]
MAP_SIZE = constants["MAP_SIZE"]

CUTTING = constants["CUTTING"]

MIN_HSV = constants["MIN_HSV"]
MAX_HSV = constants["MAX_HSV"]

LEFT_COORDINATE = 64
TOP_COORDINATE = 343
