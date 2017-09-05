% Escreva um programa capaz de ampliar e reduzir uma imagem por replicação
% de pixel. Assuma que os fatores de ampliação/redução sejam inteiros;

% Caminho do arquivo que deverá ser modificado
path = './img/Fig0219.tif';

I = imread(path);

[M, N] = size(I);

% Inteiro de entrada
f=input('Entre com o fator de redução da imagem: ');

M1 = round(M / f);
fprintf('%d',M1);
N1 = round(N / f);
fprintf('%d',N1);

k=1;
l=1;

% imshow(I, []);
% title('Imagem original');

% Criando uma imagem de saida do mesmo tamanho da de entrada
I_out = zeros(M1, N1);

for m = 1:M1
    for n = 1:N1
        I_out(m,n) = I(k,l);
        l=l+f;
    end
    l=1;
    k=k+f;
end

imwrite(I_out, 'matlab_imagem_64', 'jpg');

figure();
imshow(I_out, []);
