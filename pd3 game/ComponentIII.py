#Game Cell
#The Diamond
#Kanvir Singh, Gurpreet Singh, Rene Juarez San Migu
#Knight has to kill the devil that has attacked their kingdom.

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"The Diamond")
bk = Image("castle.png",game)
bk.resizeTo(game.width, game.height)
knight = Image("knight.png",game)
v = Image("volcano.png",game)
v.resizeTo(game.width, game.height)
devil = Image("Devil.png",game)
fb = Image("Fireball.png",game)
re = Image("re.png",game)
re.resizeTo(game.width, game.height)
brick = Image("brick.png",game)
knight.resizeBy(-80)
knight.moveTo(625,480)
brick.resizeBy(-80)
f= Font(red,20,yellow,"Castellar")
devil.resizeBy(-80)
devil.setSpeed(4,60)
s = Image("Spear.png",game)
c= Font(black,20,blue,"Castellar")
go = Image("go.jpg",game)


rock = []#empty list
for index in range(100):#add the images to the list
    rock.append(Image("brick.png",game))
for index in range(100):#set each item list
    rock[index].resizeBy(-90)
    x = randint(100,700)
    y = -randint(100,10000)
    rock[index].moveTo(x,y)
    s = randint(3,8)
    rock[index].setSpeed(s,180)
    
fire = []#empty list
for index in range(100):#add the images to the list
    fire.append(Image("Fireball.png",game))
for index in range(100):#set each item list
    fire[index].resizeBy(-90)
    x = randint(100,700)
    y = -randint(100,10000)
    fire[index].moveTo(x,y)
    s = randint(3,8)
    fire[index].setSpeed(s,180)
game.over = False

while not game.over:
    game.processInput()
    re.draw()
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.drawText("Press [SPACE BAR] to start the game",game.width/2-150,game.height/2+20,c)
    game.update(30)
    
game.over = False

#Level 1 - game loop
game.time = 100
while not game.over:
    game.processInput()
    bk.draw()
    knight.draw()
    game.displayTime(25,50,f)
    for index in range(len(rock)):
       rock[index].move()
       if rock[index].collidedWith(knight):
            knight.health-=10
            rock[index].visible=False
    game.drawText("Kinght's Health: " + str(knight.health),25,70,f)
    
    game.update(30)
    if keys.Pressed[K_LEFT]:
        knight.x -= 7
    if keys.Pressed[K_RIGHT]:
        knight.x += 7
    
    brick.draw()
    if knight.health<=0:
        game.over=True
    
while not game.over:
    game.processInput()
    
    go.draw()
    
    
    
    game.update(30)
    
game.quit()


