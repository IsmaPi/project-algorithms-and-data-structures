
# Description

This is the final A&DS computer science course project by David Oreoluwa, Ismael Picazo,  Nicolás Leyva, and Zaid Tayan. The game is an implementation of the cat and mouse, where the player has to escape the cat through a maze.

# Rules

The game is a cat-and-mouse game where the playspace is a graph. The player is the mouse, and they must escape from the cat for a certain number of moves. If the cat can catch the mouse before the turns end, the cat wins, and if the mouse can avoid the cat for the number of turns, the player wins.

# Game Logic

The project is divided into three programs: players.py (where the classes for the cat and the mouse are), graph.py (where the graph is defined), and main.py.

Firstly, within players.py, we can first see a breath-first search algorithm, where the graph nodes are traversed and then added to a dictionary to keep track of the different paths from the cat to the mouse. While the queue has elements (meaning that the cat and the mouse are not in the same location, ending the game with a win from the cat), the algorithm traverses the path until it reaches the node where the mouse is. Once the condition is satisfied, the algorithm returns the next movement towards the mouse. Furthermore, we have two classes: cat and mouse.

  - Cat: The cat class is composed of two methods, init, and move_towards_mouse:
    
      - init: defines the current position of the cat
        
      - move_towards_mouse: takes the position of the cat and the mouse. It calls the bfs function to define the path the cat must take to reach the mouse. After getting the path, the method checks the length of the path, and if the path has a length of 1 or less, it means that in the current or next move, the mouse will be caught and that a different method in the mouse class (mouse.game_over) is called. If the path is longer than one, the position changes and a message is printed to show where the cat has moved. Finally, there is a check to see if the cat's position is the same as that of the mouse, in which case it calls the mouse.game_over method.

  - Mouse: The mouse class is composed of three methods: init, move_mouse, and game_over
    
      - init: defines the current position of the mouse
        
      - move_mouse: takes the next_position and the graph. If the next_position is a node in the graph connected to the current node the player is in, the position is updated and prints a message to communicate to the user that they have moved and where they have moved. If the node inputted is not accessible, an error message is shown.
        
      - game_over: when called, it sets a variable self.eaten to true.

Secondly, the graph.py presents us with the main class for the creation and properties of a graph. 

  - init: This is where the new instances of the graph class are. It creates a dictionary (self.vertices) storing the graph nodes with the adjacent nodes.
    
  - add_vertex: The method takes a node and checks if the specified node is in self.vertices, and if it's not, it is added as a key to the dictionary with a list that will be modified to store adjacent nodes.
    
  - add_edge: It takes two nodes (a and b) and generates a path between them by calling the method add_vertex for both a and b to ensure both nodes are in the graph. It later checks if a and b are in each other's adjacency list, and if they aren't, they are added. This ensures that the graph is undirected since each node is in the adjacency list of the other.
    
  - add_edges: It takes the *args, which each represents a connection between nodes as a tuple [A, B], and calls the add_edge for each tuple and adds the connection.
    
  - print: it takes the cat_position and mouse_position and prints the graph by going over the nodes. If the node has the cat, it adds a 'C', and if it has the mouse, it adds an 'M'. Otherwise, it just adds a space. Finally, it prints each node with the corresponding symbol and the adjacent nodes.

Finally, in main, we can find three functions: is_min_distance, set_starting_positions, and main.

  - is_min_distance takes the graph, the start, the end, and the minimum distance between the cat and the mouse. This is very important as if it was not taken into account, there could be cases where the cat and mouse aren't far enough to be able to play since the cat could kill the mouse instantly. To do this, it calls the bfs function to calculate the shortest path and compares its length to the minimum length.
    
  - set_starting_positions takes the graph to then take the nodes and generate two random starting positions to the cat and mouse, but it checks if the positions are far enough by using the function is_min_distance. If it is, it just assigns the positions to the cat and mouse. If not, the process starts over, and new initial positions are generated until it passes the is_min_distance check.
    
  - The main is where everything occurs. First, the graph and the initial positions are generated using the Graph class and the set_starting_positions function. Once that is done, the maximum number of turns is defined, and it's the cat's turn. It uses the Cat class, running over it, and once the cat has moved, it checks if the new location is the same as the mouse location. If it is, the mouse loses. If the mouse is still alive, it shows the graph and prompts the user to enter a new move for the Mouse. Once the input of the user is accepted, the loop starts again. 

# Data Structures

## Graph (Main playing field):

- When thinking about the idea for the game, we came across a game called Scotland Yard, where a policeman tries to catch a criminal and has to traverse the city of London through the underground, taxis, and ferries. When thinking about this, we noticed that a graph would be the ideal data structure for a version of the game, and because of a Tom and Jerry video, we decided to create a chasing game with a cat and mouse as the characters.

- We chose it because it would allow for a maze-like structure since we can connect different nodes between each other but are not limited to a certain number of hierarchical structures such as trees.
  
- Each node corresponds to a location in the maze and allows for efficient addition, deletion, and tracking of node connections.
  
- Because nodes can be easily accessed and traversed, there is no need for complex methods to move through the nodes.
  
- We decided to use an undirected graph. This allows the connections between two nodes to be bidirectional and maximizes the possible moves that both the player and the cat can make, involving a higher level of strategizing as you have to consider more possible moves.

- One of the main issues with the graph is that to print the graph, each node has to be printed individually.

## Queue (Path list):

- To store the nodes traversed for the generation of the path between the cat and the mouse to get the move the cat should make. Since we need the order, we have to use the first-in-first-out logic to be able to apply the breadth-first search algorithm explored further down the documentation.
  
- This data structure is much better than other possibilities, such as an array, since it has a time complexity of O(1) for adding and popping the elements from the queue.
  
- The main issue with this data structure is that there are some issues with the dynamic resizing of the queue, which could prove to be cumbersome for longer and more complex graphs.

## Dictionary (Adjacency list):

- It stores the nodes and the connected ones to access the neighbors.
  
- Using this is the best option for this specific application, as it allows us to access the nodes adjacent to the current one and easily add and delete nodes to the adjacency of the current node. It also provides a time complexity of O(1).
  
- The issue with this implementation is that it takes up more memory than other similar data structures.

## Set (Visited in the breadth-first search):

- This data structure keeps visited nodes in the breadth-first search to avoid revisiting them.
  
- It's beneficial since adding and checking for membership in the set has a time complexity of O(1).
  
- The main issue is that the elements are unordered, but this does not apply to our game, as we want each node to be visited only once.

## List (Best path for the cat and positions for the setting of the starting positions):
- In our case, we use the list for the path for the cat and to keep the starting positions of both the player and the cat.
  
-  This structure is advantageous as we can easily change the size to store more elements and iterate to traverse it.
-  The issue with this data structure is that it has a time complexity of O(N), and arrays in Python also take up a significant amount of memory for dynamic resizing.

# Algorithms

## Breadth-First Search:

- The breadth-first search algorithm is used mainly for the pathfinding of the cat.
  
- We decided to use it since we can easily find the path with the least number of connections (or edges) to develop the best path from the cat to the mouse.
  
- It is also essential since getting stuck in cycles in an unweighted graph is impossible with this algorithm. However, it requires increased memory usage depending on the number of connections to each edge. It may consume too much memory, with a space complexity of (O(b^d)) where b is the branching factor and d is the depth.
  
- The time complexity of the algorithm is O(M + N) in the worst case, where M is the number of connections and N is the number of nodes, and the average case is the same with O(M + N) but depends on the size of the graph.

## Linear search:

- Linear search is used in every traversal of a linear data structure (array, set, dictionary) in the three programs.
- We decided to use it since it allows for looking up and searching for data in a low memory use with small datasets, which is our case.

- Furthermore, linear search is an excellent choice for this application since the data is not ordered.
  
- Finally, the time complexity for the worst case for this algorithm is O(N), and for the average case is the same, O(N)
