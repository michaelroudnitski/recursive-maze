#########################################
# Programmer: Michael Roudnitski
# Date: 28/02/2017
# File Name: maze.py
# Description: This program solves a maze of arbitrary size.

from random import randint
import pygame
import time

RED = (255, 83, 13)
GREEN = (0, 255, 0)
BLUE = (13, 204, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clrs = {'`':BLUE, '#':BLACK, 'G':GREEN, ' ':WHITE, 'x':RED}

def load_maze(fname):
    maze = open(fname, 'r')
    lines = maze.readlines()
    mazelist = []
    for line in lines:
        rows = line.strip("\n")
        elements = list(rows)
        mazelist.append(elements)
    maze.close()
    return mazelist


def pick_random_location(maze):
    row = 0
    column = 0
    while maze[row][column] != ' ':
        row = randint(1,len(maze)-1)
        column = randint(1,len(maze[0])-1)
    return row, column

def print_maze(maze):
    rows = ''
    for x in range(len(maze)):
        print rows.join(maze[x])

def find_path(maze,x,y):
    if maze[y][x] == 'G':
        print 'You have reached the goal at (', x, ',', y, ')!'
        return True
    elif maze[y][x] != ' ' and maze[y][x] != 'S':
        print '(',x,',',y,') is blocked'
        return False

    maze[y][x] = '`'

    redraw_screen()
    #print_maze(maze)

    if find_path(maze, x, y - 1):
        return True
    elif find_path(maze, x + 1, y):
        return True
    elif find_path(maze, x, y + 1):
        return True
    elif find_path(maze, x - 1, y):
        return True

    maze[y][x] = 'x'
    return False

def redraw_screen():
    pygame.event.clear()
    screen.fill(BLACK)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            pygame.draw.rect(screen, clrs[maze[y][x]], (x*width, y*height, width, height),0)
    time.sleep(0.01)

    pygame.display.update()

#---------------------------------------#
# main program                          #
#---------------------------------------#        
#fname = raw_input("Enter filename: ")
fname = 'maze1.txt'
maze = load_maze(fname)

WIDTH = len(maze[0])*20
HEIGHT = len(maze)*20
screen = pygame.display.set_mode((WIDTH, HEIGHT))

width = WIDTH / len(maze[0]) #defining width of each grid point
height = HEIGHT / len(maze)  #defining height of each grid point

start = pick_random_location(maze)
goal = pick_random_location(maze)

sX, sY, gX, gY = start[1], start[0], goal[1], goal[0]

if sX == gX and sY == sY:               #regenerate goal coordinates if goal and start are in the same spot
    goal = pick_random_location(maze)
    gX, gY = goal[1], goal[0]

maze[sY][sX], maze[gY][gX] = 'S', 'G'

find_path(maze, sX, sY)
maze[sY][sX] = 'S'
print '\nHere is the maze with the path from start to goal:'
print_maze(maze)

