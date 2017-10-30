from PIL import Image
import numpy as np

from projeto_05_filtragem_espacial_filter import *

src_image = "../img/Fig0338.tif"

in_img = Image.open(src_image)

# in_img.show()

in_pixel = in_img.load()

mascara = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float)
print(mascara)

out_process_img = Image.fromarray(normalize(in_img).astype('uint8'),'TIFF')

aaa = meu_filtro(out_process_img, mascara)

aaa.show()

img_out_full = process_img - aaa

img_out_full.show()

