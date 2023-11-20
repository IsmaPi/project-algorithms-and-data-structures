# This is the graph class to generate the playing space for the cat and mouse game.

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        if b not in self.vertices[a]:
            self.vertices[a].append(b)

    def add_edges(self, *args):
    # args = [('A', 'B'), ('B', 'C'), ...]
        for a, b in args:
            self.add_edge(a, b)

    def print(self):
        for k, v in self.vertices.items():
            print(f'{k} -> {v}')

