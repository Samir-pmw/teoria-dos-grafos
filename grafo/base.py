from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable


class Grafo(ABC):
    """Grafo simples não orientado com vértices 0, 1, ..., n-1."""

    @abstractmethod
    def ordem(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def tamanho(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def vizinhos(self, v: int) -> Iterable[int]:
        raise NotImplementedError

    @abstractmethod
    def tem_aresta(self, u: int, v: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def inserir_aresta(self, u: int, v: int) -> None:
        raise NotImplementedError

    def vertices(self) -> Iterable[int]:
        return range(self.ordem())

    def grau(self, v: int) -> int:
        return sum(1 for _ in self.vizinhos(v))
