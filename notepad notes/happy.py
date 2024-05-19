def happy():

	import turtle
	import pygame

# Initialize Pygame
	pygame.init()

# Set up the screen
	screen = turtle.Screen()
	screen.title("Doraemon Drawing and Song")
	screen.bgcolor("white")

# Set up the turtle
	t = turtle.Turtle()
	t.speed(3)

# Draw head
	t.penup()
	t.goto(0, -100)
	t.pendown()
	t.circle(100)

# Draw body
	t.penup()
	t.goto(0, -200)
	t.pendown()
	t.circle(150)

# Draw eyes
	t.penup()
	t.goto(-40, 30)
	t.pendown()
	t.begin_fill()
	t.circle(15)
	t.end_fill()

	t.penup()
	t.goto(40, 30)
	t.pendown()
	t.begin_fill()
	t.circle(15)
	t.end_fill()

# Draw mouth
	t.penup()
	t.goto(-40, -10)
	t.pendown()
	t.setheading(-60)
	t.circle(40, 120)

# Draw Doraemon's song
	t.penup()
	t.goto(-70, 130)
	t.pendown()
	t.write("Heloooo Cuties", font=("Arial", 16, "bold"))

# Hide the turtle
	t.hideturtle()

# Play the Doraemon song
	pygame.mixer.music.load("Happy Happy - Cat Meme Song.mp3")
	pygame.mixer.music.play()

# Exit on screen click
	screen.exitonclick()

# Quit Pygame
	pygame.quit()