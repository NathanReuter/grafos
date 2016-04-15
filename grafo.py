
from pprint import pprint
from colors import Bcolors

class Grafo(object):
    """docstring for Grafo"""

    global grafo
    grafo = {}

    def __init__(self):
        super(Grafo, self).__init__()

    def adicionaVertices(self, vertice):
        if (grafo.get(vertice) is not None):
            print 'Vertice ja existe' + Bcolors.ENDC
            return;

        grafo[vertice] = []

    # def removeVertice(self, vertice):
        # TODO

    def ligaArestas (self, vertice1, vertice2, bidirecional):
        if (grafo.get(vertice1) is not None and grafo.get(vertice2) is not None):
            grafo[vertice1].extend(vertice2)

            if (bidirecional):
                grafo[vertice2].extend(vertice1)

        else:
            print 'Vertice indicado nao foi passado.' + Bcolors.ENDC


    def mostraGrafo(self):
        pprint(grafo)

