class Graph:
    def __init__(self):    #Worst: O(1) Average: O(1)
        self.vertices = {}

    def add_vertex(self, vertex):    #Worst: O(N) N being the number of nodes if there are collisions Average: O(1)
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, a, b):    #Worst: O(N) in case there are collisions Average: O(1)
        self.add_vertex(a)
        self.add_vertex(b)
        if b not in self.vertices[a]:
            self.vertices[a].append(b)
        if a not in self.vertices[b]:
            self.vertices[b].append(a)

    def add_edges(self, *args):    #Worst: O(M*N)  M being a connection between nodes. We assume that the add_edge has worst time complexity O(N) Average: O(M)
        for a, b in args:
            self.add_edge(a, b)

    def print(self, cat_position, mouse_position):    #Worst: O(N + M) Average: O(N + M) All cases have the same complexity since the nodes and connections are traversed only once
        for k, v in self.vertices.items():
            cat_symbol = " C" if k == cat_position else " "
            mouse_symbol = "M" if k == mouse_position else " "
            
            print(f'[{k}{cat_symbol}{mouse_symbol}] -> {v}')
