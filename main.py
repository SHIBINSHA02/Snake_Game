import turtle
from snake import Snake
import time
from food import Food


window = turtle.Screen()
window.bgcolor("black")
window.title("My Snake Game")
window.setup(width=600,height=600)
window.tracer(0)
window.listen()
snake=Snake()

food= Food()

window.onkey(snake.up,"Up")
window.onkey(snake.down,"Down")
window.onkey(snake.left,"Left")
window.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    time.sleep(0.5)
    window.update()
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        game_is_on=False
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
           









window.exitonclick()
