###############################################################################
######################         ----------------         #######################
######################         |SPACE INVADERS|         #######################
######################         ----------------         #######################
###############################################################################

# Modules Used
import turtle
import os
import math
import random
import winsound
import threading

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("E:/python/space.gif")

# Register the sounds
laser_gun = "E:/python/laser_gun.wav"
explode = "E:/python/explode.wav"

# Register the shapes
turtle.register_shape("E:/python/player.gif")
turtle.register_shape("E:/python/enemy.gif")
# Create the borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(0, 4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score to zero
score = 0

# Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score : %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Player
player = turtle.Turtle()
player.color("blue")
player.shape("E:/python/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15

# Choose no.of enemies
num_of_enemies = 5

# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(num_of_enemies):
    # Create enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("E:/python/enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# Set enemy speed
enemyspeed = 2


# Create player weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# move player left and right


def move_left():
    x = player.xcor()
    x -= playerspeed
    if(x < -280):
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if(x > 280):
        x = 280
    player.setx(x)


def fire_bullet():
    # declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move the bullet to the just above of player
        winsound.PlaySound(laser_gun, winsound.SND_FILENAME)
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Check if there is a collision


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")
wn.listen()
# wn.mainloop()

# Main game loop
while True:
    for enemy in enemies:
        # move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        # move enemy back and down
        if enemy.xcor() > 275:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            if enemy.ycor() < -275:
                enemy.sety(-275)
            # change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -275:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            if enemy.ycor() < -275:
                enemy.sety(-275)
            # change enemy direction
            enemyspeed *= -1

        # check for a collision between enemy and bullet
        if isCollision(bullet, enemy):
            # reset the bullet
            winsound.PlaySound(explode, winsound.SND_FILENAME)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            score += 10
            scorestring = "Score : %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        # Not nessasary Code
        #   if __name__ == '__main__':
            # creating thread
        #      th1=threading.Thread(target=ifCollision)
        #      th2=threading.Thread(target=explode)
        #   th1.start()
        #   th2.start()

        if isCollision(player, enemy):
            player.hideturtle()
            bullet.hideturtle()
            for ey in enemies:
                ey.hideturtle()
            game_over = turtle.Turtle()
            game_over.speed(0)
            game_over.color("red")
            game_over.penup()
            gamestring = "Game Over!! \n\nScore:%s" % score
            game_over.write(gamestring, False, align="left", font=("Arial", 20, "normal"))
            game_over.hideturtle()
            breaker = 10
            break
    # move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    # check if bullet has gone top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
if(breaker == 10):
    print(quit)
else:
    wn.mainloop()
delay = input("Press enter")
