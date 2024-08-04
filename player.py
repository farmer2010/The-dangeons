import hitbox
import pygame
import blocks
import copy
pygame.init()

class Player():
    def __init__(self, world):
        self.world = world
        self.pos = [0, 0]
        self.speed = 5
        self.display_pos = [
            int(self.world.W / 2) - 15,
            int(self.world.H / 2) - 25
            ]
        self.hitbox = hitbox.Hitbox(self.world, self, (30, 50))
        self.mousedown = False
        self.selected_block = {"Type" : "stone", "Tags" : {}}

    def update(self, events):
        #перемещение
        keys = pygame.key.get_pressed()
        up = keys[pygame.K_w]
        down = keys[pygame.K_s]
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        if up:
            self.pos[1] += self.speed
            if self.hitbox.collide():
                self.pos[1] -= self.speed
        elif down:
            self.pos[1] -= self.speed
            if self.hitbox.collide():
                self.pos[1] += self.speed
        elif left:
            self.pos[0] += self.speed
            if self.hitbox.collide():
                self.pos[0] -= self.speed
        elif right:
            self.pos[0] -= self.speed
            if self.hitbox.collide():
                self.pos[0] += self.speed
        self.world.scroll = self.pos
        #установка и разрушение блоков
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousedown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mousedown = False
        if self.mousedown:
            self.world.set_and_remove_blocks(self.selected_block)
            new_block = self.world.select_block()
            if new_block != "air" and new_block != self.selected_block["Type"] and new_block != None:
                self.selected_block["Type"] = new_block

    def draw(self, screen):
        pass
        #screen.blit(self.hitbox.image, self.hitbox.rect)
