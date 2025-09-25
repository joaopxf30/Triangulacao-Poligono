# Triangulação de polígonos

Este projeto implementa o algoritmo por remoção de orelhas para realizar a triangulação de um polígono simples.
A versão utilizada para desenvolvimento é Python 3.12.3.

---
## Ambientes virtuais

É fortemente recomendado a utilização de ambientes virtuais. Para tal, execute no terminal a partir de um path desejado o seguinte comando de acordo com o sistema operacional:

**WINDOWS**:
```
python -m venv env
```

**OS/LINUX**:
```
python3 -m venv env
```

Para ativação do ambiente virutal, execute o seguinte comando de acordo com a platafoma:

**WINDOWS**:
```
<path>\env\Scripts\Activate.ps1
```

**POSIX**:
```
source <path>/env/bin/activate
```

O ambiente virtual será criado.

## Instalando dependências

Todas as dependências do projeto se encontram no arquivo `requirements.txt`. A obtenção é feita a partir da execução do seguinte comando na raiz do projeto:

```
pip install -r requirements.txt
```

As dependências são instaladas.

## Recomendações de uso

Para acionar o código basta rodar da raiz do projeto

```
python main.py
```

O código realizará a triangulação através do algoritmo por remoção de orelha para cada instância da classe `Poligono`
presente na lista `poligonos`. 

```python
def triangularizacao_por_remocao_orelha():
    algoritmo_remocao_orelha = RemocaoOrelha()
    for poligono in poligonos:
        triangulacao = algoritmo_remocao_orelha.realiza_triangulacao(poligono)
        plota_triangulacao(poligono, triangulacao)
```

Além disso, o plot de cada um das triangulações é apresentado.

As instâncias de polígono usadas como *input* se encontram no pacote `/input` e estão
cada uma em um arquivo python nominado `poligono_<contador>.py`. Exemplo de arquivo:

```python
from input.gera_poligono import constroi_poligono

COORDENADAS_X = [-1, -1, -1, 0, 0, 1, 4, 3, 1, 0, 1, 2, 2, 0]
COORDENADAS_Y = [1, -1, -2, -1, -3, -2, -1, 0, -1, 0, 1, 0, 2, 2]


poligono_3 = constroi_poligono(COORDENADAS_X, COORDENADAS_Y)
```

Para uma nova instância, basta criar um novo arquivo `poligono_<contador>.py`, definir as coordenadas cartesianas
x e y de cada um dos pontos do polígono nas constantes `COORDENADAS_X` e `COORDENADAS_Y`. Chamar a função 
`constroi_poligono(coordenadas_x: list[float], coordenadas_y: list[float]) -> Poligono:` e atribuir uma varíável
para o retorno.

Ainda é necessário adicionar essa varíavel à lista `poligonos` que fica presente no inicializador `__init__.py` do pacote
`\input`:

```python
from .poligono_1 import poligono_1
from .poligono_2 import poligono_2
from .poligono_3 import poligono_3

poligonos = [
    poligono_1,
    poligono_2,
    poligono_3,
]
```


