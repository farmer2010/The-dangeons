import random
import block
import pygame
import copy
pygame.init()

airimg = pygame.Surface((20, 20))
airimg.set_colorkey((0, 0, 0))
texture = pygame.image.load("images/blocks.png")

def get_image(x, y, size=20):
    x2 = x * 10
    y2 = y * 10
    img = pygame.Surface((10, 10))
    img.fill((255, 0, 128))
    img.set_colorkey((255, 0, 128))
    img.blit(texture, (-x2, -y2))
    img = pygame.transform.scale(img, (size, size))
    return(img)

class Air(block.Block):#воздух
    def __init__(self, pos):
        block.Block.__init__(self, airimg, pos)
        
class Stone(block.Block):#камень
    def __init__(self, pos):
        block.Block.__init__(self, get_image(0, 0), pos, name="stone")

class CoalOre(block.Block):#угольная руда
    def __init__(self, pos):
        block.Block.__init__(self, get_image(2, 0), pos, name="coal_ore")

class IronOre(block.Block):#железная руда
    def __init__(self, pos):
        block.Block.__init__(self, get_image(3, 0), pos, name="iron_ore")

class CopperOre(block.Block):#медная руда
    def __init__(self, pos):
        block.Block.__init__(self, get_image(4, 0), pos, name="copper_ore")

class Torch(block.Block):#факел
    def __init__(self, pos):
        block.Block.__init__(self, get_image(0, 4), pos, name="torch")

class Lamp(block.Block):#фонарь
    def __init__(self, pos):
        block.Block.__init__(self, get_image(1, 1), pos, name="lamp")

class Chest(block.Block):#сундук
    def __init__(self, pos, isleft=0):
        block.Block.__init__(self, get_image(isleft, 3), pos, name="chest")

class SpiderNet(block.Block):#паутина
    def __init__(self, pos, mode=random.randint(0, 4), spider=random.randint(0, 4)):
        block.Block.__init__(self, get_image(5 + mode, spider), pos, name="spider_net")

class Trotil(block.Block):#динамит(тротил)
    def __init__(self, pos):
        block.Block.__init__(self, get_image(4, 2), pos, name="trotil")

class Pumpkin(block.Block):#тыква
    def __init__(self, pos):
        block.Block.__init__(self, get_image(4, 3), pos, name="pumpkin")

class Furnace(block.Block):#печь
    def __init__(self, pos):
        block.Block.__init__(self, get_image(0, 2), pos, name="furnace")

class Soil(block.Block):#земля
    def __init__(self, pos):
        block.Block.__init__(self, get_image(9, 0), pos, name="soil")

class Water(block.Block):#вода
    def __init__(self, pos, floor):
        floor_img = get_image(floor[0], floor[1])
        image2 = get_image(9, 1)
        image2 = image2.convert_alpha()
        image2.set_alpha(100)
        floor_img.blit(image2, (0, 0))
        block.Block.__init__(self, floor_img, pos, name="water")

class StoneFloor(block.Block):#каменный пол
    def __init__(self, pos):
        block.Block.__init__(self, get_image(1, 0), pos, name="stone_floor")

class SoilFloor(block.Block):#земляной пол
    def __init__(self, pos):
        image = get_image(9, 0)
        image2 = pygame.Surface([20, 20])
        image2.fill((0, 0, 0))
        image2 = image2.convert_alpha()
        image2.set_alpha(100)
        image.blit(image2, (0, 0))
        block.Block.__init__(self, image, pos, name="soil_floor")
