#!/usr/bin/python
from grafo import Grafo

def lerArquivo():
    f = open('config/rotas.txt')
    code = f.read()
    exec code
    f.close()
    return rotas

rotas = lerArquivo()
rotas.removeVertice('A')
rotas.mostraGrafo()


