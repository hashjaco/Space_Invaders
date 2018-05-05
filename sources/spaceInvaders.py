import turtle
import os
import math
import random


# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("spaceBackgroundResize.gif")
# window.screensize(600, 600)
os.system("afplay neoncat.wav&")
# Register the shapes
turtle.register_shape("invader-animated-red.gif")
turtle.register_shape("enemyShip.gif")
turtle.register_shape("neoncat.gif")

# Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# Set up scoring
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scoreString = "Score: %s" % score
score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Create players

player = turtle.Turtle()
player.color("blue")
player.shape("enemyShip.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

enemySpeed = 2

# Create multiple enemies
numberOfEnemies = 5

# Create an empty list
enemies = []


# Create enemies
for i in range(numberOfEnemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader-animated-red.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, -200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# Create bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("neoncat.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20
bulletstate = "ready"


# define bullet state
# ready to fire
# fire - is firing
# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay quick_fart_x.wav&")
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10

        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Key listener
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

# Main Loop
while True:

    for enemy in enemies:
        # Enemy movement (up and down
        y = enemy.ycor()
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)
        if enemy.xcor() > 280:
            y -= 40
            enemy.sety(y)
            enemySpeed *= -1
        if enemy.xcor() < -280:
            y -= 40
            enemy.sety(y)
            enemySpeed *= -1
        if isCollision(bullet, enemy):
            os.system("afplay explosion_x.wav&")
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset Enemy
            x = random.randint(-200, -200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

            # Update score
            score += 10
            scoreString = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            # Sound effect
            os.system("afplay OH-MY-GAH.wav&")
            # Hide Enemy and Player
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    if bulletstate == "fire":
        # Accelerate bullet
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)
    if bullet.ycor() > 275:
        # Hide bullet if it goes out of bounds
        bullet.hideturtle()
        bulletstate = "ready"


wn.mainloop()
if exit(window):
    os.system("afstop neoncat.wav")

