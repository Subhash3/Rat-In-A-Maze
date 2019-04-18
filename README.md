# Rat in a Maze
[*] The program is written in python3 using the module "pygame"(a 2d gui framework for python).
[*] To install pygame in a linux distrubution, use the following command :
		"sudo pip3 install pygame"
[*] To run the program give executable permission to the python script file :
		"chmod +x rat-and-maze.py"
    and execute using "./rat-and-maze".
[*] The maze is of size 20 x 20.
[*] There are two button in the gui window.
    1. Generate Maze : Generates random mazes.
    2. Solve : Solves the current maze.
[*] If these buttons are clicked while solving a maze, nothing will happen.
[*] After solving a maze, if we click on solve button again, it solves the same maze again.
[*] After the completion of solving each maze, a respective message will be displayed on the screen and vanishes after 3 seconds.
[*] There are threee images in the maze.
    1. rat.jpg : The moving rat.
    2. cheese.jpg : Cheese in the destination cell.
    3. ratCheese.jpg : This figure appears in the destination if the path is found.
    (Deleting these images will not result any errors.)
