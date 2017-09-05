% Caminho do imagem
path = './Fig0220a.tif';

I = imread(path);

imshow(I);
title('Imagem de entrada');

% Calculando a nova imagem
I_out = interpolacao_bilinear(path, 100);

figure;
imshow(I_out);
title('Reduziu para 100 DPI');

% Caminho onde a imagem modificada será salva
path1 = './Fig0220a_100dpi.tif';
imwrite(I_out,path1);

% Ampliando novamente a imagem que foi reduzida
I_out1 = interpolacao_bilinear(path1, 1250);

figure;
imshow(I_out1);
title('Ampliou para 1250 DPI');

path2 = './Fig0220a_1250dpi.tif';
imwrite(I_out1,path2);

