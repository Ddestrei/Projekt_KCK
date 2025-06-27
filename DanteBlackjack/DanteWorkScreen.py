from Screen import *
import Task
class DanteWorkScreen(Screen):
    def Start(self, window, choice):
        task_background = pygame.image.load(task_background_path)
        task_background = pygame.transform.scale(task_background, (resolutions[choice]))
        window.blit(task_background, (0, 0))
        house_button.tool_draw(window)
        if Task.task_number == 0:
            task_1.hide()
            task_2.hide()
            task_3.hide()
            task_4.hide()
            task_5.hide()
        elif Task.task_number == 1:
            task_1.show()
            task_2.hide()
            task_3.hide()
            task_4.hide()
            task_5.hide()
        elif Task.task_number == 2:
            task_1.hide()
            task_2.show()
            task_3.hide()
            task_4.hide()
            task_5.hide()
        elif Task.task_number == 3:
            task_1.hide()
            task_2.hide()
            task_3.show()
            task_4.hide()
            task_5.hide()
        elif Task.task_number == 4:
            task_1.hide()
            task_2.hide()
            task_3.hide()
            task_4.show()
            task_5.hide()
        elif Task.task_number == 5:
            task_1.hide()
            task_2.hide()
            task_3.hide()
            task_4.hide()
            task_5.show()
        task_1.tool_draw(window)
        task_2.tool_draw(window)
        task_3.tool_draw(window)
        task_4.tool_draw(window)
        task_5.tool_draw(window)
        pygame.display.update()