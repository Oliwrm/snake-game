from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.update()

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

playing= True
while playing:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.segments[0].distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    #detect collision with wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()