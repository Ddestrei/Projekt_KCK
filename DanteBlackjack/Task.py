from Tool import *

class Task(Tool):
    def __init__(self, x, y, task_png):
        super().__init__(x, y, task_png)
    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False


task_number = 1
work_mode = 0
torch_table = [0, 0, 0, 0, 0]

x_task = 223
y_task = 140
x_task, y_task = scale_position(x_task,y_task,choice)
task_1 = Task(x_task, y_task, task_1_path)
task_2 = Task(x_task, y_task, task_2_path)
task_3 = Task(x_task, y_task, task_3_path)
task_4 = Task(x_task, y_task, task_4_path)
task_5 = Task(x_task, y_task, task_5_path)


x_task = 223
y_task = 386
x_task, y_task = scale_position(x_task,y_task,choice)
tip_1 = Task(x_task, y_task, tip_1_path)
tip_2 = Task(x_task, y_task, tip_2_path)
tip_3 = Task(x_task, y_task, tip_3_path)
tip_4 = Task(x_task, y_task, tip_4_path)
tip_5 = Task(x_task, y_task, tip_5_path)

x_task = 0
y_task = 0
x_task, y_task = scale_position(x_task,y_task,choice)
torch = Task(x_task, y_task, torch_path)

x_task = 672
y_task = 771
x_task, y_task = scale_position(x_task,y_task,choice)
unlock_button = Task(x_task, y_task, unlock_path)