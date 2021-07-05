from turtle import *

shape()
speed(0)
def fractal_side(length, levels):
	if levels == 0:
		forward(length)
		return

	length /= 3.0
	fractal_side(length, levels - 1)
	left(60)
	fractal_side(length, levels - 1)
	right(120)
	fractal_side(length, levels - 1)
	left(60)
	fractal_side(length, levels - 1)


def snowflake(sides, length):
	for i in range(sides):
		color("blue")
		fractal_side(length, sides)
		right(360 / sides)
	
snowflake(4, 200)

mainloop()