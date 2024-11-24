# CLRS P6 C20 Graph Breadth first search

from dataclasses import dataclass
from enum import Enum
from collections import deque

class Color(enum):
    WHITE
    GERY
    BLACK

@dataclass
class Vertex:
    p: Vertex
    d: int
    c: Color 
    key: str

# type AdjacencyList = list[list[Vertex]]

InfiniteDistance = -1

def BFS(G: dict[Vertex, list[Vertex]], s: Vertex) -> None:
    for l in G:
        for j in l:
            j.p = None; j.d = InfiniteDistance; j.c = Color.WHITE

    s.p = None; s.d = 0; s.c = Color.GREY
    q = deque()
    q.append(s)

    while not q.empty():
        u = q.popleft()
        for v in G[u]:
            if v.c is Color.WHITE:
                v.d = u.d + 1
                v.c = Color.GREY
                v.p = u
                q.append(v)
        u.c = Color.BLACK

def print_path(s: Vertex, v: Vertex) -> None:
    if v is s:
        print(s)
    elif v.p is None:
        print('No path from "s" to "v" exists')
    else:
        print_path(s, v.p)
        print(v)

