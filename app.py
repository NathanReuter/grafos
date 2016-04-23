#!/usr/bin/python
from grafo import Grafo
from pprint import pprint
import random

grafoDeRotas = Grafo()
global hospital1
global hospital2


def lerArquivo():
    f = open('config/ambulan2.dat')
    code = f.read()
    exec code
    f.close()
    return arestas

def montaGrafo(grafo, grafoEmLista, temHospitais):
    for index, aresta in enumerate(grafoEmLista):
        if ((not temHospitais) or (index < len(grafoEmLista) - 2)):
            grafo.adicionaVertices(aresta[0])
            grafo.adicionaVertices(aresta[1])
            grafo.ligaArestas(aresta[0], aresta[1], aresta[2], True)

    if(temHospitais):
        global hospital1
        global hospital2
        hospital1 = grafoEmLista[len(grafoEmLista) - 1][0]
        hospital2 = grafoEmLista[len(grafoEmLista) - 1][1]

def floydwarshall(graph, randomFactor):
    dist = {}
    pred = {}
    fator = 1

    for u in graph.keys():
        dist[u] = {}
        pred[u] = {}

        for v in graph:
            dist[u][v] = 1000     #infinito em todas as distancias
            pred[u][v] = -1#vertices sem predecessores

        dist[u][u] = 0

        for z in graph[u]:         # preenche os vizinhos e suas distancias
            if (randomFactor):
                fator = random.randrange(10)

            dist[u][z[0]] = z[1] * 1 #z[1] = graph[u][1] = custo
            pred[u][z[0]] = u      #z[0] = graph [u][0] = vertice vizinho

    for t in graph.keys():
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v]

    return dist, pred


def trajetoriaAmbulancia(graph, hosp1, hosp2, emergencia):

   a = floydwarshall(graph, True) #chama a funcao que retorna as matrizes de custo e predecessor

   pprint(a)

   custo1 = a[0][hosp1][emergencia] #custo do hospital 1 a emergencia
   custo2 = a[0][hosp2][emergencia] #custo do hospital 2 a emergencia

   if (custo1 > custo2):             #verifica o menor custo
       vencedor = hosp2
       custoV = custo2
   else:
       vencedor = hosp1
       custoV = custo1

   caminho = {}
   caminho[0] = vencedor
   anterior = a[1][emergencia][vencedor]        #passo anterior do caminho mais curto
   caminho[1] = anterior
   i = 2
   while (anterior != emergencia):               #enquanto nao chega ao local, busca e adiciona o passo anterior
       caminho[i] = a[1][emergencia][anterior]
       anterior = caminho [i]
       i = i +1

   return custoV, caminho

def bonitificador(custo, caminho):
    string = ''
    for index, v in enumerate(caminho.keys()):
        if (index < len(caminho.keys()) - 1):
            string = string + str(caminho[v]) + ' -> '
        else:
            string = string + str(caminho[v])
    print 'Custo: ', custo
    print 'Caminho: ', string

def buscarMelhorRota(emergencia):
    rotas = lerArquivo()
    montaGrafo(grafoDeRotas, rotas, True)
    resp = trajetoriaAmbulancia(grafoDeRotas.retornaGrafo(), hospital1, hospital2, emergencia)
    bonitificador(resp[0], resp[1])

buscarMelhorRota(6)

