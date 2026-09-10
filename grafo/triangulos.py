from __future__ import annotations

from grafo.base import Grafo


def contar_triangulos(g: Grafo) -> int:
    """Conta triângulos usando orientação por grau para reduzir o trabalho."""
    vizinhancas = {v: set(g.vizinhos(v)) for v in g.vertices()}
    ordem = {
        v: (len(vizinhancas[v]), v)
        for v in g.vertices()
    }
    orientada: dict[int, set[int]] = {v: set() for v in g.vertices()}

    for u in g.vertices():
        for v in vizinhancas[u]:
            if ordem[u] < ordem[v]:
                orientada[u].add(v)

    total = 0
    for u in g.vertices():
        for v in orientada[u]:
            total += len(orientada[u] & orientada[v])
    return total
