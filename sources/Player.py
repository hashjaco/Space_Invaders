import turtle

window = turtle.Screen()
window.bgcolor("red")
window.title("Player class")


class Player(turtle.Turtle()):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.speed = 1
        self.color("green")

    def move(self):
        self.forward(self.speed)

    def turn_left(self):
        self.left(30)

    def turn_right(self):
        self.right(30)

    def increase_speed(self):
        self.speed += 1


# Initialize new player object
player = Player()
# Set key bindings
window.listen()
window.onkey(player.turn_left, "Left")
window.onkey(player.turn_right, "Right")
window.onkey(player.increase_speed, "Up")

# Main Loop
while True:
    player.move()
