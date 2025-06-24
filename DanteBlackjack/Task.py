from Tool import *

class Task(Tool):
    def __init__(self, x, y, task_png):
        super().__init__(x, y, task_png)
    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False
task_number = 1
x_task = 223
y_task = 140
x_task, y_task = scale_position(x_task,y_task,choice)
task_1 = Task(x_task, y_task, "zad11.png")
task_2 = Task(x_task, y_task, "zad12.png")
task_3 = Task(x_task, y_task, "zad13.png")
task_4 = Task(x_task, y_task, "zad14.png")
task_5 = Task(x_task, y_task, "zad15.png")
