#!/usr/bin/python
from grafo import Grafo
from pprint import pprint

def lerArquivo():
    f = open('config/rotas.txt')
    code = f.read()
    exec code
    f.close()
    return rotas

def floydwarshall(graph, randomFactor):

    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
    dist = {}
    pred = {}
    fator = 1

    for u in graph.keys():
        dist[u] = {}
        pred[u] = {}

        for v in graph:
            dist[u][v] = 1000     #infinito em todas as distancias
            pred[u][v] = -1       #vertices sem predecessores
        dist[u][u] = 0

        for z in graph[u]:         # preenche os vizinhos e suas distancias
            if (randomFactor):
                fator = random.randrange(10)

            dist[u][z[0]] = z[1] * 1 #z[1] = graph[u][1] = custo
            pred[u][z[0]] = u      #z[0] = graph [u][0] = vertice vizinho

    for t in graph.keys()   :
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t

    return dist, pred


rotas = lerArquivo()
pprint(floydwarshall(rotas.retornaGrafo(), False))
# trajetoriaAmbulancia(rotas, 0, 3, 7)
