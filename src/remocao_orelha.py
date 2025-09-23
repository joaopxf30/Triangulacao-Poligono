from src.dominio import Poligono, Triangulo, Vetor


class RemocaoOrelha:

    def realiza_triangulacao(self, poligono: Poligono):
        diagonais_candidatas = self._determina_orelha(poligono)
        diagonais_validas = self._determina_diagonais_validas(diagonais_candidatas)
        ...

    def _determina_orelha(self, poligono: Poligono) -> Triangulo:
        ciclo_vertices =  [*poligono.vertices, *poligono.vertices[:2]]
        triplas_vertices = zip(ciclo_vertices, ciclo_vertices[1:], ciclo_vertices[2:])

        for vertice_previo, vertice, vertice_posterior in triplas_vertices:
            vetor_1 = vertice - vertice_previo
            vetor_2 = vertice_posterior - vertice

            produto_vetorial = vetor_1 * vetor_2
            orientacao = produto_vetorial.coord_z

            if orientacao <= 0:
                continue

            else:
                ...

    @staticmethod
    def _checa_se_diagonal_valida(diagonal: Vetor, vetores: list[Vetor]) -> bool:


