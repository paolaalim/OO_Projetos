import math

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

class Linha:
    def __init__(self, pnt1, pnt2):
        self.__pnt1 = pnt1
        self.__pnt2 = pnt2
    
    def comprimento(self):
        return math.sqrt((self.__pnt2._Ponto__x - self.__pnt1._Ponto__x) ** 2 +
                         (self.__pnt2._Ponto__y - self.__pnt1._Ponto__y) ** 2)

class Poligono:
    def __init__(self, pontos):
        self.__pontos = pontos
    
    def perímetro(self):
        total = 0
        num_pontos = len(self.__pontos)
        for i in range(num_pontos):
            linha = Linha(self.__pontos[i], self.__pontos[(i + 1) % num_pontos])
            total += linha.comprimento()
        return total

class Quadrado(Poligono):
    def __init__(self, lado):
        ponto1 = Ponto(0, 0)
        ponto2 = Ponto(lado, 0)
        ponto3 = Ponto(lado, lado)
        ponto4 = Ponto(0, lado)
        super().__init__([ponto1, ponto2, ponto3, ponto4])
        self.__lado = lado
    
    def areaQuadrado(self):
        return self.__lado ** 2
    
    def perimetroQuadrado(self):
        return self.perímetro()

class Círculo(Ponto):
    def __init__(self, raio):
        super().__init__(0, 0)
        self.__raio = raio
    
    def areaCírculo(self):
        return math.pi * self.__raio ** 2
    
    def perimetroCírculo(self):
        return 2 * math.pi * self.__raio
