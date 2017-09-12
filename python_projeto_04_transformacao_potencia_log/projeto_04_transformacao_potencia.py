import math
from PIL import Image

# Entrada do numero
number = int(input('Digite aqui o parametro C'))
lambd =  float(input('Digite aqui o parametro gamma'))

# Path da imagem
src_img = '../img/Fig0308.tif'

# Imagem de entrada
in_img = Image.open(src_img)


[M, N] = in_img.size

# Imagem de saida
out_img = Image.new("L", (M,N))
out_pixel = out_img.load()

# Carrega na variavel a imagem de entrada
in_pixel = in_img.load()

#Calculando os n�veis de cinza para imagem
for m in range(M):
    for n in range(N):
        out_pixel[m,n] = round(number*((in_pixel[m,n]) ** lambd))


out_img.save('out_image_python-po'+ str(number) + '.png', 'png')

out_img.show()