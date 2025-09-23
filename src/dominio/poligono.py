from itertools import pairwise
from src.dominio import Ponto, Vetor


class Poligono:
    def __init__(self, vertices: list[Ponto]):
        self.vertices = vertices
        self.arestas: list[Vetor] = self._determina_arestas()

    def _determina_arestas(self) -> list[Vetor]:
        ciclo_vertices = [*self.vertices, self.vertices[0]]
        arestas = []

        for vertice_previo, vertice_posteior in pairwise(ciclo_vertices):
            aresta = vertice_posteior - vertice_previo
            arestas.append(aresta)

        return arestas
