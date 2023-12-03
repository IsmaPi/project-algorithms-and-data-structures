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
        if a not in self.vertices[b]:
            self.vertices[b].append(a)

    def add_edges(self, *args):
        # args = [('A', 'B'), ('B', 'C'), ...]
        for a, b in args:
            self.add_edge(a, b)

    def print(self, cat_position, mouse_position):
        for k, v in self.vertices.items():
            if k == cat_position:
                cat_symbol = "C" 
            else: 
                " "
            if k == mouse_position:
                mouse_symbol = "M"
            else:
                " " 
            cat_symbol = "C" if k == cat_position else " "
            mouse_symbol = "M" if k == mouse_position else " "
            
            print(f'[{k}{cat_symbol}{mouse_symbol}] -> {v}')
