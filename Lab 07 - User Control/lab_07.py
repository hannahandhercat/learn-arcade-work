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

        # Define instances of the classes "Spaceship" and "Alien".
        self.alien = Alien(550, 50, 0, 0, 10, arcade.csscolor.GREEN)
        self.spaceship = Spaceship(50, 50, 15, arcade.csscolor.GHOST_WHITE)

        # Load sounds and define when the "alien sound" plays.
        self.spaceship_sound = arcade.load_sound("arcade_resources_sounds_laser2.wav")
        self.alien_sound = arcade.load_sound("arcade_resources_sounds_laser1.wav")
        self.off_screen_sound = arcade.load_sound("arcade_resources_sounds_error5.wav")
        self.alien_sound_player = None

    def on_draw(self):
        """Draw the background, spaceship, and alien."""
        arcade.start_render()
        arcade.draw_arc_filled(300, 0, 650, 400, arcade.csscolor.LIGHT_GRAY, 0, 180)
        arcade.draw_circle_outline(100, 70, 30, arcade.csscolor.GREY, 4)
        arcade.draw_circle_outline(300, 100, 80, arcade.csscolor.GREY, 5)
        arcade.draw_circle_outline(500, 30, 50, arcade.csscolor.GREY, 4)
        arcade.draw_circle_filled(150, 500, 30, arcade.csscolor.YELLOW)
        self.spaceship.draw()
        self.alien.draw()
        arcade.finish_render()

    def update(self, delta_time):
        """Define when the off screen sound plays for the alien."""
        self.alien.update()
        if self.alien.position_x == self.alien.radius:
            if not self.alien_sound_player or not self.alien_sound_player.playing:
                self.alien_sound_player = arcade.play_sound(self.off_screen_sound)
        if self.alien.position_x == SCREEN_WIDTH - self.alien.radius:
            if not self.alien_sound_player or not self.alien_sound_player.playing:
                self.alien_sound_player = arcade.play_sound(self.off_screen_sound)
        if self.alien.position_y == self.alien.radius:
            if not self.alien_sound_player or not self.alien_sound_player.playing:
                self.alien_sound_player = arcade.play_sound(self.off_screen_sound)
        if self.alien.position_y == SCREEN_HEIGHT - self.alien.radius:
            if not self.alien_sound_player or not self.alien_sound_player.playing:
                self.alien_sound_player = arcade.play_sound(self.off_screen_sound)

    def on_mouse_motion(self, x, y, dx, dy):
        """Set the spaceship position to where the mouse is."""
        self.spaceship.position_x = x
        self.spaceship.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """Play spaceship sound when the mouse is pressed."""
        arcade.play_sound(self.spaceship_sound)

    def on_key_press(self, key, modifiers):
        """Define which way the alien moves based on what key is pressed."""
        if key == arcade.key.LEFT:
            self.alien.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.alien.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.alien.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.alien.change_y = -MOVEMENT_SPEED
        if key == arcade.key.SPACE:
            arcade.play_sound(self.alien_sound)

    def on_key_release(self, key, modifiers):
        """Define how the alien stops moving when a key is released."""
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.alien.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.alien.change_y = 0


class Spaceship:
    """Define the Spaceship class."""
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
    """Define the Alien class."""
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
        arcade.draw_rectangle_filled(self.position_x - 7, self.position_y - 2, 10, 20, self.color)
        arcade.draw_rectangle_filled(self.position_x + 7, self.position_y - 2, 10, 20, self.color)
        arcade.draw_circle_outline(self.position_x, self.position_y + 8, self.radius - 3, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(self.position_x, self.position_y + 8, self.radius - 5, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(self.position_x, self.position_y + 8, self.radius -7, arcade.csscolor.BLACK)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        # Keep the aline from moving off screen.
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


def main():
    window = MyGame()
    arcade.run()


main()