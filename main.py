from graph import Graph
from players import Cat, Mouse, bfs
import random


def is_min_distance_sufficient(graph, start, end, min_distance=3):    #Worst O(N + M) where N is the nodes and M is the connections Average O(N + M)
    path = bfs(graph, start, end)
    return len(path) >= min_distance


def set_starting_positions(graph):    #Worst O(N + M)* K where N is the nodes, M is the connections, and K is how many times the loop has to iterate through creating new pairs of starting locations Average O(N + M)* K where k in the average number of iterations
    positions = list(graph.vertices.keys())
    position_cat = random.choice(positions)
    positions.remove(position_cat)
    position_mouse = random.choice(positions)

    while not is_min_distance_sufficient(graph, position_cat, position_mouse):
        positions.append(position_mouse)
        position_mouse = random.choice(positions)
        positions.remove(position_mouse)

    return position_cat, position_mouse


def main():    #Worst: O(moves * (N + M + P)) Where moves are the number of moves, N is the number of nodes, M is the number of connections, and P is the number of adjacent nodes from the node the player is in. Average: O(moves * (N + M + P))
    graph = Graph()
    graph.add_edges(    #Worst O(N) Average O(N) Where N is the number of nodes
        (1, 2), (2, 3), (3, 4),
        (4, 5), (5, 6), (6, 7),
        (7, 8), (8, 1), (1, 5),
        (2, 6), (3, 7), (4, 8),
        (9, 10), (10, 11), (11, 12),
        (12, 13), (13, 14), (14, 15),
        (15, 9), (9, 12), (10, 13),
        (11, 14), (1, 9), (2, 10),
        (3, 11), (4, 12), (5, 13),
        (6, 14), (7, 15), (8, 9)
    )

    position_cat, position_mouse = set_starting_positions(graph)
    cat = Cat(position_cat)
    mouse = Mouse(position_mouse)

    moves = 10
    for move in range(1, moves + 1):
        print(f"\nMove: {moves}")
        moves -= 1

        cat.move_towards_mouse(mouse, graph)
        
        if mouse.eaten:
            print("You have been eaten by the cat! You better be more careful next time if you want to win.")
            break

        print("\nMouse's turn:")
        print("Current graph:")
        graph.print(cat.position, mouse.position)

        valid_move = False
        while not valid_move:
            try:
                next_position = int(input("Enter where you want to move next: "))
                if next_position in graph.vertices[mouse.position]:
                    mouse.move_mouse(next_position, graph)
                    valid_move = True
                else:
                    print("Sorry, but the move you have tried is not possible, perhaps you should move to one of the positions which are accessible from where you are right now.")
            except ValueError:
                print("Sorry, but your input is not the number of a node. Please try again.")

        if mouse.eaten:
            print("The cat has caught the mouse! The cat wins!")
            break

        if moves == move:
            print("You have managed to defeat the cat! You live to fight another day.")
            break

    print("Game over.")


if __name__ == "__main__":
    main()
