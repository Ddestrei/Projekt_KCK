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
task_1 = Task(x_task, y_task, task_1_path)
task_2 = Task(x_task, y_task, task_2_path)
task_3 = Task(x_task, y_task, task_3_path)
task_4 = Task(x_task, y_task, task_4_path)
task_5 = Task(x_task, y_task, task_5_path)
