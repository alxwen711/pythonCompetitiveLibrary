"""
Author: alxwen711 (Alex Wen)
Last updated: August 14th, 2022

Basic graph creating structure, specifically for input format found
in most programming competitions.

The first value is the number of nodes in the graph
Then follows a series of lines with values u and v
representing an edge between two nodes.
The edges assume the nodes are being referred to as 1 to n (no node #0)


To refer to a certain node by id, this is usually done with graph[id],
where graph is a list[Node].

nodeList(n)
Creates an intial list[Node] of length n. Each node has an ID according to
their index in the list, but ar[x] will also suffice for referring to node #x.

edge(a,b)
Adds an undirected edge between two given Nodes.
"""

class Node:
    def __init__(self,ID,val = 0,colour = 0):
        self.ID = ID
        self.val = val
        self.colour = colour
        self.connected = list()

    def add(self,x):
        self.connected.append(x)

    
def nodeList(n: int) -> list[Node]:
    ar = list()
    ar.append(None)
    for i in range(1,n+1):
        ar.append(Node(i))
    return ar

def edge(a: Node, b: Node):
    a.add(b)
    b.add(a)



if __name__ == "__main__":
    #example use
    graph = nodeList(5)
    edge(graph[1],graph[3]) #edge between node 1 and 3
    edge(graph[1],graph[2]) #1 and 2
    edge(graph[4],graph[5]) #4 and 5
    edge(graph[2],graph[4]) #2 and 4
    
