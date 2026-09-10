from __future__ import annotations

import unittest

from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz
from grafo.triangulos import contar_triangulos


def _montar_grafo(classe):
    g = classe(5)
    arestas = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
    for u, v in arestas:
        g.inserir_aresta(u, v)
    return g


class TesteGrafo(unittest.TestCase):
    def test_grafo_matriz_e_lista(self) -> None:
        esperado_graus = [2, 3, 3, 3, 1]

        for classe in (GrafoLista, GrafoMatriz):
            with self.subTest(representacao=classe.__name__):
                g = _montar_grafo(classe)
                self.assertEqual(g.ordem(), 5)
                self.assertEqual(g.tamanho(), 6)
                graus = [g.grau(v) for v in g.vertices()]
                self.assertEqual(graus, esperado_graus)
                self.assertEqual(sum(graus), 12)
                self.assertEqual(contar_triangulos(g), 2)


if __name__ == "__main__":
    unittest.main()
