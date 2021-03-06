from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Create a turtle player that starts at the bottom of the screen.
    player = Player()
    car_manager = CarManager()
    # Create a scoreboard that keeps track of which level the user is on
    score = Scoreboard()

    screen.listen()
    screen.onkey(player.move_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        # Create cars
        car_manager.create_car()
        # Move to the left side of screen
        car_manager.move()
        # Detect when the turtle player collides with a car and stop the game if this happens.
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                # When turtle hits a car, GAME OVER.
                score.game_over()
        # Detect when turtle player has reached the finish line.
        if player.successful_cross():
            # Return the turtle to starting
            player.reset_player()
            # Increase speed of cars.
            car_manager.increase_speed()
            # Every time the player crosses the level increases.
            score.increase_level()
    play_again = screen.textinput(title="Choose", prompt="Would you like to play again? Type 'y' for yes, or 'n' for "
                                                         "no:")
    if play_again == 'y':
        screen.clear()
        main()
    else:
        screen.exitonclick()


main()
