from collections import deque


def bfs(graph, source, dest):    #Worst: O(M + N) where M is the number of connections and N is the number of nodes. Average: O(M + N), but depends on the size of the graph
    queue = deque()  
    visited = set()  
    parent = {source: None}
    queue.append(source)  

    while queue:  
        vertex = queue.popleft()  
        visited.add(vertex)  
        if vertex == dest:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1]

        for neighbour in graph.vertices[vertex]:  
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                queue.append(neighbour)
    return []


class Cat:
    def __init__(self, position):    #Worst: O(1) Average: O(1)
        self.position = position

    def move_towards_mouse(self, mouse, graph):    #Worst: O(M + N) where M is the number of connections and N is the number of nodes. Average: O(M + N), but depends on the size of the graph (same as the BFS function)
        queue = deque()  
        path = bfs(graph, self.position, mouse.position)
        if path and len(path) > 1:
            self.position = path[1]
            print(f"The cat is on the move! They have jumped to {self.position}")
            if self.position == mouse.position:
                mouse.game_over()
        elif path:
            mouse.game_over()


class Mouse:
    def __init__(self, position):    #Worst: O(1) Average: O(1)
        self.position = position
        self.eaten = False

    def move_mouse(self, next_position, graph):    #Worst: O(N) where N is the number of adjacent nodes. Average: O(N)
        if next_position in graph.vertices[self.position]:
            self.position = next_position
            print(f"You try to escape the cat! You have moved to {self.position}")
        else:
            print("Sorry, but the move you have tried is not possible, perhaps you should move to one of the positions which are accessible from where you are right now.")

    def game_over(self):    #Worst: O(1) Average: O(1)
        self.eaten = True
        
