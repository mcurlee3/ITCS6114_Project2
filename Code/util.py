from collections import defaultdict
import sys
import time
import pandas as pd
from Dykstra import dGraph
from Kruskal import kGraph
from Connected import cGraph

def parseText(txtFile):
    lst = []
    for line in txtFile:
        x = line.split()
        lst.append(x)
    stats = lst.pop(0)
    src = lst.pop()
    lst = [lst, stats, src]
    return lst

def printDykstra():
    print('###-------------Dykstra---------------###')
    file1 = open('samp1.txt', 'r')
    file2 = open('samp2.txt', 'r')
    file3 = open('samp3.txt', 'r')
    file4 = open('samp4.txt', 'r')

    file1 = parseText(file1)
    file2 = parseText(file2)
    file3 = parseText(file3)
    file4 = parseText(file4)

    sample = [file1, file2, file3, file4]
    for file in sample:
        start = file.pop()
        start = start[0]
        stats = file.pop()
        file = file[0]

        if stats[2] == 'D':
            directed = True
            dir = 'Directed'
        else:
            directed = False
            dir = 'Undirected'
        graph = dGraph(directed)
        for l in file:
            graph.addEdge(l[0], l[1], int(l[2]))
        print('Starting node for this ' + dir + ' graph is: ' + start)
        startTime = time.time()
        parent, dist = graph.Dikstra(start)

        graph.printSolution(dist, parent, start)
        runTime = (time.time() - startTime)*1000

        print('The runtime for this graph took: ', runTime, ' microseconds.')
        print('************************************************************')
        print()

def printKruskal():
    print('###------------Kruskal----------------###')
    file1 = open('samp1.txt', 'r')
    file2 = open('samp2.txt', 'r')
    file3 = open('samp3.txt', 'r')
    file4 = open('samp4.txt', 'r')

    file1 = parseText(file1)
    file2 = parseText(file2)
    file3 = parseText(file3)
    file4 = parseText(file4)

    sample = [file1, file2, file3, file4]
    for file in sample:
        start = file.pop()
        start = start[0]
        stats = file.pop()
        file = file[0]
        numVert = stats[0]
        graph = kGraph(numVert)
        for l in file:
            graph.addEdge(ord(l[0])-65, ord(l[1])-65, int(l[2]))
        start_time = time.time()
        graph.KruskalMST()

        runtime = (time.time() - start_time) * 1000

        print('The runtime for this graph took: ', runtime, ' microseconds')
        print('***********************************************************')
        print()

def printConnected():
    print('###------------Connected----------------###')
    file1 = open('samp1.txt', 'r')
    file2 = open('samp2.txt', 'r')
    file3 = open('samp3.txt', 'r')
    file4 = open('samp4.txt', 'r')

    file1 = parseText(file1)
    file2 = parseText(file2)
    file3 = parseText(file3)
    file4 = parseText(file4)

    sample = [file1, file2, file3, file4]
    for file in sample:
        start = file.pop()
        start = start[0]
        stats = file.pop()
        file = file[0]
        numVert = stats[0]
        graph = cGraph(int(numVert))
        start_time = time.time()
        for l in file:
            graph.addEdge(ord(l[0])-65, ord(l[1])-65)
        print('The following nodes are strongly connected.')
        graph.printSCCs()
        runtime = (time.time() - start_time) * 1000

        print('The runtime for this graph took: ', runtime, ' microseconds')
        print('***********************************************************')
        print()

