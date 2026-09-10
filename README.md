# Grafo em Python

Versão em Python da implementação do capítulo sobre representação de grafos.

O pacote inclui:

- `GrafoMatriz` e `GrafoLista`
- `GrafoIncidencia`
- contagem de triângulos
- leitura de arquivo em formato de lista de arestas
- construção com tradução de rótulos
- conferência do grafo lido
- teste unitário com `n=5` e `m=6`
- benchmark com `n=2000` e densidades `0.001`, `0.05` e `0.5`

## Estrutura

- `grafo/`: pacote principal
- `dados/`: arquivo de exemplo para leitura
- `tests/`: teste mínimo pedido no enunciado
- `tools/`: benchmark e comparação auxiliar

## Execução

```powershell
py -m unittest tests.teste_unitario
python -m tools.benchmark
python -m grafo.pipeline
```

O benchmark denso pode ser pesado para Python porque `n=2000` e densidade `0.5` produzem aproximadamente um milhão de arestas. A contagem de triângulos foi otimizada com orientação por grau e interseção de vizinhanças, mas ainda é recomendável validar primeiro com:

```powershell
py -m tools.benchmark --n 200 --repeticoes 1
```

Para a medição exigida na atividade, use os valores padrão, que executam três repetições:

```powershell
py -m tools.benchmark --n 2000 --repeticoes 3
```

Também é possível medir uma densidade por vez:

```powershell
py -m tools.benchmark --n 2000 --densidades 0.001 --repeticoes 3
py -m tools.benchmark --n 2000 --densidades 0.05 --repeticoes 3
py -m tools.benchmark --n 2000 --densidades 0.5 --repeticoes 3
```

```powershell
py -m unittest discover -s TG\grafo_repr_py\tests -t TG\grafo_repr_py -v
```

No `unittest`, use pontos (`tests.teste_unitario`) para indicar módulos Python; não use barras nem o sufixo `.py`.
Se quiser comparar com NetworkX, instale a dependência opcional antes de rodar `grafo.comparar`.

Itens:

1. Estão implementadas em: 
    grafo/matriz.py
    grafo/lista.py

2. Teste n=5, m=6

    Execute:

        py -m unittest tests.teste_unitario -v

    Saída esperada:

        Ran 1 test ... OK

    O teste verifica ordem, tamanho, graus, soma dos graus e triângulos.

3. Matriz de incidência:

    A matriz da figura 3.1 se dá da seguinte forma:

      e1 e2 e3 e4 e5 e6
    v1 1  1  0  0  0  0
    v2 1  0  1  1  0  0
    v3 0  1  1  0  1  0
    v4 0  0  0  1  0  1
    v5 0  0  0  0  1  1

    Cada coluna soma 2 e as linhas somam: {2, 3, 3, 2, 2}

4 e 5. Grafos aleatórios, tempo e espaço:

    Execute: 
        py -m tools.benchmark

    O programa gera grafos com n = 2000; densidades = 0.001, 0.05, 0.5.
    Para cada representação, ele informa:

        °quantidade de arestas;
        °tempo mediano de 3 execuções;
        °espaço da matriz: n²;
        °espaço da lista: n + 2m.
    
    Você pode salvar o resultado: py -m tools.benchmark > resultados.txt

6. Análise:

    A Lista de Adjacência venceu em todas as densidades. Em grafos extremamente esparsos (delta = 0,001), a lista foi cerca de 92 vezes mais rápida (0,0026s vs 0,2417s). Isso ocorre porque o algoritmo contar_triangulos na matriz itera sobre trios de vértices checando posições vazias (custo dominado por O(n^3)), enquanto a lista percorre exclusivamente vizinhanças reais, cujo custo é limitado pelo grau dos vértices. 

    Variação da ordem com o aumento da densidade: A ordem de eficiência não se inverteu, mas a vantagem relativa da lista caiu drasticamente. À medida que a densidade saltou de 0,001 para 0,5, o número de arestas subiu de 1.979 para 998.464. Com metade de todas as conexões possíveis existentes, percorrer as listas de adjacência passou a exigir quase a mesma quantidade de checagens que varrer a matriz inteira, fazendo os tempos de execução convergirem para a faixa dos 15s.

    Concordância com o custo teórico composto: Os dados medidos concordam totalmente com a teoria.  
    
        Espaço: O consumo da matriz permaneceu cravado em n^2 = 4.000.000 em todas as rodadas, provando sua ineficiência de memória para grafos esparsos. A lista escalou exatamente de forma linear n + 2m (5.958 para 0,001 até 1.998.928 para 0,5).  
        
        Tempo: Na lista, quando $m$ cresceu por um fator de aproximadamente 50 (de 1.979 para 99.475), o tempo subiu por um fator de aproximadamente 76 (de 0,0026s para 0,2014s), refletindo a dependência direta do grau médio e do número de arestas na checagem de triângulos. Na matriz, o tempo inicial manteve o custo base de varrer a estrutura n X n, aumentando fortemente apenas quando a quantidade massiva de acessos à memória cache impactou o processamento em delta = 0,5.

7. Leitura e conferência: 
