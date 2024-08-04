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
    def __init__(self, pos, game_world):
        block.Block.__init__(self, airimg, pos, game_world)
        
class Stone(block.Block):#камень
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(0, 0), pos, game_world, name="stone")

class CoalOre(block.Block):#угольная руда
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(2, 0), pos, game_world, name="coal_ore")

class IronOre(block.Block):#железная руда
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(3, 0), pos, game_world, name="iron_ore")

class CopperOre(block.Block):#медная руда
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(4, 0), pos, game_world, name="copper_ore")

class Torch(block.Block):#факел
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(0, 4), pos, game_world, name="torch")

class Lamp(block.Block):#фонарь
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(1, 1), pos, game_world, name="lamp")

class Chest(block.Block):#сундук
    def __init__(self, pos, game_world, isleft=0):
        block.Block.__init__(self, get_image(isleft, 3), pos, game_world, name="chest")

class SpiderNet(block.Block):#паутина
    def __init__(self, pos, game_world, mode=random.randint(0, 4)):
        block.Block.__init__(self, get_image(5 + mode, 0), pos, game_world, name="spider_net")

class Trotil(block.Block):#динамит(тротил)
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(4, 2), pos, game_world, name="trotil")

class Planks(block.Block):#доски
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(4, 3), pos, game_world, name="planks")

class Furnace(block.Block):#печь
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(0, 2), pos, game_world, name="furnace")

class Soil(block.Block):#земля
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(9, 0), pos, game_world, name="soil")

class Water(block.Block):#вода
    def __init__(self, pos, game_world, floor=[1, 0], shadow=128):
        image2 = pygame.Surface([20, 20])
        image2 = image2.convert_alpha()
        image2.set_alpha(shadow)
        floor_img = get_image(floor[0], floor[1])
        image = get_image(9, 1)
        image = image.convert_alpha()
        image.set_alpha(100)
        floor_img.blit(image2, (0, 0))
        floor_img.blit(image, (0, 0))
        block.Block.__init__(self, floor_img, pos, game_world, name="water")

class StoneFloor(block.Block):#каменный пол
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(1, 0), pos, game_world, name="stone_floor")

class SoilFloor(block.Block):#земляной пол
    def __init__(self, pos, game_world):
        image = get_image(9, 0)
        image2 = pygame.Surface([20, 20])
        image2.fill((0, 0, 0))
        image2 = image2.convert_alpha()
        image2.set_alpha(100)
        image.blit(image2, (0, 0))
        block.Block.__init__(self, image, pos, game_world, name="soil_floor")

class Bricks(block.Block):#каменные кирпичи
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(5, 1), pos, game_world, name="bricks")

class CrackedBricks(block.Block):#потрескавшиеся каменные кирпичи
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(6, 1), pos, game_world, name="cracked_bricks")

class MossyBricks(block.Block):#замшелые каменные кирпичи
    def __init__(self, pos, game_world):
        block.Block.__init__(self, get_image(7, 1), pos, game_world, name="mossy_bricks")

blocks = {
    "stone" : Stone,
    "air" : Air,
    "coal_ore" : CoalOre,
    "iron_ore" : IronOre,
    "copper_ore" : CopperOre,
    "torch" : Torch,
    "lamp" : Lamp,
    "chest" : Chest,
    "spider_net" : SpiderNet,
    "trotil" : Trotil,
    "planks" : Planks,
    "furnace" : Furnace,
    "soil" : Soil,
    "water" : Water,
    "stone_floor" : StoneFloor,
    "soil_floor" : SoilFloor,
    "bricks" : Bricks,
    "cracked_bricks" : CrackedBricks,
    "mossy_bricks" : MossyBricks
}
