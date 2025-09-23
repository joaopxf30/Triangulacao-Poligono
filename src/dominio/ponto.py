from src.dominio.vetor import Vetor
import math


class Ponto:
    def __init__(self, x: float, y: float):
        self.coord_x = x
        self.coord_y = y

    def __add__(self, vetor: Vetor) -> "Ponto":
        if not isinstance(vetor, Vetor):
            raise TypeError("Operando deve ser da classe Vetor")

        coord_x = self.coord_x + vetor.coord_x
        coord_y = self.coord_y + vetor.coord_y

        return Ponto(coord_x, coord_y)

    def __sub__(self, ponto: "Ponto") -> Vetor:
        if not isinstance(ponto, Ponto):
            raise TypeError("Operando deve ser da classe Ponto")

        coord_x = self.coord_x - ponto.coord_x
        coord_y = self.coord_y - ponto.coord_y

        return Vetor(coord_x, coord_y)

    def busca_ponto_medio(self, outro: "Ponto") -> "Ponto":
        if not isinstance(outro, Ponto):
            raise TypeError("Operando deve ser da classe Ponto")

        ponto_medio = self + (outro - self) * 0.5

        return ponto_medio

    def calcula_determinante_tres_pontos(self, ponto_1: "Ponto", ponto_2: "Ponto") -> float:
        if not isinstance(ponto_1, Ponto) and not isinstance(ponto_2, Ponto):
            raise TypeError("Operando deve ser da classe Ponto")

        determinante = (
            self.coord_x * ponto_1.coord_y + self.coord_y * ponto_2.coord_x +
            ponto_1.coord_x * ponto_2.coord_y - self.coord_y * ponto_1.coord_x -
            ponto_1.coord_y * ponto_2.coord_x - self.coord_x * ponto_2.coord_y
        )

        return determinante
