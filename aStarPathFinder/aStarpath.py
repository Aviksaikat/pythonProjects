#!/usr/bin/python3
from queue import PriorityQueue
try:
    import pygame
    import sys
    import math
    from tkinter import *
    import os
except:
    import pygame
    import sys
    import math
    from tkinter import *
    import os

WIDTH = 800
#setting up the display
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (231,76,60)
GREEN = (34,153,84)
BLUE = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
S_BLACK = (27,38,49)
DARK_YELLOW = (214,255,30)
VIOLET = (194,41,255)
GREY = (128,128,128)
TURQUOISE = (64,224,208)
ICY_GREEN = (59,237,135)
KICHU_BLUE = (93,173,226)
#viz tools
class Node():
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width  #x,y for pos of vertex
        self.y = col * width # WIDTH/no. of cubes = width of each cubes
        self.color = S_BLACK # all white cube
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows 
    
    def get_pos(self):
        return self.row,self.col #format = (col,row)

    def is_cloed(self):
        return self.color == ICY_GREEN #if color is red it means the node is visited and of no use
    
    def is_open(self):
        return self.color == KICHU_BLUE #can go there
    
    def is_barrier(self):
        return self.color == WHITE #barrier can't go there 
    
    def is_start(self):
        return self.color == VIOLET #starting node

    def is_end(self):
        return self.color == RED
    
    def reset(self):
        self.color = S_BLACK

    def make_start(self):
        self.color = VIOLET

    def make_closed(self):
        self.color = ICY_GREEN

    def make_open(self):
        self.color = KICHU_BLUE

    def make_barrier(self):
        self.color = WHITE

    def make_end(self):
        self.color = RED

    def make_path(self):
        self.color = DARK_YELLOW

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
        # 2 times width bcz it's a rectangle
    
    def update_neighbours(self,grid):
        self.neighbours = []
        if(self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier()):#going down the row(can we go down checking)
            self.neighbours.append(grid[self.row + 1][self.col])
        
        if(self.row > 0 and not grid[self.row - 1][self.col].is_barrier()):#going up the row(can we go up checking)
            self.neighbours.append(grid[self.row - 1][self.col])
        
        if(self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier()):#going right the row(can we go right checking)
            self.neighbours.append(grid[self.row][self.col + 1])
        
        if(self.col > 0 and not grid[self.row][self.col - 1].is_barrier()):#going left the row(can we go left checking)
            self.neighbours.append(grid[self.row][self.col - 1])
        

    def __lt__(self, other): #less than comapring 2 nodes(2 points)
        return False

# heuristic fn. = educated guess
def h(p1,p2): #cal dist. using manhaten dist. cal. L dist. b/w 2 points
    x1,y1 = p1
    x2,y2 = p2 
    return abs(x1-x2) + abs(y1-y2)

#trac-back the path 
def reconstruct_path(prev_node, current, draw):
    while(current in prev_node):
        current = prev_node[current]
        current.make_path()
        draw()
        


#A* algo F(n) = G(n) + H(n)
def algo(draw,grid,start,end):
    count = 0
    open_set = PriorityQueue()
    #count for tie breaker.2 same F score will chose the first inserted FIFO
    open_set.put((0,count, start))#push
    prev_node = {}
    g_score = {node: float("inf") for row in grid for node in row}#table "inf" = infinity at initial bcz we don't know how to preoceed
    g_score[start] = 0 #first node
    
    f_score = {node: float("inf") for row in grid for node in row}# predicted dist. form current to end node
    f_score[start] = h(start.get_pos(),end.get_pos()) #estimating dist the  H(n)

    open_set_hash = {start} #set #check if the node is int the queue

    while not open_set.empty():
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()#exit the algo/game
            
        current = open_set.get()[2]#open_set.put((0,count, start))
        # we need start so the index is 2
        #poping the lowest value F score from the queue
        open_set_hash.remove(current)#removing form the set open_set_hash
        #this node is the end node we found the shortest path
        if(current == end):
            reconstruct_path(prev_node, end, draw) #draw passed in algo the lambda one
            end.make_end() # stop printing the path color on the end node
            return True
        
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1 #assuming all node is of same dist. and going to the next node

            if(temp_g_score < g_score[neighbour]): #new g_score is less update the score bcz we haev found a better path
                prev_node[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(),end.get_pos())
                if(neighbour not in open_set_hash):
                    count+=1
                    open_set.put((f_score[neighbour],count,neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        draw()

        if(current != start): # if the node is not the start node
            current.make_closed()
    
    return False

def make_grid(rows,width):
    grid = []
    gap = width // rows #width of each cube
    for i in range(rows):
        grid.append([]) # making a empty 2D list 
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)
    
    return grid

#drawing the grid

def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        #drawing the horizontal lines
        pygame.draw.line(win,GREY, (0, i * gap), (width,i * gap)) 
        for j in range(rows):
            #drawing the vertical lines
            pygame.draw.line(win,GREY, (i * gap,0), (i * gap,width))

#drawing the whole thing

def draw(win,grid,rows,width):
    win.fill(S_BLACK) #drwaing the initial board

    for row in grid:
        for node in row:
            node.draw(win) #calling the draw fn.
        
    draw_grid(win,rows,width)
    pygame.display.update() # update the drawing on the display

#mouse pos , clicking  

def get_clicked_pos(pos,rows,width):
    gap = width // rows
    y,x = pos
    row = y //gap 
    col = x //gap
    return row,col

#pop-up window
def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    m = message
    m += "\n"
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()

#win is the window
def main(win,width):
    ROWS = 50
    grid = make_grid(ROWS,width)

    start = None
    end = None
    
    run = True
    alert_popup("A* manual", "Hello ", "Place 2 points on the canvas \n 'Space' to start the program \n 'c' to reset")
    while(run):
        draw(win,grid,ROWS,width)
        #looping through all events like mouse click etc.
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            #to stop the user form doing anything after the algo. is started
            # right or left click
            if pygame.mouse.get_pressed()[0]:#left
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                if not start and node!= end: # not starting point is set
                    start = node
                    start.make_start()
                
                elif not end and node!= start:
                    end = node
                    end.make_end()
                
                elif (node!=end and node!=start):
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:#right
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                node.reset()

                if(node == start):
                    start = None
                elif(node == end):
                    end = None

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE and start and end): #make sure that the start and end node is present before starting the algo
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    
                    #lambda is passing a fn. which is fucntion call
                    algo(lambda: draw(win, grid, ROWS, width),grid, start, end)
                
                if(event.key == pygame.K_c):
                    start = None 
                    end  = None
                    grid = make_grid(ROWS, width)
    pygame.quit()
    

main(WIN,WIDTH)
