from tkinter import *
import random
import constants as c

root = Tk()
root.title('Snake Game')
root.resizable(False, False)


class Main(Canvas):
    def __init__(self):
        super().__init__(width=c.WIDTH, height=c.HEIGHT, highlightthickness=0, bg=c.BG_COLOR)
        self.bg = PhotoImage(file='grass.png')
        self.coordinate = []
        self.x = c.START_X
        self.y = c.START_Y
        self.dir = c.move_way
        self.start_dir = self.dir['down']
        self.score = 0
        self.create_image(0, 0, image=self.bg, anchor="nw")
        self.create_food()
        self.scoreboard()
        self.snake_part(self.x, self.y)
        self.pack()

    def scoreboard(self):
        self.label = Label(root, text=f"Score:{self.score}", font=('calibri', 20))
        self.label.pack(side=TOP, anchor="nw")

    def update_score(self):
        self.score = self.score+1
        self.label['text'] = "Score:{}".format(self.score)

    def create_food(self):
        x = random.randint(0, 22) * c.PART_SIZE
        y = random.randint(0, 22) * c.PART_SIZE
        self.coordinate = [x, y]
        self.create_oval(x, y, (x + c.PART_SIZE), (y + c.PART_SIZE), fill=c.FOOD_COLOR, tags='food')

    def snake_part(self, x, y):
        self.part = self.create_rectangle(x, y, x + c.PART_SIZE, y + c.PART_SIZE, fill=c.SNAKE_COLOR)


win = Main()
root.mainloop()
