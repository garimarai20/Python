import pgzrun

HEIGHT= 500
WIDTH= 600 

music.play('bgmusic')

p=Actor('ufo',(100,100))

score=0
speed= 3
def draw():
    screen.fill('black')
    p.draw
    screen.draw.text(f'score:{score}',(WIDTH-80,10))

def update():
    player_control()
   



   
def player_control():
    if keyboard.RIGHT and not p.right> WIDTH:
        p.x+= speed
        p.angle= -10
    elif keyboard.LEFT and not p.left < 0 :
        p.x-= speed 
        p.angle= 10   
    elif keyboard.UP and not p.top < 0:
        p.y-= speed
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y+= speed 
    else : 
        p.angle= 0       

pgzrun.go()#outside the function
    