import sys
import pygame
import pygame._sdl2
from pygame._sdl2.controller import Controller


pygame.init()
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Testing controllers")

font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

pygame._sdl2.controller.init()

def debug(info, y=10, x=20):
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), False, 'white', 'black')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    display_surf.blit(debug_surf, debug_rect)

def reset_joysticks():
    return [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


joysticks = reset_joysticks()

debug_messages = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type in [pygame.JOYDEVICEADDED, pygame.JOYDEVICEREMOVED]:
            joysticks = reset_joysticks()

    window.fill('white')

    for joystick in joysticks:
        controller = Controller.from_joystick(joystick)
        js = [joystick.get_guid(), joystick.get_name()]
        for button in range(joystick.get_numbuttons()):
            btn_message = f'Button {str(button)}: {str(controller.get_button(button))}'
            js.append(btn_message)
        for axis in range(joystick.get_numaxes()):
            axis_message = f'Axis {str(axis)}: {str(controller.get_axis(axis))}'
            js.append(axis_message)
        for hat in range(joystick.get_numhats()):
            hat_message = f'Hat {str(hat)}: {str(joystick.get_hat(hat))}'
            js.append(hat_message)

        debug_messages.append(js)

    for js, dbg_messages in enumerate(debug_messages):
        for i, message in enumerate(dbg_messages):
            l = 20 if js == 0 else js * 420
            debug(message, i * 18, l)

    pygame.display.flip()
    clock.tick(60)
    debug_messages.clear()
