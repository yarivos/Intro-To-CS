from asteroid import Asteroid
import math
from screen import Screen
import sys
from ship import Ship
from torpedo import Torpedo
import random

# Constants
DEFAULT_ASTEROIDS_NUM = 20 
TURN_LEFT = 7
TURN_RIGHT = -7
MAX_ASTEROID_SPEED = 4
MIN_ASTEROID_SPEED = 1
START_ASTEROID_SIZE = 3
MAX_TORPEDO_AMOUNT = 10


class GameRunner:
    """this class runs the game, using Asteroid, Ship, Torpedo class"""

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship_loc_y = return_random_stuff(self.__screen_min_y, self.__screen_max_y)
        self.__ship_loc_x = return_random_stuff(self.__screen_min_x, self.__screen_max_x)
        self.__ship = Ship(0, 0, self.__ship_loc_x, self.__ship_loc_y, 0)  # the playing ship
        self.__asteroid_lst = []  # list for all asteroid objects currently playing
        self.asteroid_registration_beginning(asteroids_amount)  # inserting asteroids to the game
        self.__torpedo_lst = []  # list for all torpedo objects currently playing
        self.__points = 0

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        iterates the game
        """
        self.is_game_over()  # ends the game if no more asteroids in the game or Q was pressed
        self.draw_ship_in_iteration()
        self.draw_asteroids_in_iteration()
        self.draw_torpedo_in_iteration()

    def is_game_over(self):
        if len(self.__asteroid_lst) == 0:
            self.__screen.show_message("No More Asteroids", "You have won the game with "
                                       + str(self.__points) + " points!")
            self.__screen.end_game()
            sys.exit()
        if self.__screen.should_end():
            self.__screen.show_message("Q Was Pressed", "Hope to see you later")
            self.__screen.end_game()
            sys.exit()

    def draw_torpedo_in_iteration(self):
        """
        adds new torpedo to the game and draws it
        removes it when life_time is equal to zero
        """
        if self.__screen.is_space_pressed() and \
                len(self.__torpedo_lst) < MAX_TORPEDO_AMOUNT:  # checks if torpedo exceeds maximum amount
            new_torpedo = Torpedo(self.__ship.get_speed_x(), self.__ship.get_speed_y(),
                                  self.__ship.get_location_x(), self.__ship.get_location_y(),
                                  self.__ship.get_heading())
            self.__screen.register_torpedo(new_torpedo)
            self.__torpedo_lst.append(new_torpedo)
        for torpedo in self.__torpedo_lst:  # iterates over all the torpedos in the game
            self.move_object(torpedo)
            loc_x = torpedo.get_location_x()
            loc_y = torpedo.get_location_y()
            heading = torpedo.get_heading()
            self.__screen.draw_torpedo(torpedo, loc_x, loc_y, heading)  # draw torpedo
            torpedo.reduce_life_time()
            if torpedo.get_life_time() <= 0:  # deletes the torpedo if life_time = 0
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedo_lst.remove(torpedo)

    def draw_ship_in_iteration(self):
        """
        all of ship functions happen here, move, draw, accelerate
        """
        self.move_object(self.__ship)  # change ship location
        self.speed_up_ship(self.__ship)  # change ship speed
        self.change_heading()  # change ship heading
        loc_x = self.__ship.get_location_x()
        loc_y = self.__ship.get_location_y()
        heading = self.__ship.get_heading()
        self.__screen.draw_ship(loc_x, loc_y, heading)  # draws the ship on screen

    def draw_asteroids_in_iteration(self):
        """
        function moves the asteroids and draws them, checks for any 
        collisions with an asteroid
        """
        for asteroid in self.__asteroid_lst:
            self.move_object(asteroid)
            self.__screen.draw_asteroid(asteroid, asteroid.get_location_x(), asteroid.get_location_y())
            self.torpedo_hit_asteroid(asteroid)
            self.ship_ast_collision(asteroid)

    def ship_ast_collision(self, asteroid):
        """
        if collision made with no extra life game is over, else reduce ship_life. 
        removes collided asteroid
        """
        if asteroid.has_intersection(self.__ship):
            self.__ship.reduce_life()
            if self.__ship.get_life() < 0:  # checks if game is over
                self.__screen.show_message("Out of Life", "You have lost the game with "
                                           + str(self.__points) + " points!")
                self.__screen.end_game()
                sys.exit()
            self.__screen.remove_life()  # reduces 1  extra life sign from screen
            self.__screen.show_message("COLLISION", "You have collided with an asteroid \nBe Careful!")
            self.__screen.unregister_asteroid(asteroid)  # unregisters the collided asteroid
            self.__asteroid_lst.remove(asteroid)  # removes the asteroid from the list

    def torpedo_hit_asteroid(self, asteroid):
        """
        after hitting asteroid with a torpedo function will
        remove the torpedo
        calls asteroid split
        removes the "hit" asteroid
        add points
        """
        for torpedo in self.__torpedo_lst:
            if asteroid.has_intersection(torpedo):
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedo_lst.remove(torpedo)  # removes torpedo after colliding an asteroid
                self.add_points(asteroid)  # add points according to asteroid size
                if asteroid.get_size() != 1:
                    self.split_asteroid(torpedo, asteroid)
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroid_lst.remove(asteroid)  # removes the collided asteroid

    def add_points(self, asteroid):
        """
        add points after hitting an asteroid with a torpedo
        """
        if asteroid.get_size() == 3:
            self.__points += 20
        elif asteroid.get_size() == 2:
            self.__points += 50
        elif asteroid.get_size() == 1:
            self.__points += 100
        self.__screen.set_score(self.__points)  # sets new score on the screen

    def split_asteroid(self, torpedo, asteroid):
        """
        splits the asteroid to to small asteroids after hitting it with torpedo
        function adds the new asteroids to the game
        """
        asteroid_speed_x = (torpedo.get_speed_x() + asteroid.get_speed_x()) / \
                           math.sqrt((asteroid.get_speed_x() ** 2) +
                                     (asteroid.get_speed_y() ** 2))
        asteroid_speed_y = (torpedo.get_speed_y() + asteroid.get_speed_y()) / \
                           math.sqrt((asteroid.get_speed_x() ** 2) +
                                     (asteroid.get_speed_y() ** 2))
        loc_x = asteroid.get_location_x()
        loc_y = asteroid.get_location_y()
        new_asteroid_1 = Asteroid(asteroid_speed_x, loc_x,
                                  asteroid_speed_y, loc_y, asteroid.get_size() - 1)
        new_asteroid_2 = Asteroid(-asteroid_speed_x, loc_x,
                                  -asteroid_speed_y, loc_y, asteroid.get_size() - 1)
        self.__screen.register_asteroid(new_asteroid_1, asteroid.get_size() - 1)
        self.__screen.register_asteroid(new_asteroid_2, asteroid.get_size() - 1)
        self.__asteroid_lst.append(new_asteroid_1)
        self.__asteroid_lst.append(new_asteroid_2)  # asteroid is added to the game

    def move_object(self, obj):
        """ this method changes the location of an object """
        new_x = self.__screen_min_x + (obj.get_location_x() +
                                       obj.get_speed_x() - self.__screen_min_x) \
                % (self.__screen_max_x - self.__screen_min_x)
        new_y = self.__screen_min_y + (obj.get_location_y() +
                                       obj.get_speed_y() - self.__screen_min_y) \
                % (self.__screen_max_y - self.__screen_min_y)
        obj.set_location_x(new_x)
        obj.set_location_y(new_y)

    def asteroid_registration_beginning(self, asteroids_amount):
        """
        initializing the asteroids in the beginning of the game,
        adds the asteroids to asteroid list, and the screen
        """
        for i in range(asteroids_amount):
            ast_speed_x = return_random_stuff(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
            ast_speed_y = return_random_stuff(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
            ast_location_x = return_random_stuff(self.__screen_min_x, self.__screen_max_x)
            ast_location_y = return_random_stuff(self.__screen_min_y, self.__screen_max_y)
            while ast_location_x == self.__ship_loc_x and ast_location_y == self.__ship_loc_y:
                ast_location_x = return_random_stuff(self.__screen_min_x, self.__screen_max_x)
                ast_location_y = return_random_stuff(self.__screen_min_y, self.__screen_max_y)
            current_asteroid = Asteroid(ast_speed_x, ast_location_x, ast_speed_y, ast_location_y, START_ASTEROID_SIZE)
            self.__screen.register_asteroid(current_asteroid, START_ASTEROID_SIZE)
            self.__asteroid_lst.append(current_asteroid)

    def change_heading(self):
        """
        changes the heading of the ship according to user's orders
        """
        if self.__screen.is_left_pressed():
            self.__ship.set_heading(TURN_LEFT)  # add 7 to heading
        if self.__screen.is_right_pressed():
            self.__ship.set_heading(TURN_RIGHT)  # subtract 7 to heading

    def speed_up_ship(self, ship):
        """ This method is used to change the speed of the ship according to the 
        input from the user """
        if self.__screen.is_up_pressed():
            new_x_speed = ship.get_speed_x() + math.cos(math.radians(ship.get_heading()))
            new_y_speed = ship.get_speed_y() + math.sin(math.radians(ship.get_heading()))
            ship.set_speed_x(new_x_speed)
            ship.set_speed_y(new_y_speed)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


def return_random_stuff(min_val, max_val):
    return random.randint(min_val, max_val)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
