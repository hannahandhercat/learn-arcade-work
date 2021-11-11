import random
import arcade

SPRITE_SCALING = 0.5
BIG_ROCK_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 09"

VIEWPOINT_MARGIN = 220

CAMERA_SPEED = 0.1

PLAYER_MOVEMENT_SPEED = 5

TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1


class Slime(arcade.Sprite):
    """Create the class "Slime" for the player sprite."""

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING
        self.textures = []

        # Create the textures for the player sprite to dictate which way the sprite faces.
        texture = arcade.load_texture("slimeBlue.png")
        self.textures.append(texture)

        texture = arcade.load_texture("slimeBlue.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = texture

    def update(self):
        """Update so that the player faces right or left when moving right or left."""
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        """Initializer"""
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        self.gem_sound = arcade.load_sound("get_gem.wav")

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Slime()
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # Create a barrier of saws.
        for item in range(175, 1200, 50):
            saw = arcade.Sprite("sawHalf.png", SPRITE_SCALING)
            saw.center_x = item
            saw.center_y = 175
            self.wall_list.append(saw)
        for item in range(175, 800, 50):
            saw = arcade.Sprite("sawHalf.png", SPRITE_SCALING, angle=270)
            saw.center_x = 175
            saw.center_y = item
            self.wall_list.append(saw)
        for item in range(175, 1200, 50):
            saw = arcade.Sprite("sawHalf.png", SPRITE_SCALING, flipped_vertically=True)
            saw.center_x = item
            saw.center_y = 775
            self.wall_list.append(saw)
        for item in range(175, 800, 50):
            saw = arcade.Sprite("sawHalf.png", SPRITE_SCALING, angle=90)
            saw.center_x = 1175
            saw.center_y = item
            self.wall_list.append(saw)

        # Bottom row of slime blocks.
        for x in range(200, 500, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 250
            self.wall_list.append(slime_wall)
        for x in range(550, 750, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 250
            self.wall_list.append(slime_wall)
        for x in range(800, 1200, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 250
            self.wall_list.append(slime_wall)

        # Slime blocks directly above the bottom row of slime blocks.
        for x in range(200, 600, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 400
            self.wall_list.append(slime_wall)
        for x in range(700, 1200, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 400
            self.wall_list.append(slime_wall)

        # Row of slime blocks underneath the top row of slime blocks.
        for x in range(200, 450, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 550
            self.wall_list.append(slime_wall)
        for x in range(500, 900, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 550
            self.wall_list.append(slime_wall)
        for x in range(975, 1100, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 550
            self.wall_list.append(slime_wall)

        # Top row of slime blocks.
        for x in range(200, 700, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 700
            self.wall_list.append(slime_wall)
        for x in range(800, 1000, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 700
            self.wall_list.append(slime_wall)
        for x in range(1050, 1200, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 700
            self.wall_list.append(slime_wall)

        # Create various barrier rocks.
        rock = arcade.Sprite("meteorGrey_big1.png", SPRITE_SCALING)
        rock.center_x = 700
        rock.center_y = 190
        self.wall_list.append(rock)

        rock = arcade.Sprite("meteorGrey_big1.png", SPRITE_SCALING)
        rock.center_x = 800
        rock.center_y = 750
        self.wall_list.append(rock)

        rock = arcade.Sprite("meteorGrey_big1.png", BIG_ROCK_SCALING)
        rock.center_x = 525
        rock.center_y = 610
        self.wall_list.append(rock)

        # Create gems and place them.
        for i in range(3):
            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING)
            gem_placed_successfully = False
            while not gem_placed_successfully:
                gem.center_x = random.randrange(250, 1150)
                gem.center_y = 200
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)
                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    gem_placed_successfully = True
            self.gem_list.append(gem)

        for i in range(5):
            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING)
            gem_placed_successfully = False
            while not gem_placed_successfully:
                gem.center_x = random.randrange(200, 1150)
                gem.center_y = 325
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)
                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    gem_placed_successfully = True
            self.gem_list.append(gem)

        for i in range(5):
            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING)
            gem_placed_successfully = False
            while not gem_placed_successfully:
                gem.center_x = random.randrange(200, 1150)
                gem.center_y = 475
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)
                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    gem_placed_successfully = True
            self.gem_list.append(gem)

        for i in range(5):
            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING)
            gem_placed_successfully = False
            while not gem_placed_successfully:
                gem.center_x = random.randrange(200, 1150)
                gem.center_y = 625
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)
                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    gem_placed_successfully = True
            self.gem_list.append(gem)

        for i in range(2):
            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING)
            gem_placed_successfully = False
            while not gem_placed_successfully:
                gem.center_x = random.randrange(200, 1150)
                gem.center_y = 750
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)
                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    gem_placed_successfully = True
            self.gem_list.append(gem)

        # Apply the physics engine.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        """
        Draw the walls, sprites, score, and gems, and use the camera.
        """
        arcade.start_render()

        self.camera_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        self.camera_gui.use()

        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Update lists and create and add to the gem_hit_list."""
        self.physics_engine.update()
        self.gem_list.update()
        self.player_list.update()

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)

        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        """
        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
            Resize window
            Handle the user grabbing the edge and resizing the window.
            """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
