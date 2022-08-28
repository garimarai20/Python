from turtle import speed
import pgzrun

HEIGHT=500
WIDTH=600

p=Actor('ironman',(100,100))
speed= 3
def draw():
    screen.fill('yellow')
    p.draw()

def update():
    player_control()

def player_control():
    if keyboard.RIGHT and not p.right> WIDTH:
        p.x+= speed
        p.angle= -10
    elif keyboard.LEFT and not p.left < 0 :
        p.x-= speed 
        p.angle= 10   
    elif keyboard.UP and not p.up < 0:
        p.y-= speed
    elif keyboard.DOWN and not p.down > HEIGHT:
        p.y+= speed 
    else : 
        p.angle= 0       

pgzrun.go()#outside the function
    