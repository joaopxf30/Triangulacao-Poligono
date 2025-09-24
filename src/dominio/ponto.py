from fontTools.varLib.interpolatableHelpers import PerContourPen

from src.dominio.vetor import Vetor
import math


class Ponto:
    def __init__(self, x: float, y: float):
        self.coord_x = x
        self.coord_y = y

    def __key(self):
        return self.coord_x, self.coord_y

    def __eq__(self, ponto: "Ponto"):
        if not isinstance(ponto, Ponto):
            return False

        return self.__key() == ponto.__key()

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

