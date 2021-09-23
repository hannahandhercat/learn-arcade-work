import arcade

# Set the width and height of the drawing window.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_light_hills(x, y):
    """Draw lightly colored hills."""
    arcade.draw_arc_filled(x, y, 700, 600, (167, 207, 197), 0, 180)


def draw_dark_hills(x, y):
    """Draw darkly colored hills."""
    arcade.draw_arc_filled(x, y, 700, 600, (140, 173, 165), 0, 180)


def draw_darker_hills(x, y):
    """Draw darkest colored hills."""
    arcade.draw_arc_filled(x, y, 700, 600, (129, 156, 149), 0, 180)


def draw_flower(x, y):
    """Draw a flower."""
    arcade.draw_rectangle_filled(x, y - 40, 10, 50, (100, 158, 120))
    arcade.draw_ellipse_filled(x, y + 22, 15, 30, (140, 77, 90))
    arcade.draw_ellipse_filled(x + 22, y - 2, 15, 30, (140, 77, 90), 90, 90)
    arcade.draw_ellipse_filled(x, y - 22, 15, 30, (140, 77, 90))
    arcade.draw_ellipse_filled(x - 22, y - 2, 15, 30, (140, 77, 90), 90, 90)
    arcade.draw_ellipse_filled(x + 15, y + 17, 15, 30, (140, 77, 90), 30, 30)
    arcade.draw_ellipse_filled(x - 15, y + 17, 15, 30, (140, 77, 90), 150, 150)
    arcade.draw_ellipse_filled(x - 15, y - 17, 15, 30, (140, 77, 90), 60, 60)
    arcade.draw_ellipse_filled(x + 15, y - 17, 15, 30, (140, 77, 90), 120, 120)
    arcade.draw_circle_filled(x, y, 8, arcade.csscolor.YELLOW, num_segments=32)


<<<<<<< HEAD
=======
def draw_cloud(x, y):
    """Draw a cloud."""
    arcade.draw_circle_outline(x, y, 23, arcade.csscolor.WHITE, 3)
    arcade.draw_ellipse_filled(x + 10, y - 20, 80, 40, arcade.csscolor.GREY)
    arcade.draw_ellipse_outline(x + 10, y - 20, 80, 40, arcade.csscolor.WHITE, 3)
    arcade.draw_circle_filled(x, y, 20, arcade.csscolor.GREY)


def draw_windmill(x, y):
    """Draw a windmill."""
    arcade.draw_rectangle_filled(x, y, 10, 80, (182, 193, 194))
    arcade.draw_circle_filled(x, y + 40, 7, (182, 193, 194))
    arcade.draw_rectangle_filled(x + 15, y + 30, 7, 40, (182, 193, 194), 120)
    arcade.draw_rectangle_filled(x - 15, y + 30, 7, 40, (182, 193, 194), 60)
    arcade.draw_rectangle_filled(x, y + 55, 7, 40, (182, 193, 194))


def draw_big_tree(x, y):
    """Draw a relatively big tree."""
    arcade.draw_rectangle_filled(x, y, 10, 50, (110, 95, 65))
    arcade.draw_triangle_filled(x + 30, y - 10, x, y + 40, x - 30, y - 10, (100, 158, 120))


def draw_little_tree(x, y):
    """Draw a relatively little tree."""
    arcade.draw_rectangle_filled(x, y, 5, 25, (110, 95, 65))
    arcade.draw_triangle_filled(x + 15, y - 5, x, y + 20, x - 15, y - 5, (100, 158, 120))


>>>>>>> 485f68ef629594d997dbf99d509dc5083c3c7363
def main():
    """Draw main function."""
    # Open window, set background color, begin render.
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 03")
    arcade.set_background_color(arcade.csscolor.WHITE_SMOKE)
    arcade.start_render()

    # Draw a landscape of multicolored hills.
    draw_darker_hills(500, 150)
    draw_dark_hills(100, 100)
    draw_light_hills(300, 0)

    # Draw a line of flowers.
    draw_flower(35, 75)
    draw_flower(110, 75)
    draw_flower(185, 75)
    draw_flower(260, 75)
    draw_flower(335, 75)
    draw_flower(410, 75)
    draw_flower(485, 75)
    draw_flower(560, 75)

    # Draw a small line of windmills in the background.
    draw_windmill(565, 420)
    draw_windmill(482.5, 420)
    draw_windmill(400, 420)

    # Draw a couple of relatively big trees in the foreground.
    draw_big_tree(300, 300)
    draw_big_tree(200, 280)

    # Draw many relatively small trees in the background.
    draw_little_tree(200, 350)
    draw_little_tree(150, 400)
    draw_little_tree(275, 350)
    draw_little_tree(100, 325)
    draw_little_tree(135, 350)
    draw_little_tree(100, 400)
    draw_little_tree(50, 375)

    # Draw a few clouds in the sky.
    draw_cloud(300, 500)
    draw_cloud(500, 550)
    draw_cloud(200, 400)
    draw_cloud(50, 570)

    # Finish render and keep window open until closed.
    arcade.finish_render()
    arcade.run()


<<<<<<< HEAD
main()
=======
# Run main function
main()
>>>>>>> 485f68ef629594d997dbf99d509dc5083c3c7363
