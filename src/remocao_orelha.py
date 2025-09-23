from src.dominio import Poligono, Triangulacao


class RemocaoOrelha:

    def realiza_triangulacao(self, poligono: Poligono):
        self._determina_diagonais(poligono)
        ...

    def _determina_diagonais(self, poligono: Poligono) -> list[Vetor]:
        orelhas = []

        ciclo_vertices =  poligono.gera_ciclo_vertices()
        triplas_vertices = zip(ciclo_vertices, ciclo_vertices[1:], ciclo_vertices[2:])

        for vertice_previo, vertice, vertice_posterior in triplas_vertices:
            vetor_1 = vertice - vertice_previo
            vetor_2 = vertice_posterior - vertice

            produto_vetorial = vetor_1 * vetor_2
            orientacao = produto_vetorial.coord_z

            if orientacao <= 0:
                continue

            else:
                diagonal = vertice_posterior - vertice_previo

