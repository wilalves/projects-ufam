from PIL import Image
import numpy as np

from meu_filtro import my_filter

src_image = "../img/Fig0338.tif"

T = Image.open(src_image)

T.show()

w = [[1, 1, 1],[1, -8, 1], [1, 1, 1]]

print(w)

Boarder = my_filter(T2, w)
boarder.show()

I_out = T2 - Boarder
imshow(I_out);

img_done = my_filter(T,w)

img_done.show()