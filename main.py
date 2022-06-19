from tkinter import *
import random
import constants as c

root = Tk()
root.title('Snake Game')
root.resizable(False, False)

class Window(Canvas):
    def __init__(self):
        super().__init__(width=c.WIDTH, height=c.HEIGHT, highlightthickness=0, bg=c.BG_COLOR)
        self.bg = PhotoImage(file='grass.png')
        self.create_image(0, 0, image=self.bg, anchor="nw")
        self.pack()
        self.score = 0
        self.label = Label(root, text=f"Score:{self.score}", font=('calibri', 20))
        self.label.pack(side=TOP, anchor="nw")
        self.create_food()

    def create_food(self):
        x = random.randint(0, 22) * c.PART_SIZE
        y = random.randint(0, 22) * c.PART_SIZE
        self.coordinate = [x, y]
        self.create_oval(x, y, (x + c.PART_SIZE), (y + c.PART_SIZE), fill=c.FOOD_COLOR)


win = Window()
root.mainloop()
