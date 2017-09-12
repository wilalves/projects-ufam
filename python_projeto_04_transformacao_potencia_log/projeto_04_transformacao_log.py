import math
from PIL import Image

# Entrada do numero
number = int(input('Digite aqui o parametro C'))

# Path da imagem
src_img = '../img/Fig0308.tif'

# Imagem de entrada
in_img = Image.open(src_img)
in_img.show()

[M, N] = in_img.size

# Imagem de saida
out_img = Image.new("L", (M,N))
out_pixel = out_img.load()

# Carrega na variavel a imagem de entrada
in_pixel = in_img.load()

#Calculando os n�veis de cinza para imagem
for m in range(M):
    for n in range(N):
        out_pixel[m,n] = round(number*math.log10(1+in_pixel[m,n]))


out_img.save('out_image_python-'+ str(number) + '.png', 'png')

out_img.show()