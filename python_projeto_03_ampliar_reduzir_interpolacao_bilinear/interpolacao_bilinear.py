from PIL import Image

# def interpolacao_bilinear (self, src_image, resolucao):

    # Imagem de entrada
src_image = "../img/Fig0219.tif"
in_img = Image.open(src_image)

M, N = in_img.size

resolucao_in = in_img.info['resolution']

print(resolucao_in)

