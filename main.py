from tkinter import *
import random
import constants as c

root = Tk()
root.title('Snake Game')
root.resizable(False, False)

score = 0
label =Label(root, text="Score:{}".format(score), font=('caliblri', 20))
label.pack(side=TOP, anchor=NW)

canvas = Canvas(root, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
canvas.pack()

root.mainloop()