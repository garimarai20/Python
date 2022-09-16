import pgzrun
from random import randint

HEIGHT = 500
WIDTH=500


ps = 3    # player speed
es = 1    # enemy speed 

game_over = False  #switch 
game_started = False # switch

center=(WIDTH//2,HEIGHT//2)  # points to the center coordinates of the screen

bg=Actor('bg', center= (0,0))
p = Actor('enemy',pos=(50,50))
e = Actor('alien',pos=(250,250))



def show_screen_1():
    bg.draw()
    screen.draw.text('Our Game',center=center,fontsize=100,color='white')
    screen.draw.text('Press SPACE to start', center=(center[0],center[1]+100),fontsize=50,color='white')

def show_game_screen():
     
    bg.draw()
    p.draw()
    e.draw()

def show_game_over():
    bg.draw()
    screen.draw.text('Game Over',center=center,fontsize=100,color='white')
    screen.draw.text('Press ENTER to restart', center=(center[0],center[1]+100),fontsize=50,color='white')


def player_control():
    if keyboard.RIGHT and not p.right> WIDTH:
        p.x+= ps
        p.angle= -10
    elif keyboard.LEFT and not p.left < 0 :
        p.x-= ps
        p.angle= 10   
    elif keyboard.UP and not p.top < 0:
        p.y-= ps
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y+= ps 
    else : 
        p.angle= 0  

def draw():
    screen.clear()
    if not game_started: 
        show_screen_1()
    elif game_started and not game_over:
        show_game_screen()
    elif game_over:
        show_game_over()
    
    

def update():
    global game_started
    if keyboard.SPACE and not game_started:
        game_started = True
        bg.image='peakpx'
    if game_started and not game_over:
       player_control()
       enemy_control()
        
    print (game_started, game_over)
   
def enemy_control():
    global game_over
    if p.x > e.x:
        e.x += es
    if p.x < e.x :
        e.x += -es
    if p.y > e.y:
        e.y += es
    if p.y < e.y :
        e.y += -es
    if p.colliderect(e):
        game_over = True



pgzrun.go()