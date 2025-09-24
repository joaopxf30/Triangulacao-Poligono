from src.dominio.ponto import Ponto
from src.dominio.vetor import Vetor


class Segmento:
    def __init__(self, vertice_inicial: Ponto, vertice_final: Ponto):
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.ordenamento: Vetor = vertice_final - vertice_inicial

    def determina_intersecao(self, segmento: "Segmento") -> bool:
        orientacoes = []

        vetor_1 = segmento.vertice_inicial - self.vertice_inicial
        vetor_2 = segmento.vertice_final - self.vertice_inicial
        vetor_3 = self.vertice_inicial - segmento.vertice_inicial
        vetor_4 = self.vertice_final - segmento.vertice_inicial

        orientacoes.append(self.ordenamento.calcula_produto_vetorial(vetor_1).coord_z)
        orientacoes.append(self.ordenamento.calcula_produto_vetorial(vetor_2).coord_z)
        orientacoes.append(segmento.ordenamento.calcula_produto_vetorial(vetor_3).coord_z)
        orientacoes.append(segmento.ordenamento.calcula_produto_vetorial(vetor_4).coord_z)

        if self._determina_cruzamento(orientacoes):
            return True

        if orientacoes[0] == 0 and self._determina_tangenciamento(
            vertice_extremidade_1=self.vertice_inicial,
            vertice_extremidade_2=self.vertice_final,
            vertice_analise=segmento.vertice_inicial,
        ):
            return True

        if orientacoes[1] == 0 and self._determina_tangenciamento(
            vertice_extremidade_1=self.vertice_inicial,
            vertice_extremidade_2=self.vertice_final,
            vertice_analise=segmento.vertice_final,
        ):
            return True

        if orientacoes[2] == 0 and self._determina_tangenciamento(
            vertice_extremidade_1=segmento.vertice_inicial,
            vertice_extremidade_2=segmento.vertice_final,
            vertice_analise=self.vertice_inicial
        ):
            return True

        if orientacoes[3] == 0 and self._determina_tangenciamento(
            vertice_extremidade_1=segmento.vertice_inicial,
            vertice_extremidade_2=segmento.vertice_final,
            vertice_analise=self.vertice_final
        ):
            return True

        return False

    @staticmethod
    def _determina_cruzamento(coordenadas_z: list[float]) -> bool:
        return (
            coordenadas_z[0] * coordenadas_z[1] < 0
            and coordenadas_z[2] * coordenadas_z[3] < 0
        )

    @staticmethod
    def _determina_tangenciamento(
        vertice_extremidade_1: Ponto,
        vertice_extremidade_2: Ponto,
        vertice_analise: Ponto
    ) -> bool:
        tangenciamento_coord_x = (
                min(vertice_extremidade_1.coord_x, vertice_extremidade_2.coord_x)
                <= vertice_analise.coord_x
                <= max(vertice_extremidade_1.coord_x, vertice_extremidade_2.coord_x)
        )

        tangenciamento_coord_y = (
                min(vertice_extremidade_1.coord_y, vertice_extremidade_2.coord_y)
                <= vertice_analise.coord_y
                <= max(vertice_extremidade_1.coord_y, vertice_extremidade_2.coord_y)
        )

        return tangenciamento_coord_x and tangenciamento_coord_y
