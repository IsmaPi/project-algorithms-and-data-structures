
# Description

This project is the final project for the A&DS computer science course by David Oreoluwa, Ismael Picazo,  Nicolás Leyva, and Zaid Tayan. The game is an implementation of the cat and mouse, where the player has to escape the cat through a maze.

# Rules

The game is a cat-and-mouse game where the playspace is a graph. The player is the mouse, and they must escape from the cat for a certain number of moves. If the cat is able to catch the mouse before the turns end, the cat wins, and if the mouse is able to avoid the cat for the number of turns, the player wins.

# Game Logic

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

# Data Structures

## Graph (Main playing field):

- When thinking about the idea for the game, we came across a game called Scotland Yard, where a policeman tries to catch a criminal and has to traverse the city of London through the underground, taxis, and ferries. When thinking about this, we noticed that a graph would be the ideal data structure for a version of the game, and because of a Tom and Jerry video, we decided to create a chasing game with a cat and mouse as the characters.

- We chose it because it would allow for a maze-like structure since we can connect different nodes between each other but not be limited to a certain number of hierarchical structures such as trees.
  
- Each node corresponds to a location in the maze and allows for efficient addition, deletion, and keeping track of connections between nodes.
  
- Due to the fact that nodes can be easily accessed and traversed, there is no need for complex methods to move through the nodes.
  
- We decided to use an undirected graph. This allows the connections between two nodes to be bidirectional and maximizes the possible moves that both the player and the cat can make, involving a higher level of strategizing as you have to take into consideration more possible moves.

- One of the main issues with the graph is that to print the graph, each node has to be printed individually.

## Queue (Path list):

- To store the nodes traversed for the generation of the path between the cat and the mouse to then get the move the cat should make. Since we need the order, we have to use the first-in-first-out logic to be able to apply the breadth-first search algorithm explored further down the documentation.
  
- This data structure is much better than other possibilities, such as an array, since it has a time complexity of O(1) for adding and popping the elements from the queue.
  
- The main issue with this data structure is that there are some issues with the dynamic resizing of the queue, which could prove to be cumbersome for longer and more complex graphs.

## Dictionary (Adjacency list):

- It stores the nodes and the connected ones to be able to access all of the neighbors.
  
- Using this is the best option for this specific application, as it allows us to access the nodes adjacent to the current one and be able to easily add and delete nodes to the adjacency of the current node. It also provides a time complexity of O(1).
  
- The issue with this implementation is that it takes up more memory than other similar data structures.

## Set (Visited in the breadth-first search):

- This data structure is used for the keeping of visited nodes in the breadth-first search not to revisit them again.
  
- It's very useful since adding and checking for membership in the set has a time complexity of O(1).
  
- The main issue is that the elements are unordered, but for our game, this is not applicable as we want each node to be visited only once.

## List (Best path for the cat and positions for the setting of the starting positions):
- In our case, we use the list for the path for the cat and to keep the starting positions of both the player and the cat.
  
-  This structure is very useful as we can easily dynamically change the size to store more elements and iterate to traverse it.
-  The issue with this data structure is that it has a time complexity of O(N), and arrays in Python also take up a significant amount of memory for dynamic resizing.

# Algorithms

## Breadth-First Search:

- Breadth-First Search algorithm used mainly for the pathfinding of the cat.
  
- We decided to use it since we can easily find the path with the least number of connections (or edges) to develop the best path from the cat to the mouse.
  
- It is also important since it is basically impossible to get stuck in cycles in an unweighted graph. However, it requires increased memory usage depending on the number of connections to each edge it may consume too much memory (O(b^d)) where b is the branching factor and d is the depth.
  
- The time complexity of the algorithm is O(M + N) in the worst case, where M is the number of connections and N is the number of nodes, and the average case is the same with O(M + N), but depends on the size of the graph.

## Linear search:

- Linear search is used in every traversal of a linear data structure (array, set, dictionary) in the three programs.
- We decided to use it since it allows for looking up and searching for data in a low memory use with small datasets, which is our case.

- Furthermore, since the data is not ordered, linear search is an excellent choice for this application.
  
- Finally, the time complexity for the worst case for this algorithm is O(N), and for the average case is the same, O(N)
