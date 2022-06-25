from tkinter import *
import random
import constants as c

root = Tk()
root.title('Snake Game')
root.resizable(False, False)
score = 0
label = Label(root, text="Score:{}".format(score), font=('caliblri', 20))
label.pack(side=TOP, anchor=NW)

canvas = Canvas(root, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
bg = PhotoImage(file='grass.png')
canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.pack()

class Snake:

    def __init__(self):
        self.body_size = c.START_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, c.START_SIZE):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + c.PART_SIZE, y + c.PART_SIZE, fill=c.SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):
        x = random.randint(0, (int(c.WIDTH / c.PART_SIZE)) - 1) * c.PART_SIZE
        y = random.randint(0, (int(c.HEIGHT / c.PART_SIZE)) - 1) * c.PART_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + c.PART_SIZE, y + c.PART_SIZE, fill=c.FOOD_COLOR, tag="food")


snake = Snake()
food = Food()

root.mainloop()
