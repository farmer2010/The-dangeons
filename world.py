import random
import player
import blocks
import math
import chunk
import pygame
pygame.init()

font = pygame.font.SysFont(None, 30)
white = (255, 255, 255)

def int_or_round(x):
    if x > 0:
        return(int(x) + 1)
    return(int(x))

class World():
    def __init__(self):
        self.W = pygame.display.Info().current_w
        self.H = pygame.display.Info().current_h
        self.seed = random.randint(-99999999, 99999999)
        self.chunks = {}
        self.load_chunks = {}
        self.load_distance = 4
        self.scroll = [-160, -160]
        self.display_scale = (-320, -320, self.W, self.H)
        self.center_chunk = [0, 0]
        self.last_center_chunk = [0, 0]
        for x in range(self.load_distance * 2 + 1):
            for y in range(self.load_distance * 2 + 1):
                self.chunks[f"{x - 3}_{y - 3}"] = chunk.Chunk((x - 3, y - 3), self, self.seed)
        self.load_chunks = self.chunks.copy()
        self.player = player.Player(self)

    def render(self, screen):#отрисовка
        mousepos = pygame.mouse.get_pos()#позиция указателя мыши
        for x in range(self.load_distance * 2 + 1):
            for y in range(self.load_distance * 2 + 1):
                chunkpos = [(self.center_chunk[0] + x - 3) * 320 + self.scroll[0] + int(self.W / 2), (self.center_chunk[1] + y - 3) * 320 + self.scroll[1] + int(self.H / 2)]
                if (chunkpos[0] > self.display_scale[0] and chunkpos[0] < self.display_scale[2]) and (chunkpos[1] > self.display_scale[1] and chunkpos[1] < self.display_scale[3]):
                    self.load_chunks[f"{self.center_chunk[0] + x - 3}_{self.center_chunk[1] + y - 3}"].draw(screen, self.scroll)
        self.player.draw(screen)

    def loading_chunks(self):#подгрузка чанков
        self.center_chunk = [-math.floor((self.scroll[0] + 320) / 320), -math.floor((self.scroll[1] + 320) / 320)]#позиция центрального чанка
        if self.center_chunk != self.last_center_chunk:
            self.load_chunks = {}
            for x in range(self.load_distance * 2 + 1):
                for y in range(self.load_distance * 2 + 1):
                    load_chunk_pos = f"{self.center_chunk[0] + x - 3}_{self.center_chunk[1] + y - 3}"
                    try:
                        ch = self.chunks[load_chunk_pos]
                        self.load_chunks[load_chunk_pos] = ch
                    except:
                        self.chunks[load_chunk_pos] = chunk.Chunk((self.center_chunk[0] + x - 3, self.center_chunk[1] + y - 3), self, self.seed)
                        self.load_chunks[load_chunk_pos] = self.chunks[load_chunk_pos]
        self.last_center_chunk = self.center_chunk.copy()

    def set_and_remove_blocks(self, blockdata):#установка и разрушение блоков
        mousepos = pygame.mouse.get_pos()#позиция указателя мыши
        #поиск нажатого чанка
        ch_pos = [
            -int_or_round((self.scroll[0] + int(self.W / 2) - mousepos[0]) / 320),
            -int_or_round((self.scroll[1] + int(self.H / 2) - mousepos[1]) / 320)
            ]
        ch = self.load_chunks[f"{ch_pos[0]}_{ch_pos[1]}"]
        pos = [
                ch.pos[0] * 320 + self.scroll[0] + int(self.W / 2),
                ch.pos[1] * 320 + self.scroll[1] + int(self.H / 2)
                ]
        #позиция нажатого блока
        blockpos = [
            int((mousepos[0] - pos[0]) / 20),
            int((mousepos[1] - pos[1]) / 20)
            ]
        #ограничитель
        if blockpos[0] < 0:
            blockpos[0] = 0
        elif blockpos[0] > 15:
            blockpos[0] = 15
        if blockpos[1] < 0:
            blockpos[1] = 0
        elif blockpos[1] > 15:
            blockpos[1] = 15
        clicked_chunk = ch#чанк, на который нажали
        clicked_block = clicked_chunk.blocks[blockpos[0]][blockpos[1]]#блок, на который нажали
        if pygame.mouse.get_pressed()[2]:#сломать блок
            if clicked_block.name != "air":
                clicked_chunk.blocks[blockpos[0]][blockpos[1]] = blocks.Air((ch_pos[0] * 16 + blockpos[0], ch_pos[1] * 16 + blockpos[1]), self)
        elif pygame.mouse.get_pressed()[0]:#установить блок
            if clicked_block.name == "air":
                block = blocks.blocks[blockdata["Type"]]((ch_pos[0] * 16 + blockpos[0], ch_pos[1] * 16 + blockpos[1]), self)
                clicked_chunk.blocks[blockpos[0]][blockpos[1]] = block
        clicked_chunk.change_image()#сменить текстуру у нажатого чанка

    def select_block(self):
        mousepos = pygame.mouse.get_pos()#позиция указателя мыши
        #поиск нажатого чанка
        ch_pos = [
            -int_or_round((self.scroll[0] + int(self.W / 2) - mousepos[0]) / 320),
            -int_or_round((self.scroll[1] + int(self.H / 2) - mousepos[1]) / 320)
            ]
        ch = self.load_chunks[f"{ch_pos[0]}_{ch_pos[1]}"]
        pos = [
                ch.pos[0] * 320 + self.scroll[0] + int(self.W / 2),
                ch.pos[1] * 320 + self.scroll[1] + int(self.H / 2)
                ]
        #позиция нажатого блока
        blockpos = [
            int((mousepos[0] - pos[0]) / 20),
            int((mousepos[1] - pos[1]) / 20)
            ]
        #ограничитель
        if blockpos[0] < 0:
            blockpos[0] = 0
        elif blockpos[0] > 15:
            blockpos[0] = 15
        if blockpos[1] < 0:
            blockpos[1] = 0
        elif blockpos[1] > 15:
            blockpos[1] = 15
        clicked_chunk = ch#чанк, на который нажали
        clicked_block = clicked_chunk.blocks[blockpos[0]][blockpos[1]]#блок, на который нажали
        if pygame.mouse.get_pressed()[1]:#выбрать блок
            return(clicked_chunk.blocks[blockpos[0]][blockpos[1]].name)
        

    def block_in_pos(self, x, y):
        chunkx = int(x / 16)
        chunky = int(y / 16)
        ch = self.load_chunks[f"{chunkx}_{chunky}"]
        bl = ch.blocks[x % 16][y % 16]
        return(bl)

    def update(self, screen, events):
        #перемещение
        self.player.update(events)
        #подгрузка чанков
        self.loading_chunks()
        #отрисовка
        self.render(screen)
