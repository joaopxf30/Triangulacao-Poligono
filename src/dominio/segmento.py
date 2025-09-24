from src.dominio.ponto import Ponto
from src.dominio.vetor import Vetor


class Segmento:
    def __init__(self, vertice_inicial: Ponto, vertice_final: Ponto):
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.ordenamento: Vetor = vertice_final - vertice_inicial

    def acha_intersecao(self, segmento: "Segmento") -> bool:
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

        if 0 == orientacoes[0]:
            return self._determina_tangenciamento(segmento.vertice_inicial)

        if 0 == orientacoes[1]:
            return self._determina_tangenciamento(segmento.vertice_final)

        else:
            return False

    @staticmethod
    def _determina_cruzamento(orientacoes: list[float]) -> bool:
        return (
            orientacoes[0] * orientacoes[1] < 0
            and orientacoes[2] * orientacoes[3] < 0
        )

    def _determina_tangenciamento(
        self,
        vertice: "Ponto",
    ) -> bool:
        if abs(self.ordenamento.coord_x) > abs(self.ordenamento.coord_y):
            return (
                    min(self.vertice_inicial.coord_x, self.vertice_final.coord_x)
                    < vertice.coord_x <
                    max(self.vertice_inicial.coord_x, self.vertice_final.coord_x)
            )

        else:
            return (
                    min(self.vertice_inicial.coord_y, self.vertice_final.coord_y)
                    < vertice.coord_y <
                    max(self.vertice_inicial.coord_y, self.vertice_final.coord_y)
            )
