#!/usr/bin/python3

import pygame
import random
import time

pygame.init()
pygame.font.init()

#size = int(input("Enter size: "))
size = 20
width = height = 25
winWidth = 500
winHeight = 580

window = pygame.display.set_mode((winWidth, winHeight))
pathInfo = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Rat!! Go find the Cheese.!!")
cheese_x = cheese_y = size -1
try :
    ratImg = pygame.image.load("rat.jpg")
    cheeseImg = pygame.image.load("cheese.jpg")
    ratCheeseImg = pygame.image.load("ratCheese.jpg")
    imagesFound = True
except :
    imagesFound = False
    pass

#rat_x = 0
#rat_y = 0

class Cell :
    def __init__(self) :
        self.blocked = 1

# Function to create a button
def button(string, x, y, w, h, inactiveColor, onHoverColor) :
    # x, y : Co-ordinates of the button
    # w, h : Dimensions of the button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    flag = 0 # Not clicked

    # If the cursor position is on the button
    if x < mouse[0] < x+w and y < mouse[1] <y+h :
        pygame.draw.rect(window, onHoverColor, (x, y, w, h))

        # If clicked
        if click[0] == 1 :
            flag = 1
    # If cursor is not on the button ==> inactive
    else :
        pygame.draw.rect(window, inactiveColor, (x, y, w, h))

    font = pygame.font.SysFont("latinmodernmonocaps", 20)
    text = font.render(string, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.centerx = x+70
    textRect.centery = y+13
    window.blit(text, textRect) 

    return flag


# Function to draw maze
def drawMaze(maze, width, height, size, rat_x = 0, rat_y = 0) :
    window.fill((0, 0, 0)) # Fill window with black
    i = 0
    for row in maze :
        j = 0
        for cell in row :
            if cell.blocked == 1 :
                color = (7, 32, 73, 1)
            elif cell.blocked == 0 :
                color = (106, 197, 120, 1)
            elif cell.blocked == 8 :
                color = (0, 255, 0, 1)
            else :
                color = (0, 90, 0, 1)
            pygame.draw.rect(window, color, (j*width, i*height, width-2, height-1))
            j += 1
        i += 1
    if imagesFound :
        window.blit(cheeseImg, (cheese_y*height, cheese_x*width))
        window.blit(ratImg, (rat_y*height, rat_x*width))
    else :
        pass

    """
    button("Generate Maze", 10, 520, 150, 30, (100, 100, 100), (70, 70, 110))
    button("Solve", 340, 520, 150, 30, (100, 100, 100), (70, 70, 110))
    """
    # display buttons
    button(" Generate Maze", 10, 520, 150, 30, (100, 100, 100), (70, 70, 110))
    button("Solve", 340, 520, 150, 30, (100, 100, 100), (70, 70, 110))
    pygame.display.update()
    return

# After a maze is solved, get back its original cells
def restoreMaze(maze) :
    for row in maze :
        for cell in row :
            if cell.blocked != 1 :
                cell.blocked = 0

# Function to display msg on the window
def displayMsg(string, color) :
    # Create a surface with transparency 160
    s = pygame.Surface((winHeight, winWidth))
    s.set_alpha(160)
    s.fill((0))
    # Display a transparent screen on the window
    window.blit(s, (0, 0))

    # Display text
    font = pygame.font.SysFont("latinmodernmonocaps", 80)
    text = font.render(string, True, color)
    textRect = text.get_rect()
    textRect.centerx = window.get_rect().centerx
    textRect.centery = window.get_rect().centery
    #textRect.center = (winHeight // 2, winWidth // 2) 
    window.blit(text, textRect) 
    pygame.display.update()
    time.sleep(2)

    return


def winningMsg(string) :
    s = pygame.Surface((winHeight, winWidth))
    s.set_alpha(160)
    s.fill((0))
    window.blit(s, (0, 0))

    font = pygame.font.SysFont("latinmodernmonocaps", 80)
    text = font.render(string, True, (90, 108, 190))
    textRect = text.get_rect()
    textRect.centerx = window.get_rect().centerx
    textRect.centery = window.get_rect().centery
    #textRect.center = (winHeight // 2, winWidth // 2) 
    window.blit(text, textRect) 
    pygame.display.update()
    time.sleep(2)

    return

def lostMsg(string) :
    s = pygame.Surface((winHeight, winWidth))
    s.set_alpha(160)
    s.fill((0))
    window.blit(s, (0, 0))

    font = pygame.font.SysFont("latinmodernmonocaps", 80)
    text = font.render(string, True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = window.get_rect().centerx
    textRect.centery = window.get_rect().centery
    #textRect.center = (winHeight // 2, winWidth // 2) 
    window.blit(text, textRect) 
    pygame.display.update()

    return

# Initialize maze with cell objects
maze = [[Cell() for i in range(size)] for j in range(size)]

def generateMaze(maze) :
    # creating a random maze
    for i in range(size) :
        for j in range(size) :
            num = int(random.random()*10)%3
            if num == 1 :
                maze[i][j].blocked = 1 # blocked cell
            else :
                maze[i][j].blocked = 0 # open cell

            # first and last cells are always opened
            if i == j == 0 or i == j == size -1 :
                maze[i][j].blocked = 0
    return maze

# Wait till the close button is clicked
def waitUntilQuit() :
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                quit()

# Function to find the path
def findPath(maze) :
    path = list() # Stack to restore location

    # Initially location is (0, 0)
    # direction is right
    row = col = 0
    direction = 1

    while True :
        #print(row, col)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                quit()
        # Visited cell contains 8
        maze[row][col].blocked = 8
        # Location to display rat
        rat_x = row
        rat_y = col
        # Draw maze
        drawMaze(maze, width, height, size, rat_x, rat_y)

        #print("Path :", path)
        # If rat reached the last cell
        if row == col == size -1 :
            #print("Path Found")
            winningMsg("Path Found")
            drawMaze(maze, width, height, size, rat_x, rat_y)
            if imagesFound : 
                window.blit(ratCheeseImg, (cheese_y*height, cheese_x*width))
                pygame.display.update()
            else :
                pass
            #waitUntilQuit()
            return

        # Direction Preference : Right, Down, Left then Up.
        # Check if right move is possible
        if 0 <= row < size and 0 <= col +1 < size and maze[row][col+1].blocked == 0 :
            d = 1
            path.append([row, col, d]) # Push the location to the stack
            col += 1
        # Check if down move is possible
        elif 0 <= row +1 < size and 0 <= col < size and maze[row+1][col].blocked == 0 :
            d = 2
            path.append([row, col, d]) # Push the location to the stack
            row += 1
        # Check if left move is possible
        elif 0 <= row < size and 0 <= col -1 < size and maze[row][col-1].blocked == 0 :
            d = -1
            path.append([row, col, d]) # Push the location to the stack
            col -= 1
        # Check if up move is possible
        elif 0 <= row -1 < size and 0 <= col < size and maze[row -1][col].blocked == 0 :
            d = -2
            path.append([row, col, d]) # Push the location to the stack
            row -= 1
        else :
            # If move is not possible, the cell we are currently in
            # is not in the path, hence make it some other number
            # means visted, but not in the path
            maze[row][col].blocked = 2
            # If stack is empty, means no path
            if path == [] :
                displayMsg("No Path!!", (255, 0, 0))
                drawMaze(maze, width, height, size, rat_x, rat_y)
                return
            # Stack is not empty ==> there are some locations left unvisited
            # get the recently pushed one and go to the location
            popped = path.pop()
            row = popped[0]
            col = popped[1]

        time.sleep(0.2)
    return

# creating a random maze
maze = generateMaze(maze)
drawMaze(maze, width, height, size)
# Game main loop
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            quit()
    
    flag = button(" Generate Maze", 10, 520, 150, 30, (100, 100, 100), (70, 70, 110))
    pygame.display.update()
    # If generateMaze button is clicked, then generate a new maze and continue
    if flag == 1 :
        maze = generateMaze(maze)
        drawMaze(maze, width, height, size)
        continue

    sflag = button("Solve", 340, 520, 150, 30, (100, 100, 100), (70, 70, 110))
    # If Solve button is clicked then call find path function to solve the maze
    if sflag == 1 :
        findPath(maze)
        restoreMaze(maze) # after finding the path, restore the original maze
                          # cuz, the user may click the solve button again
                          # where u have to solve the same maze again
