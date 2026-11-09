"""EXERCISE: animate multiple polygons by moving existing objects.
First finish polygon_shape.py. Then change the motion, colors, sizes,
number of polygons, and frame count to create your own artwork.
"""
import turtle
import time
import math
from polygon_shape import Polygon

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Animated Polygon Artwork")
    screen.tracer(0)

    polygons = [
        Polygon(-150, 50, 3, 60, "cyan", 3, 0),
        Polygon(-100, -80, 4, 70, "orange", 4, 15),
        Polygon(0, 100, 5, 50, "magenta", 2, 30),
        Polygon(120, 60, 6, 45, "lime", 5, 45),
        Polygon(150, -100, 7, 40, "yellow", 3, 60),
        Polygon(-50, -150, 3, 65, "deepskyblue", 4, 10),
        Polygon(50, -50, 4, 55, "crimson", 2, 20),
        Polygon(0, 0, 5, 50, "white", 3, 0),
    ]

    for p in polygons:
        p.draw()
    screen.update()

    for frame in range(70):
        for i, p in enumerate(polygons):
            new_x = p._x + math.sin(frame * 0.1 + i) * 4
            new_y = p._y + math.cos(frame * 0.1 + i) * 3
            p.move_to(new_x, new_y)
        screen.update() 
        time.sleep(0.05)    
    screen.mainloop()

if __name__ == "__main__":
    main()