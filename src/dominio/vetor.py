import math


class Vetor:
    def __init__(self, x: float, y: float, z: float = 0):
        self.coord_x = x
        self.coord_y = y
        self.coord_z = z

    def __mul__(self, entidade: "float | Vetor") -> "Vetor":
        match entidade:
            case float():
                return self.__calcula_produto_escalar(entidade)

            case Vetor():
                return self.calcula_produto_vetorial(entidade)

            case _:
                raise TypeError("Somente produto escalar e vetorial são implementados")

    def calcula_norma_euclidiana(self) -> float:
        p_norma_2 = math.sqrt(self.coord_x**2 + self.coord_y**2)

        return p_norma_2

    def __calcula_produto_escalar(self, escalar: float) -> "Vetor":
        if escalar < 0 or escalar > 1:
            raise ValueError("Parâmetro deve estar entre 0 e 1")

        coord_x = escalar * self.coord_x
        coord_y = escalar * self.coord_y

        return Vetor(coord_x, coord_y)

    def calcula_produto_vetorial(self, vetor: "Vetor") -> "Vetor":
        coord_x = self.coord_y * vetor.coord_z - self.coord_z * vetor.coord_y
        coord_y = self.coord_z * vetor.coord_x - self.coord_x * vetor.coord_y
        coord_z = self.coord_x * vetor.coord_y - self.coord_y * vetor.coord_x

        return Vetor(coord_x, coord_y, coord_z)
