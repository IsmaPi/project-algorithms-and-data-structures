from graph import Graph
from players import Cat, Mouse
import random

def main():
    # I created a graph inastance which was called from the graph file to create the graph in the main function.
    graph = Graph()

    # Setting the initial cat position and the mouse position to random.
    all_positions = list(graph.vertices.keys())

    position_cat = random.choice(all_positions)

    # Remove the cat initial position from all positions.
    all_positions.remove(position_cat)

    position_mouse = random.choice(all_positions)

    # Create instances of the Cat and Mouse classes
    cat = Cat(position_cat)
    mouse = Mouse(position_mouse)

    

    # Main game loop
    moves_limit = 15  # Adjust this limit as needed
    for moves_num in range(1, moves_limit + 1):
        print(f"\n Move: {moves_num}")

        # Cat's turn
        cat.move_towards_mouse(mouse, graph)

        # Check if the game is over
        if mouse.game_over():
            print("The mouse is found the cat wins the game!!!")
            break

        # Mouse's turn
        print("\nMouse's turn:")
        print("Current graph:")
        graph.print(cat.position, mouse.position)

        # Get the next move from the player (you can replace this with user input or a different logic)
        next_position = input("Enter the next position for the mouse: ")

        # Move the mouse
        mouse.move_mouse(next_position, graph)

        # Im checking if the game is over
        if mouse.game_over():
            print("Cat wins!")
            break

        # I'm checking if the moves limit has been exhausted
        if moves_num == moves_limit:
            print("The cat moves has been exhausted, the mouse wins!!!")
            break

    print("Game over.")
