from tkinter import *
import random
import constants as c

score = 0
direction = 'Dowm'

master = Tk()
master.title("SNAKE GAME")
master.resizable(False, False)

label = Label(master, text='Score: {}'.format(score), font=('calibri', 20))
label.pack(side=TOP, anchor=NW)

canvas = Canvas(master, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
canvas.pack()












mainloop()

