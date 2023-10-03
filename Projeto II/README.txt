Geometria Python

Este é um projeto Python que implementa classes para representar pontos, linhas, polígonos, quadrados e círculos, juntamente com métodos para calcular seus perímetros e áreas. 
Este código pode ser usado como base para cálculos geométricos simples.


Classes

Ponto: A classe Ponto representa um ponto no plano cartesiano. Crie pontos com Ponto(x, y), onde x e y são as coordenadas do ponto.
Linha: A classe Linha representa uma linha entre dois pontos. Pode-se criar uma linha usando Linha(ponto1, ponto2), onde ponto1 e ponto2 são instâncias da classe Ponto.
Poligono: A classe Poligono representa um polígono formado por uma lista de pontos. Para criar um polígono, a classe Poligono pode ser utilizada. Cada polígono é formado 
por uma lista de pontos, onde cada ponto é representado como uma instância da classe Ponto.
Quadrado e Circulo: São subclasses de Poligono e representam um quadrado e um círculo, respectivamente. Pra fazer um quadrado a subclasse Quadrado(lado) deve ser utilizada, 
o lado é o comprimento do lado do quadrado. E para fazer um círculo a do Circulo(raio), raio do círculo, deve ser usado.


Métodos 

comprimento(): Calcula o comprimento da linha ou o perímetro do polígono.
areaQuadrado(): Calcula a área do quadrado.
perimetroQuadrado(): Calcula o perímetro do quadrado.
areaCirculo(): Calcula a área do círculo.
perimetroCirculo(): Calcula o perímetro do círculo.
