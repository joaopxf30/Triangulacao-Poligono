from inputs import poligonos
from src.plot import plota_triangulacao
from src.remocao_orelha import RemocaoOrelha


def triangularizacao_por_remocao_orelha():
    algoritmo_remocao_orelha = RemocaoOrelha()
    for poligono in poligonos:
        triangulacao = algoritmo_remocao_orelha.realiza_triangulacao(poligono)
        plota_triangulacao(poligono, triangulacao)


if __name__ == "__main__":
    triangularizacao_por_remocao_orelha()
