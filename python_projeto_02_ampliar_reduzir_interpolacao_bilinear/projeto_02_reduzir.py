'''
    Escreva um programa capaz de ampliar e reduzir uma imagem por replicação
    de pixel. Assuma que os fatores de ampliação/redução sejam inteiros;
'''

from PIL import Image

# Path da imagem
src_image = "../img/Fig0219.tif"

# Imagem de entrada
in_img = Image.open(src_image)

# Tamanho da imagem LINHAS, COLUNAS
M, N = in_img.size

# Carrega na variavel a imagem de entrada
in_pixel = in_img.load()

# Entrada da redução
reducao = input("Digite quanto vc quer que diminua")

MM = round(M / reducao)
NN = round(N / reducao)

#TodO..........
# Imagem de saida
out_img = Image.new("L", (M,N))
out_pixel = out_img.load()

menor = 255
maior = 0

for m in range(M):
    for n in range(N):
        out_pixel[m,n] = round((Nc/255)*in_pixel[m,n])

for m in range(M):
    for n in range(N):
        if menor > out_pixel[m,n]:
            menor = out_pixel[m,n]
        if maior < out_pixel[m,n]:
            maior = out_pixel[m,n]


for m in range(M):
    for n in range(N):
        out_pixel[m,n] = round(255 * ((out_pixel[m, n] - menor)/(maior - menor)))

out_img.save('out_image_python-'+ str(number) + '.png', 'png')

# Mostra imagem de saida
out_img.show()
