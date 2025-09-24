from src.dominio import Poligono, Triangulo, Ponto, Segmento
from src.plot import plota_triangulacao


class RemocaoOrelha:

    def realiza_triangulacao(self, poligono: Poligono) -> list[Triangulo]:
        triangulacao = []

        while len(poligono.vertices) >= 3:
            triangulo = self._determina_orelha(poligono)
            triangulacao.append(triangulo)

            vertices = poligono.vertices.copy()
            vertice_a_remover = triangulo.vertice
            index = poligono.vertices.index(vertice_a_remover)

            vertices = self._rotaciona_vertices(vertices, index)
            vertices.remove(vertice_a_remover)

            poligono = Poligono(vertices)

        return triangulacao

    def _determina_orelha(self, poligono: Poligono) -> Triangulo:
        if len(poligono.vertices) == 3:
            return Triangulo(poligono.vertices)

        arestas = poligono.arestas
        ciclo_vertices =  [*poligono.vertices, *poligono.vertices[:2]]
        triplas_vertices = zip(ciclo_vertices, ciclo_vertices[1:], ciclo_vertices[2:])

        for indice, (vertice_anterior, vertice, vertice_posterior) in enumerate(triplas_vertices):
            vetor_1 = vertice - vertice_anterior
            vetor_2 = vertice_posterior - vertice

            produto_vetorial = vetor_1 * vetor_2
            orientacao = produto_vetorial.coord_z

            if orientacao <= 0:
                continue

            diagonal = Segmento(
                vertice_inicial=vertice_posterior,
                vertice_final=vertice_anterior
            )

            arestas_teste = arestas[:indice] + arestas[indice+3:]
            if self._checa_se_diagonal_valida(diagonal, arestas_teste):
                return Triangulo([vertice_anterior, vertice, vertice_posterior])

        assert False, "Nenhuma orelha encontrada: há algum problema no algoritmo"

    @staticmethod
    def _rotaciona_vertices(vertices: list[Ponto], indice: int) -> list[Ponto]:
        if indice <= 2:
            return vertices

        vertices_rotacionados = vertices[indice - 2:] + vertices[:indice - 2]

        return vertices_rotacionados

    @staticmethod
    def _checa_se_diagonal_valida(diagonal: Segmento, arestas: list[Segmento]) -> bool:
        for aresta in arestas:
            if diagonal.acha_intersecao(aresta):
                return False

        return True
