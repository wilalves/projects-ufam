% Escreva um programa de computador capaz de reduzir o número de niveis de
% intensidade emu ma imagem de 256 a 2 em incrementos inteiros de potencia de 2.
% O número de níveis de intensidade deve ser uma variável de entrada do seu programa


% Caminho do arquivo que deverá ser modificado
path = './img/Fig0221.tif';

% Novo nível de cinza da imagem
% K é o número de bits
% K = 0;

k = input('Digite o numero de bits');
Nc = 2 .^ k;

% Imagem de entrada 
I = imread(path);

%Extraindo o número de linhas(M) e colunas(N) da imagem
[M, N] = size(I);

imshow(I,[]);
title('Imagem original');

%Criando uma imagem de saida do mesmo tamanho da de entrada
I_out = zeros(M,N);

%Calculando os novos níveis de cinza para imagem
for m = 1:M
    for n = 1:N
        I_out(m,n) = (Nc/256)*I(m,n);
    end
end

imwrite(I_out, 'matlab_imagem_8.png');

figure();
imshow(I_out, []);
