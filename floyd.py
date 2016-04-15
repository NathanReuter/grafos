def floydwarshallVariante(graph):

    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = 1000     #infinito em todas as distancias
            pred[u][v] = -1       #vertices sem predecessores
        dist[u][u] = 0
        for z in graph[u]:         # preenche os vizinhos e suas distancias
            fator = random.randrange(10) #fator de variacao
            dist[u][z[0]] = z[1] * fator   #z[1] = graph[u][1] = custo
            pred[u][z[0]] = u      #z[0] = graph [u][0] = vertice vizinho

    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t
    return dist, pred

def trajetoriaAmbulancia(graph,hosp1,hosp2,emergencia){
    a={}
    a = floydwarshallVariante(graph) #chama a funcao que retorna as matrizes de custo e predecessor
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
    anterior = a[1][vencedor][emergencia]        #passo anterior do caminho mais curto
    caminho[1] = anterior
    i = 2

    while{anterior != emergencia}               #enquanto nao chega ao local, busca e adiciona o passo anterior
        caminho[i] = a[1][anterior][emergencia]
        i = i +1
    if(i < 2):                                  #caso haja passo entre os destinos
        caminho[i] = emergencia
    return custoV, caminho
}
