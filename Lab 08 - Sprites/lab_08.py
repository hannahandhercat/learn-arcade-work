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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Collect the Fish!")

        arcade.set_background_color(arcade.csscolor.MEDIUM_AQUAMARINE)

        self.set_mouse_visible(False)

        # Create player, "good" sprite, and "bad" sprite lists.
        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

        # Create player sprite list and set the score to 0.
        self.player_sprite = None
        self.score = 0

        # Load the sounds that play when you hit a good or bad sprite.
        self.good_sound = arcade.load_sound("good_sprite_sound.wav")
        self.bad_sound = arcade.load_sound("bad_sprite_sound.wav")

    def setup(self):

        # Set the previously created lists to instances of the arcade SpriteList class.
        self.player_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        self.score = 0

        # Set the player sprite to the fishPink.png, scale it, place it, and add it to the player list.
        self.player_sprite = arcade.Sprite("fishPink.png", SPRITE_SCALING_PLAYER_FISH)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(GREEN_FISH_COUNT):

            # Generate the green fish count randomly around the game and add it to the good sprite list.
            fish = GreenFish("fishGreen.png", SPRITE_SCALING_GREEN_FISH)

            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(SCREEN_HEIGHT)

            self.good_sprite_list.append(fish)

        for i in range(SLIME_COUNT):

            # Generate the slime and add them to the bad sprite list.
            slime = Slime("slimeGreen.png", SPRITE_SCALING_SLIME)

            slime.center_x = SCREEN_WIDTH / 2
            slime.center_y = i * 20

            if i % 2 == 0:
                slime.change_x = -3
            else:
                slime.change_x = 3

            slime.change_y = 3

            self.bad_sprite_list.append(slime)

    def on_draw(self):

        # Start the render and drew the good sprite, bad sprite, and player lists.
        arcade.start_render()

        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        self.player_list.draw()

        # Draw the score.
        output = f"Score: {self.score}"
        if len(self.good_sprite_list) > 0:
            arcade.draw_text(output, 10, 20, arcade.csscolor.BLACK, 14)
        if len(self.good_sprite_list) <= 0:
            arcade.draw_text("Game Over", 225, 350, arcade.csscolor.BLACK, 48)
            arcade.draw_text(f"Score: {self.score}", 250, 250, arcade.csscolor.BLACK, 48)

    def on_mouse_motion(self, x, y, dx, dy):

        # Set the player sprite to move with the mouse movement.
        if len(self.good_sprite_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):

        # Tell the game to update only when there are still sprites in the good sprite list.
        if len(self.good_sprite_list) > 0:
            self.good_sprite_list.update()
            self.bad_sprite_list.update()

        # If there are no more sprites in the good sprite list then stop updating and display "Game Over"
        elif len(self.good_sprite_list) == 0:
            arcade.draw_text("Game Over", 300, 300, arcade.csscolor.BLACK, 14)

        # Set the mouse visible when the game stops updating.
        elif len(self.good_sprite_list) <= 0:
            self.set_mouse_visible(True)

        # Create a good hit list that checks for collision of the player sprite and the good sprite.
        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)

        # For every fish hit, add 1 to the score, remove from the good sprite list, and play the good sound.
        for fish in good_hit_list:
            fish.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.good_sound)

        # Create a bad hit list that checks for collision of the player sprite and the bad sprite.
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)

        # For every slime hit, remove 1 to the score, remove from the bad sprite list, and play the bad sound.
        for slime in bad_hit_list:
            slime.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.bad_sound, 2)


class GreenFish(arcade.Sprite):
    """Create the GreenFish class and define how it moves in the update method."""
    def update(self):
        self.center_x -= 1

        if self.right < 0:
            self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
            self.center_y = random.randrange(SCREEN_HEIGHT)


class Slime(arcade.Sprite):
    """Create the Slime class and define how it moves in the update method."""
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
