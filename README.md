# The Cat and Mouse

This project is the final project for the A&DS computer science course by David Oreoluwa, Ismael Picazo,  Nicolás Leyva, and Zaid Tayan.

## Description

The game is a cat-and-mouse game where the playspace is a graph. The player is the mouse, and they must escape from the cat for a certain number of moves. If the cat is able to catch the mouse before the turns end, the cat wins, and if the mouse is able to avoid the cat for the number of turns, the player wins.

The project is divided into three distinct programs: players.py (where the classes for both the cat and the mouse are), graph.py (where the graph is defined), and main.py.

Firstly, within players.py, the first thing we can see is the use of a breath-first search algorithm, where the graph nodes are traversed and then added to a dictionary to keep track of the different paths from the cat to the mouse. While the queue has elements (meaning that the cat and the mouse are not in the same location, ending the game with a win from the cat), the algorithm traverses the path until it reaches the node where the mouse is. Once the condition is satisfied, the algorithm returns the next movement towards the mouse. Furthermore, we have two classes: cat and mouse.

  - Cat: The cat class is composed of two methods, init, and move_towards_mouse:
    
      - init: defines the current position of the cat
        
      - move_towards_mouse: takes the position of the cat and the mouse. It calls the bfs function to define the path the cat must take to reach the mouse. After getting the path, the method checks the length of the path, and if the path has a length of 1 or less, it means that in the current or next move, the mouse will be caught and that a different method in the mouse class (mouse.game_over) is called. If the path is longer than one, the position is changed, and a message is printed to show where the cat has moved. Finally, there is a check to see if the position of the cat is the same as that of the mouse, in which case it calls the mouse.game_over method.

  - Mouse: The mouse class is composed of three methods, init, move_mouse, and game_over:
    
      - init: defines the current position of the mouse
        
      - move_mouse: takes the next_position and the graph. If the next_position is a node in the graph and is connected to the current node the player is in, the position is updated and prints a message to communicate to the user that they have moved and where they have moved. If the node inputted is not accessible, an error message is shown.
        
      - game_over: when it is called, it sets a variable self.eaten to true and prints a game-over message to the user.

Secondly, the graph.py presents us with the main class for the creation and properties of a graph. 

  - init: This is where the new instances of the graph class are. It creates a dictionary (self.vertices) where the nodes of the graph are stored with the adjacent nodes.
    
  - add_vertex: The method takes a node and checks if the specified node is in self.vertices, and if it's not, it is added as a key to the dictionary with a list that will be modified to store adjacent nodes.
    
  - add_edge: It takes two nodes (a and b) and generates a path between them by calling the method add_vertex for both a and b to ensure both nodes are in the graph. It later checks if a and b are in the adjacency list of each other and if they aren't, they are added. This is to make sure that the graph is undirected since each node is in the adjacency list of the other.
    
  - add_edges: It takes the *args, which each represents a connection between nodes in the form of a tuple [A, B], and calls the add_edge for each tuple and adds the connection.
    
  - print: it takes the cat_position and mouse_position and prints the graph by going over the nodes. If the node has the cat, it adds a 'C', and if it has the mouse, it adds an 'M'. Otherwise, it just adds an empty space. Finally, it prints each node with the corresponding symbol and the adjacent nodes.

### Dependencies
The libraries needed for the program to function correctly are: 
random, deque from collections

### Executing program
To run the program, execute the main.py program.


