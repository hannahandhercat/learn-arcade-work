import arcade
# Open a window.
arcade.open_window(600, 600, "Lab 02")

# Set background color and begin render.
arcade.set_background_color(arcade.csscolor.WHITE_SMOKE)
arcade.start_render()

# Hills in the background and foreground.
arcade.draw_arc_filled(450, 0, 500, 700, (167, 207, 197), 0, 180)
arcade.draw_arc_filled(150, 0, 400, 600, (140, 173, 165), 0, 180)
arcade.draw_arc_filled(300, 0, 600, 200, (140, 77, 90), 0, 180)

# Lamp Post
arcade.draw_rectangle_filled(300, 300, 10, 400, (54, 48, 48))
arcade.draw_arc_filled(300, 480, 50, 100, (54, 48, 48), 0, 180)
arcade.draw_arc_filled(300, 485, 40, 80, (231, 235, 117), 0, 180)
arcade.draw_rectangle_outline(300, 502, 50, 50, (54, 48, 48), 5, 0)
arcade.draw_arc_filled(300, 530, 10, 10, (54, 48, 48), 0, 180)
arcade.draw_rectangle_filled(300, 500, 5, 50, (54, 48, 48))
arcade.draw_ellipse_filled(300, 50, 450, 100, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_outline(300, 500, 100, (231, 235, 117), 3)

# Bird
arcade.draw_ellipse_filled(280, 545, 10, 35, (32, 44, 69))
arcade.draw_triangle_filled(260, 550, 278, 555, 278, 560, (181, 163, 105))

# Finish render and keep window open until closed.
arcade.finish_render()
arcade.run()
