from __future__ import annotations

from typing import Iterable

from grafo.base import Grafo


class GrafoIncidencia(Grafo):
    def __init__(self, n: int) -> None:
        self._n = n
        self._arestas: list[tuple[int, int]] = []
        self._inc: list[list[int]] = [[] for _ in range(n)]

    def ordem(self) -> int:
        return self._n

    def tamanho(self) -> int:
        return len(self._arestas)

    def vizinhos(self, v: int) -> Iterable[int]:
        return iter(self._inc[v])

    def tem_aresta(self, u: int, v: int) -> bool:
        return v in self._inc[u]

    def inserir_aresta(self, u: int, v: int) -> None:
        if u == v:
            raise ValueError("laço não é permitido em grafo simples")
        if v in self._inc[u]:
            return
        self._arestas.append((u, v))
        self._inc[u].append(v)
        self._inc[v].append(u)

    def espaco(self) -> int:
        return self._n * self.tamanho()
