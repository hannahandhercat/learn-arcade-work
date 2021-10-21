""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.csscolor.BLACK)

        self.alien = Alien(550, 50, 0, 0, 10, arcade.csscolor.GREEN)
        self.spaceship = Spaceship(50, 50, 15, arcade.csscolor.SLATE_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_arc_filled(300, 0, 650, 400, arcade.csscolor.WHITE_SMOKE, 0, 180)
        arcade.draw_circle_outline(100, 70, 30, arcade.csscolor.GREY, 4)
        arcade.draw_circle_outline(300, 100, 80, arcade.csscolor.GREY, 5)
        arcade.draw_circle_outline(500, 30, 50, arcade.csscolor.GREY, 4)
        arcade.draw_circle_filled(150, 500, 30, arcade.csscolor.YELLOW)
        self.spaceship.draw()
        self.alien.draw()
        arcade.finish_render()

    def update(self, delta_time):
        self.alien.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.spaceship.position_x = x
        self.spaceship.position_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.alien.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.alien.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.alien.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.alien.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.alien.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.alien.change_y = 0


class Spaceship:
    def __init__(self, position_x, position_y, radius, color,):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 20, 20, 20, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 10, 10, 20, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 40, 24, 30, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius - 5, arcade.csscolor.GREY)
        arcade.draw_circle_outline(self.position_x, self.position_y, self.radius - 5, arcade.csscolor.BLACK, 2)


class Alien:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_arc_filled(self.position_x, self.position_y, 40, 30, self.color, 0, 180)
        arcade.draw_rectangle_filled(self.position_x - 10, self.position_y + 10, 5, 20, self.color)
        arcade.draw_rectangle_filled(self.position_x + 10, self.position_y + 10, 5, 20, self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x


def main():
    window = MyGame()
    arcade.run()


main()