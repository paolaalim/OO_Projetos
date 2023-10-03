Geometria Python

Este é um projeto Python que implementa classes para representar pontos, linhas, polígonos, quadrados e círculos, juntamente com métodos para calcular seus perímetros e áreas. Este código foi desenvolvido como parte de um projeto para a faculdade e pode ser usado como base para cálculos geométricos simples.

Instruções de Uso

Ponto: A classe Ponto representa um ponto no plano cartesiano. Você pode criar um ponto usando Ponto(x, y), onde x e y são as coordenadas do ponto.

Linha: A classe Linha representa uma linha entre dois pontos. Você pode criar uma linha usando Linha(ponto1, ponto2), onde ponto1 e ponto2 são instâncias da classe Ponto.

Polígono: A classe Poligono representa um polígono formado por uma lista de pontos. Você pode criar um polígono usando Poligono([ponto1, ponto2, ponto3, ...]), onde cada ponto é uma instância da classe Ponto.

Quadrado: A classe Quadrado é uma subclasse de Poligono e representa um quadrado. Você pode criar um quadrado usando Quadrado(lado), onde lado é o comprimento de um lado do quadrado.

Círculo: A classe Círculo é uma subclasse de Ponto e representa um círculo. Você pode criar um círculo usando Círculo(raio), onde raio é o raio do círculo.

Métodos Disponíveis

Para Linhas e Polígonos:

comprimento(): Calcula o comprimento da linha ou o perímetro do polígono.
Para Quadrados:

areaQuadrado(): Calcula a área do quadrado.
perimetroQuadrado(): Calcula o perímetro do quadrado.
Para Círculos:

areaCirculo(): Calcula a área do círculo.
perimetroCirculo(): Calcula o perímetro do círculo.
