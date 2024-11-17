import pgzrun
import random
WIDTH=500
HEIGHT=500
sCORE=0
GAME_OVER=False
Bumblebee=Actor("C:/Users/17657/OneDrive/Desktop/game dev/images/bee.png")
Bumblebee.pos=(100,100)
Tulip=Actor("C:/Users/17657/OneDrive/Desktop/game dev/images/flower.png")
Tulip.pos=(200,200)
def draw():
    screen.blit("C:/Users/17657/OneDrive/Desktop/game dev/images/background.png",(0,0))
    Tulip.draw()
    Bumblebee.draw()
    screen.draw.text("SCORE:"+str(sCORE),color="blue",topleft=(10,10))
    if GAME_OVER:
        screen.fill("pink")
        screen.draw.text("Time up! Your final score is"+str(sCORE),midtop=(WIDTH/2,10),fontsize=40,color="red")
def place_flower():
    Tulip.x=random.randint(70,(WIDTH-70))
    Tulip.y=random.randint(70,(HEIGHT-70))
def time_up():
    global GAME_OVER
    GAME_OVER=True
def update():
    global sCORE
    if keyboard.left:
        Bumblebee.x=Bumblebee.x-2
    if keyboard.right:
        Bumblebee.x=Bumblebee.x+2
    if keyboard.up:
        Bumblebee.y=Bumblebee.y-2
    if keyboard.down:
        Bumblebee.y=Bumblebee.y+2
    Tulip_collected=Bumblebee.colliderect(Tulip)
    if Tulip_collected:
        sCORE=sCORE+10
        place_flower()
clock.schedule(time_up,100)
pgzrun.go()