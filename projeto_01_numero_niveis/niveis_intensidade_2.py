'''
    Escreva um programa de computador capaz de reduzir o número de níveis de intensidade
    em uma imagem de 256 a 2 em incrementos inteiros de potencia de 2. O número de níveis
    de intensidade deve ser uma variavel de entrada do seu programa
'''

from PIL import Image

# Entrada do numero
number = int(input('Digite Aqui a quantidade de Bits'))

# Path da imagem
src_image = "../../img/Fig0221.tif"

# Numero de Bits
K = number

# Niveis de cinza
Nc = 2 ** K

# Imagem de entrada
in_img = Image.open(src_image)

# Salvar imagem de entrada
in_img.save('in_image.png', 'png')

#mostra imagem de entrada
in_img.show()

# Carrega na variavel a imagem de entrada
in_pixel = in_img.load()

# Tamanho da imagem LINHAS, COLUNAS
M, N = in_img.size

# Imagem de saida
out_img = Image.new("L", (M,N))
out_pixel = out_img.load()

menor = 255
maior = 0

for m in range(M):
    for n in range(N):
        out_pixel[m,n] = round((Nc/256)*in_pixel[m,n])

for m in range(M):
    for n in range(N):
        if menor > out_pixel[m,n]:
            menor = out_pixel[m,n]
        if maior < out_pixel[m,n]:
            maior = out_pixel[m,n]


for m in range(M):
    for n in range(N):
        out_pixel[m,n] = round(255 * ((out_pixel[m, n] - menor)/(maior - menor)))

out_img.save('foto'+ str(number) + '.png', 'png')

# Mostra imagem de saida
out_img.show()
