import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Final Lab"

VIEWPOINT_MARGIN = 220

CAMERA_SPEED = 0.5

PLAYER_MOVEMENT_SPEED = 5
JUMP_SPEED = 13

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


class InstructionView(arcade.View):
    pass


class GameView(arcade.View):
    """ Main Window """

    def __init__(self):
        """ Create the variables """

        # Init the parent class
        super().__init__()

        self.player_sprite = None

        self.player_list = None
        self.static_walls_list = None
        self.moving_walls_list = None
        self.coin_list = None

        self.tile_map = None

        self.score = 0

        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up everything with the game """
        self.player_list = arcade.SpriteList()
        self.static_walls_list = arcade.SpriteList()
        self.moving_walls_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        self.tile_map = arcade.load_tilemap("final_lab_3.json", scaling=SPRITE_SCALING)

        # Set wall and coin SpriteLists
        # Any other layers here. Array index must be a layer.
        self.static_walls_list = self.tile_map.sprite_lists["Static Walls"]
        self.moving_walls_list = self.tile_map.sprite_lists["Moving Walls"]
        self.coin_list = self.tile_map.sprite_lists["Coins"]
        # You're going to need to make some hit-list and junk for the new layer! good luck girl.

        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        all_walls_list = [self.static_walls_list, self.moving_walls_list]

        # Keep player from running through the wall_list layer
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, all_walls_list,
                                                             gravity_constant=.5)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        self.camera_sprites.use()

        self.player_list.draw()
        self.static_walls_list.draw()
        self.moving_walls_list.draw()
        self.coin_list.draw()

        self.camera_gui.use()
        arcade.draw_rectangle_filled(self.window.width // 2, 20, self.window.width, 40, arcade.color.ALMOND)
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK_BEAN, 20)

        if self.player_sprite.center_y <= -1:
            arcade.draw_text("Game Over", 200, 200, arcade.csscolor.BLACK)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()

        if self.player_sprite.center_y > -1:
            self.player_list.update()
            self.moving_walls_list.update()
            self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.window.width / 2, \
                   self.player_sprite.center_y - self.window.height / 2
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
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
