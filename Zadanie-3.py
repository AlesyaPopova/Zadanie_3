import networkx as nx
n = 10
p = 0.75
g = nx.erdos_renyi_graph(n, p)
a = 0
for n in g.nodes():
    a = a + g.degree(n)
    a_avr = float(a) / len(g.nodes())
    calc_avr = (n - 1)*p
    div_a = calc_avr - a_avr
    print("Средняя степень вершины фактическая: ", round(a_avr, 3))
    print("Средняя степень вершины по формуле: ", round(calc_avr, 3))
    print("Полученная разница значений: ", round(div_a, 3))


# Средняя степень вершины фактическая:  0.7
# Средняя степень вершины по формуле:  -0.75
# Полученная разница значений:  -1.45
# Средняя степень вершины фактическая:  1.3
# Средняя степень вершины по формуле:  0.0
# Полученная разница значений:  -1.3
# Средняя степень вершины фактическая:  2.0
# Средняя степень вершины по формуле:  0.75
# Полученная разница значений:  -1.25
# Средняя степень вершины фактическая:  2.8
# Средняя степень вершины по формуле:  1.5
# Полученная разница значений:  -1.3
# Средняя степень вершины фактическая:  3.6
# Средняя степень вершины по формуле:  2.25
# Полученная разница значений:  -1.35
# Средняя степень вершины фактическая:  4.3
# Средняя степень вершины по формуле:  3.0
# Полученная разница значений:  -1.3
# Средняя степень вершины фактическая:  5.0
# Средняя степень вершины по формуле:  3.75
# Полученная разница значений:  -1.25
# Средняя степень вершины фактическая:  5.6
# Средняя степень вершины по формуле:  4.5
# Полученная разница значений:  -1.1
# Средняя степень вершины фактическая:  6.4
# Средняя степень вершины по формуле:  5.25
# Полученная разница значений:  -1.15
# Средняя степень вершины фактическая:  7.0
# Средняя степень вершины по формуле:  6.0
# Полученная разница значений:  -1.0