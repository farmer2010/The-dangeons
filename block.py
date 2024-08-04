import pygame
pygame.init()

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

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos, game_world, name="air"):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.pos = pos
        self.pos2 = [
            self.pos[0] % 16,
            self.pos[1] % 16
        ]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] % 16 * 20
        self.rect.y = self.pos[1] % 16 * 20
        self.world = game_world

    def draw(self, screen):#отрисовка
        screen.blit(self.image, self.rect)

    def update(self):
        pass

    def blockupdate(self):
        pass
