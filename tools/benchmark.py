from __future__ import annotations

import random
import statistics
import time
import argparse

from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz
from grafo.triangulos import contar_triangulos


def gerar_grafo(n: int, densidade: float, seed: int):
    random.seed(seed)
    g_m = GrafoMatriz(n)
    g_l = GrafoLista(n)
    m = 0
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < densidade:
                g_m.inserir_aresta(u, v)
                g_l.inserir_aresta(u, v)
                m += 1
    return g_m, g_l, m


def medir(nome: str, n: int, densidade: float, repeticoes: int) -> None:
    g_m, g_l, m = gerar_grafo(n, densidade, 12345)
    tm = mediana_tres(lambda: contar_triangulos(g_m), repeticoes)
    tl = mediana_tres(lambda: contar_triangulos(g_l), repeticoes)
    print(nome)
    print(f"  n={n} m={m} densidade={densidade:.3f}")
    print(f"  matriz: tempo_mediano={tm:.6f} s espaco={g_m.espaco()}")
    print(f"  lista : tempo_mediano={tl:.6f} s espaco={g_l.espaco()}")


def mediana_tres(funcao, repeticoes: int = 3):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        funcao()
        tempos.append(time.perf_counter() - inicio)
    return statistics.median(tempos)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=2000)
    parser.add_argument("--densidades", nargs="+", type=float, default=[0.001, 0.05, 0.5])
    parser.add_argument("--repeticoes", type=int, default=3)
    args = parser.parse_args()

    for densidade in args.densidades:
        medir(f"densidade {densidade}", args.n, densidade, args.repeticoes)


if __name__ == "__main__":
    main()
