import cv2 as cv
import numpy as np
import os
from filters import PencilSketch
from glob import glob
from make_sketch import make_sketch

m = 240
n = 320
DIR_PATH = '../img_align_celeba/'
SKETCH_PATH = '../celeba_sketch/'

for file_path in glob(DIR_PATH + '*.jpg'):
    make_sketch(file_path, SKETCH_PATH)
    # img = cv.imread(file_path)
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # height, width, channels = img.shape
    # if (height, width, channels) != (m, n, 3):
	   #  img = np.resize(img, (m, n, 3))
    # pencil = PencilSketch(width, height)
    # sketch = pencil.render(img)
    # write_path = os.path.join(SKETCH_PATH, file)
    # cv.imwrite(write_path, sketch)
    