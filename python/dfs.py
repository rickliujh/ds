# CLRS P6 C20.3 Graph Depth first search

from dataclasses import dataclass
from enum import Enum
from collections import deque

class Color(enum):
    WHITE
    GERY
    BLACK

class DirectedEdgeType(enum):
    TREE
    BACK
    FORDARD
    CROSS

class UndirectedEdgeType(enum):
    TREE
    BACK

@dataclass
class Vertex:
    p: Vertex
    d: int # discovery timestamp
    f: int # finish timestamp
    c: Color 
    key: str

class Time:
    ts: int
    def increase(self):
       self.ts += 1 
    def timestamp():
        return ts

def DFS(G: dict[Vertex, list[Vertex]]) -> None:
    for i in G:
        for j in i:
            j.p = None; j.d = InfiniteDistance; j.f = InfiniteDistance; j.c = Color.WHITE
    time = Time(0)
    for i in G:
        if i.c is Color.WHITE:
            DFS_visit(G, i, time)

def DFS_visit(G: dict[Vertex, list[Vertex]], u: Vertex, t: Time) -> None:
    t.increase()
    u.d = t.timestamp()
    u.c = Color.GREY

    for v in G[u]:
        if v.c is Color.WHITE:
            v.p = u
            DFS_visit(G, v, t)

    t.increase()
    u.f = t.timestamp()
    u.c = Color.BLACK
    
def DFS_edge_type(u: Vertex, v: Vertex) -> DirectedEdgeType:
    if v.c is Color.WHITE:
        return DirectedEdgeType.TREE
    if v.c is Color.GREY:
        return DirectedEdgeType.BACK
    if v.c is Color.BLACK:
        if u.d < v.d:
            return DirectedEdgeType.FORDARD
        elif u.d > v.d:
            return DirectedEdgeType.CROSS
    
def DFS_edge_type_undirected_graph(u: Vertex, v: Vertex) -> DirectedEdgeType:
    if v.c is Color.WHITE:
        return DirectedEdgeType.TREE
    else:
        return DirectedEdgeType.BACK
    
