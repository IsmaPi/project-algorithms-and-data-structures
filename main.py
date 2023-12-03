from graph import Graph
from players import Cat, Mouse, bfs
import random


def is_distance_sufficient(graph, start, end, min_distance=3):
    path = bfs(graph, start, end)
    return len(path) >= min_distance


def set_initial_positions(graph):
    all_positions = list(graph.vertices.keys())
    position_cat = random.choice(all_positions)
    all_positions.remove(position_cat)
    position_mouse = random.choice(all_positions)

    while not is_distance_sufficient(graph, position_cat, position_mouse):
        all_positions.append(position_mouse)
        position_mouse = random.choice(all_positions)
        all_positions.remove(position_mouse)

    return position_cat, position_mouse


def main():
    graph = Graph()
    graph.add_edges(
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

    position_cat, position_mouse = set_initial_positions(graph)
    cat = Cat(position_cat)
    mouse = Mouse(position_mouse)

    moves_limit = 10
    for moves_num in range(1, moves_limit + 1):
        print(f"\nMove: {moves_num}")

        cat.move_towards_mouse(mouse, graph)

        if mouse.eaten:
            print("The cat has caught the mouse! The cat wins!")
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
                    print("Invalid move. Please choose a valid adjacent vertex.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if mouse.eaten:
            print("The cat has caught the mouse! The cat wins!")
            break

        if moves_num == moves_limit:
            print("Move limit reached. The mouse wins!")
            break

    print("Game over.")


if __name__ == "__main__":
    main()
