from Screen import *

class DanteTaskScreen(Screen):
    def Start(self, window, choice):
        dante_task_background = pygame.image.load(dante_task_background_path)
        dante_task_background = pygame.transform.scale(dante_task_background, (resolutions[choice]))
        window.blit(dante_task_background, (0, 0))
        house_button.tool_draw(window)
        do_1.tool_draw(window)
        do_2.tool_draw(window)
        do_3.tool_draw(window)
        do_4.tool_draw(window)
        do_5.tool_draw(window)
        wiwd.tool_draw(window)
        pp1.tool_draw(window)
        pygame.display.update()
