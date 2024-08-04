import pygame
pygame.init()

def int_or_round(x):
    if x > 0:
        return(int(x) + 1)
    return(int(x))

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, world, obj, scale):
        self.world = world
        self.object = obj
        self.image = pygame.Surface(scale)
        self.rect = self.image.get_rect()
        self.rect.x = self.object.display_pos[0]
        self.rect.y = self.object.display_pos[1]

    def collide(self):
        return(False)
        ch_pos = [
            -int_or_round((self.world.scroll[0] + int(self.world.W / 2) - self.object.display_pos[0]) / 320),
            -int_or_round((self.world.scroll[1] + int(self.world.H / 2) - self.object.display_pos[1]) / 320)
            ]
        pos = [
            ch_pos[0] * 320 + self.world.scroll[0] + int(self.world.W / 2),
            ch_pos[1] * 320 + self.world.scroll[1] + int(self.world.H / 2)
            ]
        block_pos_in_chunk = [
            int((self.object.display_pos[0] - pos[0]) / 20),
            int((self.object.display_pos[1] - pos[1]) / 20)
            ]
        blockpos = [
            ch_pos[0] * 16 + block_pos_in_chunk[0],
            ch_pos[1] * 16 + block_pos_in_chunk[1]
            ]
        return(self.world.block_in_pos(blockpos[0], blockpos[1]).name != "air")
