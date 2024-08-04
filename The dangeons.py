#модули
import world
import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.widget import WidgetHandler as wh
pygame.init()

#настройка экрана и шрифта
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode([W, H])
description = "The dangeons"
pygame.display.set_caption(description)
font = pygame.font.SysFont(None, 300)
timer = pygame.time.Clock()
font2 = pygame.font.SysFont(None, 50)

#настройка цветов и текста
white = (255, 255, 255)
grey = (128, 128, 128)
keep_going = True
game_name = "The dangeons"
menu = "main menu"

#настройка текстур для меню
blocks = pygame.image.load("images/blocks.png")
stone = pygame.Surface((10, 10))#текстура камня
stone.blit(blocks, (0, 0))
stone = pygame.transform.scale(stone, (20, 20))
floor = pygame.Surface((10, 10))#текстура пола
floor.blit(blocks, (-10, 0))
floor = pygame.transform.scale(floor, (20, 20))
game_world = world.World()

def playfunc():#запуск игры
    global menu
    global game_world
    game_world = world.World()
    menu = "game"
    wh.removeWidget(play)

play = Button(#создание кнопки "play"
    screen,
    850,
    425,
    100,
    50,
    text='Play',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=grey,  # Colour of button when not being interacted with
    hoverColour=(100, 100, 100),  # Colour of button when being hovered over
    pressedColour=(150, 150, 150),  # Colour of button when being clicked
    onClick=playfunc
)

while keep_going:#основной цикл
    events = pygame.event.get()
    for event in events:#проверка нажатий кнопок
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keep_going = False
    screen.fill(white)
    if menu == "main menu":#отрисовка меню
        for x in range(int(W / 20)):
            for y in range(int(H / 20)):
                screen.blit(floor, (x * 20, y * 20))
        text = font.render(game_name, True, grey)#отрисовка текста
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 20
        screen.blit(text, text_rect)
    elif menu == "game":#игра
        game_world.update(screen, events)
    pygame_widgets.update(events)
    string = str(int(timer.get_fps()))
    screen.blit(font2.render(string, True, (255, 0, 0)), (0, 0))
    pygame.display.update()
    timer.tick(60)
pygame.quit()
