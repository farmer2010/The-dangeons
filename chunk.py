import generator
import random
import blocks
import pygame
pygame.init()

font = pygame.font.SysFont(None, 50)

texture = pygame.image.load("images/blocks.png")
floor = pygame.Surface((10, 10))
floor.blit(texture, (-10, 0))
floor = pygame.transform.scale(floor, (20, 20))

def get_light(blocks):
    movelist = [
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
    ]
    light = [[255 for y in range(16)]for x in range(16)]
    for x in range(16):
        for y in range(16):
            for i in range(8):
                pos = [x + movelist[i][0], y + movelist[i][1]]
                if pos[0] >= 0 and pos[0] <= 15 and pos[1] >= 0 and pos[1] <= 15:
                    if blocks[pos[0]][pos[1]].name == "air" or blocks[x][y].name == "air":
                        light[x][y] = 0
                else:
                    if blocks[x][y].name == "air":
                        light[x][y] = 0
    return(light)

class Chunk():
    def __init__(self, pos, game_world, seed=0):
        self.W = pygame.display.Info().current_w
        self.H = pygame.display.Info().current_h
        self.world = game_world
        self.seed = seed
        generator_result = generator.generate(pos[0], pos[1], self.seed, self.world)
        self.blocks = generator_result[0]
        self.floor = generator_result[1]
        self.lightmap = []
        self.image = pygame.Surface((320, 320))
        self.pos = pos
        self.generate = 1
        self.change_image()

    def draw(self, screen, scroll):#отрисовка
        screen.blit(self.image, (self.pos[0] * 320 + scroll[0] + int(self.W / 2), self.pos[1] * 320 + scroll[1] + int(self.H / 2)))

    def change_image(self):#сменить тексуру
        string = str(self.pos[0]) + "_" + str(self.pos[1])
        self.image.fill((255, 255, 255))
        for x in range(16):
            for y in range(16):
                self.floor[x][y].draw(self.image)#отрисовка пола
                self.blocks[x][y].draw(self.image)#отрисовка блоков
        self.image.blit(font.render(string, True, (0, 0, 0)), (0, 0))
        #self.lightmap = get_light(self.blocks)
        #for x in range(16):
        #    for y in range(16):
        #        square = pygame.Surface((20, 20))
        #        square.convert_alpha()
        #        square.set_alpha(self.lightmap[x][y])
        #        self.image.blit(square, (x * 20, y * 20))
