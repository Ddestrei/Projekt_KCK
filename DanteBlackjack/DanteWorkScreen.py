from Screen import *
from Task import Task
from Task import torch_table
class DanteWorkScreen(Screen):
    def Start(self, window, choice):
        task_background = pygame.image.load(task_background_path)
        task_background = pygame.transform.scale(task_background, (resolutions[choice]))
        window.blit(task_background, (0, 0))
        house_button.tool_draw(window)
        wiwd.tool_draw(window)
        pp1.tool_draw(window)
        help.tool_draw(window)
        tip_1.hide()
        tip_2.hide()
        tip_3.hide()
        tip_4.hide()
        tip_5.hide()
        task_1.hide()
        task_2.hide()
        task_3.hide()
        task_4.hide()
        task_5.hide()
        torch.hide()
        if torch_table[Task.task_number-1] == 1 or Task.work_mode == 0:
            unlock_button.hide()
        else:
            unlock_button.show()
        if Task.task_number == 1:
            task_1.show()
            if Task.work_mode == 1:
                if torch_table[0] == 1:
                    tip_1.show()
                else:
                    tip_1.hide()
                    torch.show()
        elif Task.task_number == 2:
                task_2.show()
                if Task.work_mode == 1:
                    if torch_table[1] == 1:
                        tip_2.show()
                    else:
                        tip_2.hide()
                        torch.show()
        elif Task.task_number == 3:
                task_3.show()
                if Task.work_mode == 1:
                    if torch_table[2] == 1:
                        tip_3.show()
                    else:
                        tip_3.hide()
                        torch.show()
        elif Task.task_number == 4:
                task_4.show()
                if Task.work_mode == 1:
                    if torch_table[3] == 1:
                        tip_4.show()
                    else:
                        tip_4.hide()
                        torch.show()
        elif Task.task_number == 5:
            task_5.show()
            if Task.work_mode == 1:
                if torch_table[4] == 1:
                    tip_5.show()
                else:
                    tip_5.hide()
                    torch.show()



        task_1.tool_draw(window)
        task_2.tool_draw(window)
        task_3.tool_draw(window)
        task_4.tool_draw(window)
        task_5.tool_draw(window)
        tip_1.tool_draw(window)
        tip_2.tool_draw(window)
        tip_3.tool_draw(window)
        tip_4.tool_draw(window)
        tip_5.tool_draw(window)
        tip_5.tool_draw(window)
        torch.tool_draw(window)
        unlock_button.tool_draw(window)
        mode_0_button.tool_draw(window)
        pygame.display.update()