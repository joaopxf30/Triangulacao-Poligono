from src.dominio import Ponto, Poligono


if __name__ == "__main__":
    coordenadas_x = [-1, 0, -1, -2, 2, 1, 2, 0, -1]
    coordenadas_y = [-1, 0, -1, 0, -1, 0, 1, 2, 2]

    pontos = [Ponto(x,y) for x, y in zip(coordenadas_x, coordenadas_y)]
    poligono = Poligono(pontos)

    print(pontos)

