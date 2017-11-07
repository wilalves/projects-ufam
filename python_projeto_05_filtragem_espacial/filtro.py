'''
    This Example opens an Image and transform the image into grayscale, halftone, dithering, and primary colors.
    You need PILLOW (Python Imaging Library fork) and Python 3.5.
    -Isai B. Cicourel
'''

# Imported PIL Library
from PIL import Image

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
  image = Image.new("L", (i, j))
  return image


# Get the pixel from the given image
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None

  # Get Pixel
  pixel = image.getpixel((i, j))
  return pixel

def meu_filtro(imagem, mascara):
    M, N = imagem.size
    mm, nn = mascara.size

    nova = create_image(M, N)
    pixels = nova.load()

    mascara = create_image(mm, nn)
    pixels_mascara = mascara.load()

    for m in range(2, M - 1):
        for n in range(2, N - 1):
            pixels[m - 1, n - 1] = \
                pixels_mascara[0, 0] * get_pixel(nova, m - 1, n - 1) + \
                pixels_mascara[0, 1] * get_pixel(nova, m - 1, n)   + \
                pixels_mascara[0, 2] * get_pixel(nova, m - 1, n + 1) + \
                pixels_mascara[1, 0] * get_pixel(nova, m, n - 1) + \
                pixels_mascara[1, 1] * get_pixel(nova, m, n) + \
                pixels_mascara[1, 2] * get_pixel(nova, m, n + 1) + \
                pixels_mascara[2, 0] * get_pixel(nova, m + 1, n-1) + \
                pixels_mascara[2, 1] * get_pixel(nova, m + 1, n) + \
                pixels_mascara[2, 2] * get_pixel(nova, m + 1, n+1)

    return nova