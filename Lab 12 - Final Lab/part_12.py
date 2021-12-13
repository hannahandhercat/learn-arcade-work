import arcade

# Credit:
# Sprite assets downloaded from kenny.nl; "Jumper pack"
# Sprite assets downloaded from arcade.academy; ":resources:images/tiles/"
# Sprite assets downloaded from arcade.academy; ":resources:images/animated_characters/female_adventurer/"
# Sound effect assets downloaded from OpenGameArt.org; "512 Sound Effects (8-bit style)"
# Music assets downloaded from OpenGameArt.org; "Platformer Game Music Pack"

# Create the constant variables.
SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "World Jump"

VIEWPOINT_MARGIN = 220

CAMERA_SPEED = 0.5

PLAYER_MOVEMENT_SPEED = 5
JUMP_SPEED = 13

TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1

SCORE = 0


class Player(arcade.Sprite):
    """ Create and define the class for your player sprite."""
    def __init__(self):

        # Init the parent class.
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
    """ Create the opening screen."""
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Welcome to World Jump", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Collect carrots and reach the coins!", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Press any key to start", self.window.width / 2, self.window.height / 2 - 150,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        """ If the user presses a key start the game. """
        level_view = LevelOneView()
        level_view.setup()
        self.window.show_view(level_view)


class GameOverView(arcade.View):
    """ Create the Game over screen."""
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Game Over", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press any key to start over", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key: int, modifiers: int):
        """ If the user presses the mouse button, start the game. """
        level_view = LevelOneView()
        level_view.setup()
        self.window.show_view(level_view)


class LevelOneCompleteView(arcade.View):
    """ Create the level one completion screen."""
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Level One Complete!", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press any key continue on to the next level", self.window.width / 2,
                         self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        """ If the user presses a key start the game. """
        level_view = LevelTwoView()
        level_view.setup()
        self.window.show_view(level_view)


class LevelTwoCompleteView(arcade.View):
    """Create the level two completion screen."""
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.LIGHT_GRAY)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Level Two Complete!", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press any key continue on to the next level", self.window.width / 2,
                         self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        """ If the user presses a key start the game. """
        level_view = LevelThreeView()
        level_view.setup()
        self.window.show_view(level_view)


class LevelThreeCompleteView(arcade.View):
    """ Create the level three (and final) completion screen."""
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("You did it!", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press 'Q to quit or 'P' to play again", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key: int, modifiers: int):
        """ If the user presses a key start the game. """
        if key == arcade.key.P:
            level_view = LevelOneView()
            level_view.setup()
            self.window.show_view(level_view)
        elif key == arcade.key.Q:
            self.window.close()


class LevelOneView(arcade.View):
    """ Create level one."""

    def __init__(self):
        """ Create the variables """

        # Init the parent class.
        super().__init__()

        # Create the level complete variable to define when the music should end.
        self.level_complete = False

        # Create the player sprite variable.
        self.player_sprite = None

        # Create the variables for the SpriteLists.
        self.player_list = None
        self.static_walls_list = None
        self.moving_walls_list = None
        self.coin_list = None
        self.carrot_list = None

        # Create the tile map variable for the json files.
        self.tile_map = None

        # Create the score variable.
        self.score = 0

        # Create the physics engine variable.
        self.physics_engine = None

        # Create variables for the keyboard.
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Load the sounds.
        self.jump_sound = arcade.load_sound("jump_sound.wav")
        self.falling_sound = arcade.load_sound("falling_sound.wav")
        self.coin_sound = arcade.load_sound("coin_sound.wav")
        self.super_coin_sound = arcade.load_sound("super_coin_sound.wav")
        self.carrot_sound = arcade.load_sound("carrot_sound.wav")

        # Load music and create the music player.
        self.music = arcade.load_sound("Grasslands Theme.mp3")
        self.music_player = None

        # Create the cameras.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up everything with the game """

        # Create the SpriteLists.
        self.player_list = arcade.SpriteList()
        self.static_walls_list = arcade.SpriteList()
        self.moving_walls_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()

        # Create the user's player.
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

        # Open the tile map created in Tiled.
        self.tile_map = arcade.load_tilemap("final_lab_3.json", scaling=SPRITE_SCALING)

        # Set SpriteLists.
        self.static_walls_list = self.tile_map.sprite_lists["Static Walls"]
        self.moving_walls_list = self.tile_map.sprite_lists["Moving Walls"]
        self.coin_list = self.tile_map.sprite_lists["Coins"]
        self.carrot_list = self.tile_map.sprite_lists["Carrots"]

        # Set the background color.
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Create a list of wall lists to use for the physics engine.
        all_walls_list = [self.static_walls_list, self.moving_walls_list]

        # Keep player from running through the wall_list layer.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, all_walls_list,
                                                             gravity_constant=.5)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # Use the camera for the background and draw the background.
        self.background.use()

        # Draw a cloud.
        arcade.draw_circle_filled(600, 430, 40, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(580, 420, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(620, 420, 30, arcade.csscolor.WHITE)

        # Draw a cloud.
        arcade.draw_circle_filled(300, 215, 40, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(280, 205, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(320, 205, 30, arcade.csscolor.WHITE)

        # Draw a cloud.
        arcade.draw_circle_filled(200, 500, 40, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(180, 490, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(220, 490, 30, arcade.csscolor.WHITE)

        # Use the camera for the sprites.
        self.camera_sprites.use()

        # Draw the SpriteLists.
        self.player_list.draw()
        self.static_walls_list.draw()
        self.moving_walls_list.draw()
        self.coin_list.draw()
        self.carrot_list.draw()

        # Use the camera for the score.
        self.camera_gui.use()

        # Draw the score.
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 25)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        # Calculate speed based on the keys pressed.
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        # Calculate speed based on the keys pressed.
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the physics engine.
        self.physics_engine.update()

        # Create a list to check for collisions between the player and the coins.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Create a for loop that is called everytime the user collects a coin.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.level_complete = True
            if self.score < 10:
                arcade.play_sound(self.coin_sound)
            elif self.score >= 10:
                arcade.play_sound(self.super_coin_sound)
            view = LevelOneCompleteView()
            self.window.show_view(view)

        # Create if statements that determine whether or not music is playing.
        if not self.music_player or not self.music_player.playing and self.level_complete is False:
            self.music_player = arcade.play_sound(self.music)
        elif self.level_complete is True:
            arcade.stop_sound(self.music_player)

        # Create a list to check for collisions between the player and the carrots.
        carrot_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.carrot_list)
        for carrot in carrot_hit_list:
            arcade.play_sound(self.carrot_sound)
            carrot.remove_from_sprite_lists()
            self.score += 1

        # Create an if statement that determines when the player looses the game.
        if self.player_sprite.center_y > -1:
            self.player_list.update()
            self.scroll_to_player()
        else:
            view = GameOverView()
            self.window.show_view(view)
            arcade.stop_sound(self.music_player)
            arcade.play_sound(self.falling_sound)

    def scroll_to_player(self):
        """ Makes the screen scroll to the player."""
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


class LevelTwoView(arcade.View):
    """ Create level two."""
    def __init__(self):
        """ Create the variables """

        # Init the parent class.
        super().__init__()

        # Create the level complete variable to define when the music should end.
        self.level_complete = False

        # Create the player sprite variable.
        self.player_sprite = None

        # Create the sprite list variables.
        self.player_list = None
        self.static_walls_list = None
        self.moving_walls_list = None
        self.coin_list = None
        self.carrot_list = None

        # Create the tile map variable for the json files.
        self.tile_map = None

        # Create the score variable.
        self.score = 0

        # Create the physics engine variable.
        self.physics_engine = None

        # Create variables for the keyboard.
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Load the sounds.
        self.jump_sound = arcade.load_sound("jump_sound.wav")
        self.falling_sound = arcade.load_sound("falling_sound.wav")
        self.coin_sound = arcade.load_sound("coin_sound.wav")
        self.super_coin_sound = arcade.load_sound("super_coin_sound.wav")
        self.carrot_sound = arcade.load_sound("carrot_sound.wav")

        # Load music and create the music player.
        self.music = arcade.load_sound("Desert Theme.mp3")
        self.music_player = None

        # Create the cameras.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up everything with the game """

        # Create the SpriteLists.
        self.player_list = arcade.SpriteList()
        self.static_walls_list = arcade.SpriteList()
        self.moving_walls_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()

        # Create the user's player.
        self.player_sprite = Player()
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

        # Open the tile map created in Tiled.
        self.tile_map = arcade.load_tilemap("final_lab_lvl_2.json", scaling=SPRITE_SCALING)

        # Set SpriteLists.
        self.static_walls_list = self.tile_map.sprite_lists["Static Walls"]
        self.moving_walls_list = self.tile_map.sprite_lists["Moving Walls"]
        self.coin_list = self.tile_map.sprite_lists["Coins"]
        self.carrot_list = self.tile_map.sprite_lists["Carrots"]

        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Create a list of wall lists to use for the physics engine.
        all_walls_list = [self.static_walls_list, self.moving_walls_list]

        # Keep player from running through the wall_list layer.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, all_walls_list,
                                                             gravity_constant=.5)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # Use the camera for the background and draw the background.
        self.background.use()

        # Draw the sun.
        arcade.draw_ellipse_filled(600, 500, 100, 90, arcade.csscolor.LIGHT_YELLOW)

        # Use the camera for the sprites.
        self.camera_sprites.use()

        # Draw the SpriteLists.
        self.player_list.draw()
        self.static_walls_list.draw()
        self.moving_walls_list.draw()
        self.coin_list.draw()
        self.carrot_list.draw()

        # Use the camera for the score.
        self.camera_gui.use()

        # Draw the score.
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 25)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the physics engine.
        self.physics_engine.update()

        # Create a list to check for collisions between the player and the coins.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Create a for loop that is called everytime the user collects a coin.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.level_complete = True
            if self.score < 10:
                arcade.play_sound(self.coin_sound)
            elif self.score >= 10:
                arcade.play_sound(self.super_coin_sound)
            view = LevelTwoCompleteView()
            self.window.show_view(view)

        # Create if statements that determine whether or not music is playing.
        if not self.music_player or not self.music_player.playing and self.level_complete is False:
            self.music_player = arcade.play_sound(self.music)
        elif self.level_complete is True:
            arcade.stop_sound(self.music_player)

        # Create a list to check for collisions between the player and the carrots.
        carrot_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.carrot_list)
        for carrot in carrot_hit_list:
            arcade.play_sound(self.carrot_sound)
            carrot.remove_from_sprite_lists()
            self.score += 1

        # Create an if statement that determines when the player looses the game.
        if self.player_sprite.center_y > -1:
            self.player_list.update()
            self.scroll_to_player()
        else:
            view = GameOverView()
            self.window.show_view(view)
            arcade.stop_sound(self.music_player)
            arcade.play_sound(self.falling_sound)

    def scroll_to_player(self):
        """ Makes the screen scroll to the player."""
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


class LevelThreeView(arcade.View):
    """ Create level three."""

    def __init__(self):
        """ Create the variables """

        # Init the parent class.
        super().__init__()

        # Create the level complete variable to define when the music should end.
        self.level_complete = False

        # Create the player sprite variable.
        self.player_sprite = None

        # Create the sprite list variables.
        self.player_list = None
        self.static_walls_list = None
        self.moving_walls_list = None
        self.coin_list = None
        self.carrot_list = None

        # Create the tile map variable for the json files.
        self.tile_map = None

        # Create the score variable.
        self.score = 0

        # Create the physics engine variable.
        self.physics_engine = None

        # Create variables for the keyboard.
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Load the sounds.
        self.jump_sound = arcade.load_sound("jump_sound.wav")
        self.falling_sound = arcade.load_sound("falling_sound.wav")
        self.coin_sound = arcade.load_sound("coin_sound.wav")
        self.super_coin_sound = arcade.load_sound("super_coin_sound.wav")
        self.carrot_sound = arcade.load_sound("carrot_sound.wav")

        # Load music and create the music player.
        self.music = arcade.load_sound("Iceland Theme.mp3")
        self.music_player = None

        # Create the cameras.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up everything with the game """

        # Create the SpriteLists.
        self.player_list = arcade.SpriteList()
        self.static_walls_list = arcade.SpriteList()
        self.moving_walls_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()

        # Create the user's player.
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

        # Open the tile map created in Tiled.
        self.tile_map = arcade.load_tilemap("final_lab_lvl_3.json", scaling=SPRITE_SCALING)

        # Set SpriteLists.
        self.static_walls_list = self.tile_map.sprite_lists["Static Walls"]
        self.moving_walls_list = self.tile_map.sprite_lists["Moving Walls"]
        self.coin_list = self.tile_map.sprite_lists["Coins"]
        self.carrot_list = self.tile_map.sprite_lists["Carrots"]

        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Create a list of wall lists to use for the physics engine.
        all_walls_list = [self.static_walls_list, self.moving_walls_list]

        # Keep player from running through the wall_list layer.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, all_walls_list,
                                                             gravity_constant=.5)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # Use the camera for the background and draw the background.
        self.background.use()

        # Draw the mountain.
        arcade.draw_triangle_filled(0, 0, 800, 0, 400, 600, arcade.csscolor.GREY)
        arcade.draw_triangle_filled(330, 500, 470, 500, 400, 600, arcade.csscolor.WHITE)

        # Use the camera for the sprites.
        self.camera_sprites.use()

        # Draw the SpriteLists.
        self.player_list.draw()
        self.static_walls_list.draw()
        self.moving_walls_list.draw()
        self.coin_list.draw()
        self.carrot_list.draw()

        # Use the camera the for score.
        self.camera_gui.use()

        # Draw the score.
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 25)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        # Calculate speed based on the keys pressed.
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        # Calculate speed based on the keys pressed.
        self.player_sprite.change_x = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the physics engine.
        self.physics_engine.update()

        # Create a list to check for collisions between the player and the coins.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Create a for loop that is called everytime the user collects a coin.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.level_complete = True
            if self.score < 10:
                arcade.play_sound(self.coin_sound)
            elif self.score >= 10:
                arcade.play_sound(self.super_coin_sound)
            view = LevelThreeCompleteView()
            self.window.show_view(view)

        # Create if statements that determine whether or not music is playing.
        if not self.music_player or not self.music_player.playing and self.level_complete is False:
            self.music_player = arcade.play_sound(self.music)
        elif self.level_complete is True:
            arcade.stop_sound(self.music_player)

        # Create a list to check for collisions between the player and the carrots.
        carrot_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.carrot_list)
        for carrot in carrot_hit_list:
            arcade.play_sound(self.carrot_sound)
            carrot.remove_from_sprite_lists()
            self.score += 1

        # Create an if statement that determines when the player looses the game.
        if self.player_sprite.center_y > -1:
            self.player_list.update()
            self.scroll_to_player()
        else:
            view = GameOverView()
            self.window.show_view(view)
            arcade.stop_sound(self.music_player)
            arcade.play_sound(self.falling_sound)

    def scroll_to_player(self):
        """ Makes the screen scroll to the player."""
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
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
