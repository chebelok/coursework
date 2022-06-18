from tkinter import *
import random
import constants as c

class Food:
    def __init__(self):
        x = random.randint(0, 22) * c.PART_SIZE
        y = random.randint(0, 22) * c.PART_SIZE
        self.coordinate = [x, y]
        canvas.create_oval(x, y, (x + c.PART_SIZE), (y + c.PART_SIZE), fill=c.FOOD_COLOR)

root = Tk()
root.title('Snake Game')
root.resizable(False, False)

score = 0
label =Label(root, text="Score:{}".format(score), font=('caliblri', 20))
label.pack(side=TOP, anchor=NW)

canvas = Canvas(root, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
canvas.pack()

food = Food()
root.mainloop()