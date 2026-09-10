from __future__ import annotations

from pathlib import Path

from grafo.conferencia import conferir
from grafo.construcao import construir
from grafo.leitura import indexar, ler_pares
from grafo.lista import GrafoLista


def main() -> None:
    caminho = Path("dados/exemplo.edges")
    pares, relatorio = ler_pares(caminho)
    indice = indexar(pares)
    g, repetidas = construir(pares, indice, GrafoLista)
    print(relatorio)
    print({"repetidas": repetidas})
    print(conferir(g))


if __name__ == "__main__":
    main()
