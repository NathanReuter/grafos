
from pprint import pprint
from colors import Bcolors
import random

class Grafo(object):
    """docstring for Grafo"""

    global grafo
    global numeroDeArestas
    grafo = {}


    def __init__(self):
        super(Grafo, self).__init__()

    def adicionaVertices(self, vertice):
        if (grafo.get(vertice) is not None):
            return;

        grafo[vertice] = []

    def removeVertice(self, vertice):
        arestas = grafo[vertice]

        for adjacente in arestas:
            for ver in grafo[adjacente[0]]:
                if ver[0] == vertice:
                    del ver[0]
        del grafo[vertice]

    def ligaArestas (self, vertice1, vertice2, custo, bidirecional):
        if (grafo.get(vertice1) is not None and grafo.get(vertice2) is not None):
            grafo[vertice1].append([vertice2, custo])

            if (bidirecional):
                grafo[vertice2].append([vertice1, custo])

        else:
            print 'Vertice indicado nao foi passado.' + Bcolors.ENDC

    # TODO DESCONECTA
    def desconecta(self, vertice1, vertice2, bidirecional):
        for aresta in enumerate(grafo[vertice1]):
            if (aresta[1][0] == vertice2):
                del grafo[vertice1][aresta[0]]

        if (bidirecional):
            self.desconecta(vertice2, vertice1, False)

    def ordem(self):
        return len(grafo.keys())

    def numeroDeArestas(self):
        return numeroDeArestas

    def mostraGrafo(self):
        pprint(grafo)

    # TODO umVertice
    def umVertice(self):
        return grafo[random.randrange(self.ordem())]

    def adjacentes(self, vertice):
        return grafo[vertice]

    def grau(self, vertice):
        return len(self.adjacentes(vertice))

    # vertices
    def retornaGrafo(self):
        return grafo

