from turtle import Screen
import time
from snake import Snake
from food import Food
from score_bord import ScoreBord

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score_bord = ScoreBord()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score_bord.score_increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score_bord.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_bord.game_over()

screen.exitonclick()
