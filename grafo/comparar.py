from __future__ import annotations

from pathlib import Path

from grafo.construcao import construir
from grafo.conferencia import conferir
from grafo.leitura import indexar, ler_pares
from grafo.lista import GrafoLista


def main() -> None:
    try:
        import networkx as nx
    except ModuleNotFoundError as exc:
        raise SystemExit("NetworkX não está instalado; instale a dependência opcional para comparar.") from exc

    from grafo.triangulos import contar_triangulos

    arestas = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    proprio = GrafoLista(5)
    for u, v in arestas:
        proprio.inserir_aresta(u, v)

    referencia = nx.Graph()
    referencia.add_nodes_from(range(5))
    referencia.add_edges_from(arestas)

    print("ordem", proprio.ordem(), referencia.number_of_nodes())
    print("tamanho", proprio.tamanho(), referencia.number_of_edges())
    print("triangulos", contar_triangulos(proprio), sum(nx.triangles(referencia).values()) // 3)

    pares, relatorio = ler_pares(Path("dados/exemplo.edges"))
    indice = indexar(pares)
    g, repetidas = construir(pares, indice, GrafoLista)
    print(relatorio)
    print({"repetidas": repetidas})
    print(conferir(g))


if __name__ == "__main__":
    main()
