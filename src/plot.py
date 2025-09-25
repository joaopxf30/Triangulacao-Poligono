import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from src.dominio import Triangulo, Poligono


def plota_triangulacao(poligono: Poligono, triangulacao: list[Triangulo]):
    fig, ax = plt.subplots()

    vertices_triangulos = []
    for vertices_triangulo in triangulacao:
        vertices = []
        for vertice_poligono in vertices_triangulo.vertices:
            vertices.append((vertice_poligono.coord_x, vertice_poligono.coord_y))

        vertices_triangulos.append(vertices)

    vertices_poligono = []
    for vertice_poligono in poligono.vertices:
        vertices_poligono.append((vertice_poligono.coord_x, vertice_poligono.coord_y))

    poligono_patch = Polygon(vertices_poligono, closed=True, edgecolor="black", facecolor="lightgray")
    ax.add_patch(poligono_patch)

    for vertices_triangulo in vertices_triangulos:
        triangulo_plot = Polygon(vertices_triangulo, closed=True, edgecolor="black", facecolor="lightcoral")
        ax.add_patch(triangulo_plot)

    xs, ys = zip(*vertices_poligono)
    ax.scatter(xs, ys, color="black", s=20, zorder=3)  # s é o tamanho da bolinha

    ax.set_title(fr"Polígono $\mathcal{{P}}_{{{len(poligono.vertices)}}}$", fontsize=12)
    ax.set_xlabel(r"$x$", fontsize=12)
    ax.set_ylabel(r"$y$", fontsize=12)

    ax.set_aspect("equal")

    plt.show()
