"""EXERCISE: make overlapping polygon art like the reference image.
Complete polygon_shape.py first. Then adjust the parameters below to
create your own composition. The example uses a black background.
"""
import turtle
import random
from polygon_shape import Polygon

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Static Polygon Artwork")
    screen.tracer(0)  # Disable immediate animation drawing for fast rendering

    colors = ["cyan", "orange", "magenta", "yellow", "lime", "deepskyblue", "crimson", "white"]
    polygons = []

    for _ in range(20):
        x = random.randint(-250, 250)
        y = random.randint(-180, 180)
        sides = random.randint(3, 7)
        length = random.randint(30, 90)
        color = random.choice(colors)
        pen_size = random.randint(1, 6)
        angle = random.randint(0, 360)

        poly = Polygon(x, y, sides, length, color, pen_size, angle)
        poly.draw()
        polygons.append(poly)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()