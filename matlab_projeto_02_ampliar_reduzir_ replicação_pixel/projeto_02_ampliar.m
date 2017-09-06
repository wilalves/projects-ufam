% Escreva um programa capaz de ampliar e reduzir uma imagem por replicação
% de pixel. Assuma que os fatores de ampliação/redução sejam inteiros;

% Caminho do imagem
path = 'matlab_image_512.png';

I = imread(path);

[M, N] = size(I);

% Inteiro de entrada
f = 2;

for c=1:1:N
    AA(:,f*c) = I(:,c);
    AA(:,(f*c-1)) = AA(:,f*c);
end
    
% Replicando linhas:
for c=1:1:M
    BB(f*c,:)= AA(c,:);
    BB((f*c-1),:)= BB(f*c,:);
end

figure;
imshow(BB, []);
imwrite(BB,'Fig0219_zoom_1024).tif');
