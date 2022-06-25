from tkinter import *
import random
import constants as c

root = Tk()
root.title('Snake Game')
root.resizable(False, False)
score = 0
direction = 'down'
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


def move_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= c.PART_SIZE
    elif direction == "down":
        y += c.PART_SIZE
    elif direction == "left":
        x -= c.PART_SIZE
    elif direction == "right":
        x += c.PART_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + c.PART_SIZE, y + c.PART_SIZE, fill=c.SNAKE_COLOR)
    snake.squares.insert(0, square)
    if check(snake):
        game_over()
    else:
        root.after(c.SPEED, move_turn, snake, food)


def check(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= c.WIDTH:
        return True
    elif y < 0 or y >= c.HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False



def change_dir(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction


def game_over():
    canvas.delete(ALL)
    canvas.create_text(c.WIDTH / 2, c.HEIGHT / 2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")


root.bind('<Left>', lambda event: change_dir('left'))
root.bind('<Right>', lambda event: change_dir('right'))
root.bind('<Up>', lambda event: change_dir('up'))
root.bind('<Down>', lambda event: change_dir('down'))

snake = Snake()
food = Food()
move_turn(snake, food)
root.mainloop()
