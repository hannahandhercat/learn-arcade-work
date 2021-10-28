""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER_FISH = 0.5
SPRITE_SCALING_GREEN_FISH = 0.3
SPRITE_SCALING_SLIME = 0.3
GREEN_FISH_COUNT = 50
SLIME_COUNT = 50
MOVEMENT_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        arcade.set_background_color(arcade.csscolor.MEDIUM_AQUAMARINE)

        self.set_mouse_visible(False)

        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

        self.player_sprite = None
        self.score = 0

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("fishPink.png", SPRITE_SCALING_PLAYER_FISH)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(GREEN_FISH_COUNT):
            fish = GreenFish("fishGreen.png", SPRITE_SCALING_GREEN_FISH)

            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(SCREEN_HEIGHT)

            self.good_sprite_list.append(fish)

        for i in range(SLIME_COUNT):
            slime = Slime("slimeGreen.png", SPRITE_SCALING_SLIME)

            slime.center_x = random.randrange(SCREEN_WIDTH)
            slime.center_y = random.randrange(SCREEN_HEIGHT)

            self.bad_sprite_list.append(slime)

    def on_draw(self):
        arcade.start_render()

        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.csscolor.BLACK, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        if len(self.good_sprite_list) > 0:
            self.good_sprite_list.update()
            self.bad_sprite_list.update()
        elif len(self.good_sprite_list) <= 0:
            arcade.draw_text("GAME OVER", 300, 400, arcade.csscolor.BLACK, 14)

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)

        for fish in good_hit_list:
            fish.remove_from_sprite_lists()
            self.score += 1

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)

        for slime in bad_hit_list:
            slime.remove_from_sprite_lists()
            self.score -= 1


class GreenFish(arcade.Sprite):

    def update(self):
        self.center_x -= 1

        if self.right < 0:
            self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
            self.center_y = random.randrange(SCREEN_HEIGHT)


class Slime(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()