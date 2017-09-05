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
reducao = int(input("Digite quanto vc quer que diminua"))

MM = round(M / reducao)
print(str(MM))
NN = round(N / reducao)
print(str(NN))

k = 1
l = 1

#TodO..........
# Imagem de saida
out_img = Image.new("L", (MM,NN))
out_pixel = out_img.load()

for m in range(MM):
    for n in range(NN):
        out_pixel[m,n] = in_pixel[k,l]
        l = l + reducao
    l = 1
    k = k + reducao

out_img.save('out_image_XXX_python.png', 'png')

# Mostra imagem de saida
out_img.show()
