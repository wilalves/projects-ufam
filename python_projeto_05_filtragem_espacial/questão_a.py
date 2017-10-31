from PIL import Image
import numpy as np

from meu_filtro import my_filter

src_image = "../img/Fig0338.tif"

T = Image.open(src_image)

T.show()

w = np.ones((3,3))

img_done = my_filter(T,w)

img_done.show()