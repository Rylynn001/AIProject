import tkinter as tk
import random

# 游戏配置
WIDTH = 400
HEIGHT = 400
SIZE = 20
SPEED = 150   # 刷新速度，越小越快

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇游戏 - Python Tkinter")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # 初始化蛇
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"

        # 绑定键盘
        root.bind("<KeyPress>", self.change_direction)

        # 食物
        self.food = self.spawn_food()

        # 开始游戏
        self.running = True
        self.update()

    def spawn_food(self):
        x = random.randrange(0, WIDTH, SIZE)
        y = random.randrange(0, HEIGHT, SIZE)
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        # 不允许直接反方向
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE
        elif self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE

        new_head = (head_x, head_y)

        # 撞墙
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.running = False
            return

        # 撞自己
        if new_head in self.snake:
            self.running = False
            return

        # 添加新头
        self.snake.insert(0, new_head)

        # 吃食物
        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        # 画蛇
        for (x, y) in self.snake:
            self.canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill="green")

        # 画食物
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+SIZE, fy+SIZE, fill="red")

    def update(self):
        if self.running:
            self.move()
            self.draw()
            self.root.after(SPEED, self.update)
        else:
            self.game_over()

    def game_over(self):
        self.canvas.create_text(WIDTH/2, HEIGHT/2, fill="white",
                                text="GAME OVER",
                                font=("Arial", 24))
        self.canvas.create_text(WIDTH/2, HEIGHT/2+40, fill="white",
                                text="按 ESC 退出",
                                font=("Arial", 14))
        self.root.bind("<Escape>", lambda e: self.root.destroy())


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
