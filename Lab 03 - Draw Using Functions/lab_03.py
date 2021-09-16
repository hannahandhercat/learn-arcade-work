import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_light_hills(x, y):
    arcade.draw_arc_filled(300 + x - 300, 0 + y, 700, 600, (167, 207, 197), 0, 180)


def draw_dark_hills(x, y):
    arcade.draw_arc_filled(300 + x - 300, 0 + y, 700, 600, (140, 173, 165), 0, 180)


def draw_darker_hills(x, y):
    arcade.draw_arc_filled(300 + x - 300, 0 + y, 700, 600, (129, 156, 149), 0, 180)


def draw_flower(x, y):
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


def cloud(x, y):


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 03")
    arcade.set_background_color(arcade.csscolor.WHITE_SMOKE)
    arcade.start_render()

    draw_darker_hills(500, 150)
    draw_dark_hills(100, 100)
    draw_light_hills(300, 0)

    draw_flower(35, 75)
    draw_flower(110, 75)
    draw_flower(185, 75)
    draw_flower(260, 75)
    draw_flower(335, 75)
    draw_flower(410, 75)
    draw_flower(485, 75)
    draw_flower(560, 75)

    # Finish render and keep window open until closed.
    arcade.finish_render()
    arcade.run()


main()