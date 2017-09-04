% Escreva um programa capaz de ampliar e reduzir uma imagem por replica��o
% de pixel. Assuma que os fatores de amplia��o/redu��o sejam inteiros;

% Caminho do arquivo que dever� ser modificado
path = 'matlab_image_32.png';

I = imread(path);

[M, N] = size(I);

% Inteiro de entrada
f = 2;

M1 = M * f;
N1 = N * f;

k=1;
l=1;

% Criando uma imagem de saida do mesmo tamanho da de entrada
I_out = zeros(M1, N1);

for i=1:f:M1
   for j=1:f:N1
       I_out(i,j)= I(k,l);
       l=l+1;
   end
   l=1;
   k=k+1;
end

for i=1:f:M1
   for j=2:f:N1
       I_out(i,j)=I_out(i,j-1);
   end
end

for j=1:f:M1
    for i=2:f:N1
        I_out(i,j)=I_out(i-1,j);
    end
end

for i=2:f:M1
    for j=2:f:N1
        I_out(i,j)= I_out(i,j-1);
    end
end

imshow(I, []);
figure;
imshow(I_out, []);
imwrite(I_out,'Fig0219_zoom_1024).tif');
