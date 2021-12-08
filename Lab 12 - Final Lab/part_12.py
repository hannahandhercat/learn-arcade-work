import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Final Lab"

VIEWPOINT_MARGIN = 220

CAMERA_SPEED = 0.5

PLAYER_MOVEMENT_SPEED = 5

TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING
        self.textures = []

        # Create the textures for the player sprite to dictate which way the sprite faces.
        texture = arcade.load_texture("femaleAdventurer_idle.png")
        self.textures.append(texture)

        texture = arcade.load_texture("femaleAdventurer_idle.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = texture

    def update(self):
        """Update so that the player faces right or left when moving right or left."""
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]


class MyGame(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)

        self.player_sprite = None

        self.player_list = None
        self.static_walls_list = None
        self.moving_walls_list = None

        self.tile_map = None

        self.score = 0

        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up everything with the game """
        self.player_list = arcade.SpriteList()
        self.static_walls_list = arcade.SpriteList()
        self.moving_walls_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        self.tile_map = arcade.load_tilemap("final_lab_3.json", scaling=SPRITE_SCALING)

        # Set wall and coin SpriteLists
        # Any other layers here. Array index must be a layer.
        self.static_walls_list = self.tile_map.sprite_lists["Static Walls"]

        """self.moving_walls_list = self.tile_map.sprite_lists["Moving Walls"]
        self.all_walls_list.append(self.moving_walls_list)"""

        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        all_walls_list = [self.static_walls_list]

        # Keep player from running through the wall_list layer
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, all_walls_list,
                                                             gravity_constant=.5)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        self.player_list.draw()
        self.static_walls_list.draw()
        self.moving_walls_list.draw()

        self.camera_sprites.use()
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
        """ Movement and game logic """
        self.physics_engine.update()
        self.moving_walls_list.update()
        self.player_list.update()

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
