from turtle import Turtle,Screen
import time

screen= Screen()
screen.setup(600,400)
screen.title("")
screen.title("The Snake Game")
screen.bgcolor("black")
n=3

sequences =[]
length=[(0,0),(-20,0),(-40,0)]
for n in range(3):
    sequence=Turtle()
    sequence.shape("square")
    sequence.color("white")
    sequence.goto(length[n])
    sequences.append(sequence)

# sequence.shape("square")
# sequence.color("white")
# sequence.goto(0,0)
# # sequences.append(sequence)

# sequence.shape("square")
# sequence.color("white")
# sequence.goto(-20,0)
# # sequences.append(sequence)

# sequence.shape("square")
# sequence.color("white")
# sequence.goto(-40,0)
# # sequences.append(sequence)


screen.exitonclick()
