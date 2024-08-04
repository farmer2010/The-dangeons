import pygame
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos, name="air"):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] * 20
        self.rect.y = self.pos[1] * 20

    def draw(self, screen):#отрисовка
        screen.blit(self.image, self.rect)

    def update(self):
        pass

    def blockupdate(self):
        pass
