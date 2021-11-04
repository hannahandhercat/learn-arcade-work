import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 09"

VIEWPOINT_MARGIN = 220

CAMERA_SPEED = 0.1

PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        """Initializer"""
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

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

        # Set up the player
        self.player_sprite = arcade.Sprite("slimeBlue.png", SPRITE_SCALING)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
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

        for x in range(200, 500, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 500
            self.wall_list.append(slime_wall)
        for x in range(700, 1000, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 500
            self.wall_list.append(slime_wall)
        for x in range(500, 700, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 200
            self.wall_list.append(slime_wall)
        for x in range(500, 700, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 400
            self.wall_list.append(slime_wall)
        for x in range(200, 500, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 300
            self.wall_list.append(slime_wall)
        for x in range(700, 1100, 50):
            slime_wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
            slime_wall.center_x = x
            slime_wall.center_y = 300
            self.wall_list.append(slime_wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        arcade.start_render()

        self.camera_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()

        self.camera_gui.use()

        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)

        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

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

        self.physics_engine.update()

        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(lower_left_corner, CAMERA_SPEED)

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
