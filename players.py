# Here the class for both the cat (algorithm chasing the mouse) and the mouse (the player that is chased by the cat) is defined. For the cat, it uses a breadth-first search algorithm to find the shortest path to the mouse. The mouse can move to any of the nodes that are accessible from its current position. The cat wins if it catches the mouse, and the mouse wins if it is not caught after a certain ammount of moves.
from collections import deque
from graph import Graph

def bfs(graph, source, dest):
    queue = deque()  
    visited = set()  
    parent = {source: None}  # Dictionary to keep track of the path being currently explored by the cat
    queue.append(source)  

    while queue:  
        vertex = queue.popleft()  
        visited.add(vertex)  
        if vertex == dest:  
            # Reconstruct the path from source to dest
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1]

        for neighbour in graph.vertices[vertex]:  
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex  # Set the parent of the neighbour
                queue.append(neighbour)
    return []

class Cat:
    def __init__(self, position):
        self.position = position

    def move_towards_mouse(self, mouse, graph):
        path = bfs(graph, self.position, mouse.position)
        if path and len(path) > 1:
            # Move towards the mouse in the case thay the path is not empty and the path is longer than one node (if the path is empty it means that the mouse has been caught and if the path is one node long it means that the cat will move to the mouse node and catch it)
            self.position = path[1]
            print(f"The cat is on the move! They have jumped to {self.position}")
            if self.position == mouse.position:
                mouse.game_over()
        elif path:
            mouse.game_over()


class Mouse:
    def __init__(self, position):
        self.position = position

    def move_mouse(self, next_position, graph):
        if next_position in graph.vertices[self.position]:
            self.position = next_position
        else:
            print("Sorry, but the move you have tried is not possible, pehaps you should move to one of the positions which are accessible from where you are right now.")

    def game_over(self):
        self.eaten = True
        print("Game over! You have been eaten by the cat! You better be more careful next time if you want to win.")