
from turtle import Screen
from snake import New_Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My LeSnake game")
screen.tracer(0)

player = New_Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.turn_left, key="Left")
screen.onkey(fun=player.turn_right, key="Right")

game_is_on = True
while game_is_on:
   screen.update()
   time.sleep(0.1)
   player.moving()
   if player.head.distance(food) < 15:
       food.refresh()
       player.extend()
       scoreboard.increase_score()

   if player.head.xcor() > 280 or player.head.xcor() < -294 or player.head.ycor() > 294 or player.head.ycor() < -280:
    scoreboard.reset_score()
    player.reset()
   for segment in player.segments[1:]:
       if segment == player.head:
        pass
       elif player.head.distance(segment) < 10:
           scoreboard.reset_score()

           player.reset()

screen.exitonclick()

if __name__ == '__main__':
    print('Run the game here')
