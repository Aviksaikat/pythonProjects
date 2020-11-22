# Python implementation for visualizing merge sort.  
import pygame 
import random 

#*initialize pygame
pygame.font.init() 

SIZE = 155
WIDTH = 1000
LENGTH = 600

screen = pygame.display.set_mode((WIDTH,650)) 
pygame.display.set_caption("SORTING VISUALISER")   
run = True

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (229,231,233)

array =[0]*SIZE
arr_clr =[(0, 204, 102)]*SIZE
clr_ind = 0

#* colors [blue,red,green,violet]
clr =[(52,152,219),(255,63,47),(39,243,89),(165,105,189)] 
fnt = pygame.font.SysFont("comicsans", 30) 
fnt1 = pygame.font.SysFont("comicsans", 24) 

def generate_arr(): 
    for i in range(1, SIZE): 
        arr_clr[i]= clr[0] 
        array[i]= random.randrange(1, 100) 
generate_arr()  

def refill(): 
    screen.fill(GREY) 
    draw() 
    pygame.display.update() 
    pygame.time.delay(15) 
  

def mergesort(array, l, r): 
    mid =(l + r)//2
    if l<r: 
        mergesort(array, l, mid) 
        mergesort(array, mid + 1, r) 
        merge(array, l, mid,mid + 1, r) 
def merge(array, x1, y1, x2, y2): 
    i = x1 
    j = x2 
    temp =[] 
    pygame.event.pump()  
    while i<= y1 and j<= y2: 
        arr_clr[i]= clr[1] 
        arr_clr[j]= clr[1] 
        refill() 
        arr_clr[i]= clr[0] 
        arr_clr[j]= clr[0] 
        if array[i]<array[j]: 
                temp.append(array[i]) 
                i+= 1
        else: 
                temp.append(array[j]) 
                j+= 1
    while i<= y1: 
        arr_clr[i]= clr[1] 
        refill() 
        arr_clr[i]= clr[0] 
        temp.append(array[i]) 
        i+= 1
    while j<= y2: 
        arr_clr[j]= clr[1] 
        refill() 
        arr_clr[j]= clr[0] 
        temp.append(array[j]) 
        j+= 1
    j = 0    
    for i in range(x1, y2 + 1):  
        pygame.event.pump()  
        array[i]= temp[j] 
        j+= 1
        arr_clr[i]= clr[2] 
        refill() 
        if y2-x1 == len(array)-2: 
            arr_clr[i]= clr[3] 
        else:  
            arr_clr[i]= clr[0] 
  

def draw(name="MERGE SORT"): 
    txt = fnt.render("PRESS"\
        " 'SPACE' TO PERFORM SORTING.", 1, BLACK) 
    
    #*this is the location of the prev text 
    screen.blit(txt, (20, 20)) 
    txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.",1, BLACK) 
    screen.blit(txt1, (20, 40)) 
    
    txt2 = fnt1.render(f"ALGORITHM USED: {name}", 1, BLACK) 
    screen.blit(txt2, (LENGTH, 60)) 
    
    element_width = (WIDTH-150)//150
    boundry_arr = WIDTH / 150
    boundry_grp = 550 / 100
    
    #* format line(surface, color, start_pos, end_pos, width)
    pygame.draw.line(screen,(0, 0, 0),(0, 95),(WIDTH, 95), 6) 
    # for i in range(1, 100): 
        # pygame.draw.line(screen,  
                        # (224, 224, 224),  
                        # (0, boundry_grp * i + 100),  
                        # (WIDTH, boundry_grp * i + 100), 1) 
    
    #*drwaing the bar over the window as a line  
    for i in range(1, SIZE): 
        pygame.draw.line(screen, arr_clr[i],
            (boundry_arr * i-3, 100),
            (boundry_arr * i-3, array[i]*boundry_grp + 100),
            element_width) 

while run: 
    screen.fill(GREY) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                generate_arr()  
            if event.key == pygame.K_SPACE: 
                mergesort(array, 1, len(array)-1)      
    draw() 
    pygame.display.update() 
pygame.quit()