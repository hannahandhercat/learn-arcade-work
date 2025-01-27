import arcade

WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                else:
                    color = arcade.color.GREEN
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        cell_count = 0
        for row in range(ROW_COUNT):
            row_cell_count = 0
            continuous_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    cell_count += 1
                    row_cell_count += 1
                    continuous_count += 1
                else:
                    if continuous_count >= 2:
                        print(f"There are {continuous_count} continuous in selected row {row}")
                    continuous_count = 0
            print(f"Row {row} has {row_cell_count} selected")

            if continuous_count >= 2:
                print(f"There are {continuous_count} continuous in selected row {row}")
        print(f"Total of {cell_count} cells are selected")

        for column in range(COLUMN_COUNT):
            column_cell_count = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    column_cell_count += 1
            print(f"Column {column} has {column_cell_count} selected")


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()