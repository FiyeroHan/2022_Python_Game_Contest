import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('module/items/sprite4.png').convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(topleft = (150,360))
        self.gravity = 0
        self.air_timer = 0

        self.jump_sound = pygame.mixer.Sound('module/items/level/jump.mp3')
        self.jump_sound.set_volume(0.1)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.gravity += 0.8
        self.rect.y += self.gravity

        self.air_timer += 1

    def jump(self):
        if self.air_timer > 6:
            self.gravity = -9
            self.jump_sound.play()
            
            self.air_timer = 0

    def update(self):
        self.input()
        self.apply_gravity()