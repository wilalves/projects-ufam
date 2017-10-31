from PIL import Image
import numpy as np

from meu_filtro import my_filter

src_image = "../img/Fig0338.tif"

T = Image.open(src_image)

T.show()

w = (1/9)*[[1, 1, 1],[1, 1, 1],[1, 1, 1]]
print(w)

# I2 = im2double(I)
Blurred = myfilter(I2,w)

Gmask = I2 - Blurred
Gmask.imshow()

I_out = I2 + K*Gmask
I_out.imshow(I_out)

K = 4.5
I_out_h = I2 + K*Gmask
I_out_h.show()