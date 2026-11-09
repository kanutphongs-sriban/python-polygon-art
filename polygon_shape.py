"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle

class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Validate state values and initialize private internal Turtle object."""
        if sides < 3:
            raise ValueError("Polygon must have at least 3 sides.")
        if side_length <= 0:
            raise ValueError("Side length must be positive.")
        if pen_size <= 0:
            raise ValueError("Pen size must be positive.")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle

        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)

    def draw(self):
        """Draw regular polygon using starting vertex (x, y) and initial angle."""
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)
        self._pen.pencolor(self._color)
        self._pen.pensize(self._pen_size)
        self._pen.pendown()

        turn_angle = 360 / self._sides
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(turn_angle)

        self._pen.penup()

    def move_to(self, x, y):
        """Erase current polygon strokes, update coordinates, and redraw."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()