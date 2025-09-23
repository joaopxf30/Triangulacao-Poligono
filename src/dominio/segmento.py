from src.dominio import Ponto, Vetor


class Segmento:
    def __init__(self, vertice_inicial: Ponto, vertice_final: Ponto):
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.orientacao: Vetor = vertice_final - vertice_inicial

    def detecta_cruzamento(self, segmento: "Segmento") -> bool:
        vetor_1 = segmento.vertice_inicial - self.vertice_inicial
        vetor_2 = segmento.vertice_final - self.vertice_inicial
        produto_vetorial_1 = segmento.orientacao.calcula_produto_vetorial(vetor_1)
        produto_vetorial_2 = segmento.orientacao.calcula_produto_vetorial(vetor_2)

        vetor_3 = self.vertice_inicial - segmento.vertice_inicial
        vetor_4 = self.vertice_final - segmento.vertice_inicial
        produto_vetorial_3 = segmento.orientacao.calcula_produto_vetorial(vetor_3)
        produto_vetorial_4 = segmento.orientacao.calcula_produto_vetorial(vetor_4)

        if (
            produto_vetorial_1.coord_z * produto_vetorial_2.coord_z < 0
            and ...
        ):
            return True

        return False
