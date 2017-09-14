'''
    Escreva um programa capaz de ampliar e reduzir uma imagem por replicação
    de pixel. Assuma que os fatores de ampliação/redução sejam inteiros;
'''

from PIL import Image

# Path da imagem
src_image = "out_image_256_python.png"

# Imagem de entrada
in_img = Image.open(src_image)

# Carrega na variavel a imagem de entrada
in_pixel = in_img.load()

# Tamanho da imagem LINHAS, COLUNAS
M, N = in_img.size

# Entrada da redução
aumentar = int(input("Digite quanto vc quer que amplie"))

MM = M * aumentar
NN = N * aumentar

w = 0
h = 0

# Imagem de saida
out_img = Image.new("L", (MM,NN))
W, H = out_img.size
out_pixel = out_img.load()

for m in range(0, W, aumentar):
    for n in range(0, H, aumentar):
        out_pixel[m,n] = in_pixel[w,h]
        h = h + 1
    h = 0
    w = w + 1

for m in range(0, W, aumentar):
    for n in range(1, H, aumentar):
        out_pixel[m,n] = out_pixel[m,n-1]

for m in range(1, W, aumentar):
    for n in range(0, H, aumentar):
        out_pixel[m,n] = out_pixel[m-1,n]

for m in range(1, W, aumentar):
    for n in range(1, H, aumentar):
        out_pixel[m,n] = out_pixel[m,n-1]

out_img.save('out_2-4image_python.png', 'png')

# Mostra imagem de saida
out_img.show()
