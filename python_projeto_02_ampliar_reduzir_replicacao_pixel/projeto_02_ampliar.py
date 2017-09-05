'''
    Escreva um programa capaz de ampliar e reduzir uma imagem por replicação
    de pixel. Assuma que os fatores de ampliação/redução sejam inteiros;
'''

from PIL import Image

# Path da imagem
src_image = "out_image_512_python.png"

# Imagem de entrada
in_img = Image.open(src_image)

# Tamanho da imagem LINHAS, COLUNAS
M, N = in_img.size

# Carrega na variavel a imagem de entrada
in_pixel = in_img.load()

# Entrada da redução
aumentar = int(input("Digite quanto vc quer que amplie"))

MM = M * aumentar
NN = N * aumentar

k = 1
l = 1

#TodO..........
# Imagem de saida
out_img = Image.new("L", (MM,NN))
out_pixel = out_img.load()

for m in range(1, MM):
    for n in range(1, NN):
        out_pixel[m,n] = in_pixel[k,l]
        l = l + 1
    l = 1
    k = k + 1

for m in range(1, MM):
    for n in range(2, NN):
        out_pixel[m,n] = in_pixel[m,n-1]

for m in range(1, MM):
    for n in range(2, NN):
        out_pixel[m,n] = in_pixel[m-1,n]

for m in range(2, MM):
    for n in range(2, NN):
        out_pixel[m,n] = in_pixel[m,n-1]

out_img.save('out_image_python.png', 'png')

# Mostra imagem de saida
out_img.show()
