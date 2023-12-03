from graph import Graph
from players import Cat, Mouse
import random

def main():
    graph = Graph()
    # Initialize the game graph
    graph.add_edges(('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('A', 'C'), ('B', 'D'), ('C', 'E'))

    # Randomly determine the initial positions of the cat and mouse
    all_positions = list(graph.vertices.keys())
    position_cat = random.choice(all_positions)
    all_positions.remove(position_cat)
    position_mouse = random.choice(all_positions)

    cat = Cat(position_cat)
    mouse = Mouse(position_mouse)

    moves_limit = 15
    for moves_num in range(1, moves_limit + 1):
        print(f"\nMove: {moves_num}")

        # Cat's turn
        cat.move_towards_mouse(mouse, graph)

        # Check if the cat has caught the mouse
        if mouse.eaten:
            print("The cat has caught the mouse! The cat wins!")
            break

        # Mouse's turn
        print("\nMouse's turn:")
        print("Current graph:")
        graph.print(cat.position, mouse.position)

        next_position = input("Enter where you want to move next: ")

        # Move the mouse and validate the move
        if next_position in graph.vertices[mouse.position]:
            mouse.move_mouse(next_position, graph)
        else:
            print("Sorry, but the move you have tried is not possible, pehaps you should move to one of the positions which are accessible from where you are right now.")
            continue  # Skips the rest of the loop and start the next turn

        # Check if the cat has caught the mouse after the move
        if mouse.eaten:
            print("The cat has caught the mouse! The cat wins!")
            break

        # Check if the move limit has been reached
        if moves_num == moves_limit:
            print("Move limit reached. The mouse wins!")
            break

    print("Game over.")

# Make sure to call main to start the game
if __name__ == "__main__":
    main()
