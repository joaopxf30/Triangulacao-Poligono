from src.dominio import Ponto
from src.dominio.poligono import Poligono


class Triangulo(Poligono):
    def __init__(self, vertices: list[Ponto]):
        if len(vertices) != 3:
            raise ValueError("Triângulo só admite três vértices")

        super().__init__(vertices)

        self.vertice_previo = self.vertices[0]
        self.vertice = self.vertices[1]
        self.vertice_posterior = self.vertices[-1]

