# Imports the relevant modules
import turtle
import random
import time


# Sets the screen paramaters and creates a list of shuffled colors
WIDTH, HEIGHT = 800, 500
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "cyan", "pink"]
random.shuffle(COLORS)


# Gets the input from the user for the number of racers
def get_num_of_racers():
    total_racers = 0
    while True:
        total_racers = input("Enter the number of turtles to race (2 - 10): ")
        if total_racers.isdigit():
            total_racers = int(total_racers)
        else:
            print("Please enter a numerical value.")
            continue

        if 2 <= total_racers <= 10:
            return total_racers
        else:
            print("Please enter a value within the range")


# Creates the screen and field for the race
def innit_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgcolor("forestgreen")
    turtle.speed(0)

    #Heading
    turtle.penup()
    turtle.goto(-100, 205)
    turtle.color("white")
    turtle.write("TURTLE RACE", font=("Arial", 20, "bold"))

    #Dirt
    turtle.goto(-350, 200)
    turtle.pendown()
    turtle.color("chocolate")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(700)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()

    #Finish Line
    gap_size = 20
    turtle.shape("square")
    turtle.penup()

    #White Squares Row 1
    turtle.color("white")
    for i in range(10):
        turtle.goto(250, (170 - (i * gap_size * 2)))
        turtle.stamp()

    #White Squares Row 2
    for i in range(10):
        turtle.goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        turtle.stamp()

    #Black Squares Row 1
    turtle.color("black")
    for i in range(10):
        turtle.goto(250, (190 - (i * gap_size * 2)))
        turtle.stamp()

    #Black Squares Row 2
    for i in range(10):
        turtle.goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        turtle.stamp()


# Sets the speed of each turtle and races them, returning the winning turtle's color
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if x >= 225:
                for i in range(72):
                    racer.right(5)
                    racer.shapesize(2.5)
                return colors[turtles.index(racer)]


# Creates the turtle objects and sets their initial position
def create_turtles(colors):
    turtles = []
    spacingy = 400 // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.setpos((-700//2), (400//2 - (i + 1) * spacingy))
        racer.pendown()
        turtles.append(racer)

    return turtles

# Gets the number of racers from the user
racers = get_num_of_racers()

# Initiates the screen and racing field
innit_turtle()

# Sets the colors of the turtles
colors = COLORS[:racers]

# Races and prints the winning turtle
winner = race(colors)
print(f"The winner is the {winner} turtle!")
time.sleep(5)
