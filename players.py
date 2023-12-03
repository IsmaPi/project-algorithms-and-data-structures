from collections import deque


def bfs(graph, source, dest):    #Best: O(1) Worst: O(M*N) where M is the number of nodes and N is the number of connections Average: Depending on the size of the graph, but it would be between O(1) and O(M*N)
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
    def __init__(self, position):    #Best: O(1) Worst: O(1) Average: O(1)
        self.position = position

    def move_towards_mouse(self, mouse, graph):    #Best: O(1) Worst: O(M*N) where M is the number of nodes and N is the number of connections Average: Depending on the size of the graph, but it would be between O(1) and O(M*N) (same as the BFS function)
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
    def __init__(self, position):    #Best: O(1) Worst: O(1) Average: O(1)
        self.position = position
        self.eaten = False

    def move_mouse(self, next_position, graph):    #Best: O(1) Worst: O(N) where N is the number of adjacent nodes Average: O(N) where N is the number of adjacent nodes
        if next_position in graph.vertices[self.position]:
            self.position = next_position
            print(f"You have moved to {self.position}")
        else:
            print("Sorry, but the move you have tried is not possible, perhaps you should move to one of the positions which are accessible from where you are right now.")

    def game_over(self):    #Best: O(1) Worst: O(1) Average: O(1)
        self.eaten = True
        print("Game over! You have been eaten by the cat! You better be more careful next time if you want to win.")
        
