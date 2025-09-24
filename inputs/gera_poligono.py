from src.dominio import Poligono, Ponto


def constroi_poligono(coordenadas_x: list[float], coordenadas_y: list[float]) -> Poligono:
    pontos = [Ponto(x,y) for x, y in zip(coordenadas_x, coordenadas_y)]
    poligono = Poligono(pontos)

    return poligono