import pygame
from random import randint
from module.game_data import levels

class Piece(pygame.sprite.Sprite):
    def __init__(self, surface, current_level, amount):
        super().__init__()

        self.display_surface = surface
        self.amount = amount
        self.need_to_clear = levels[current_level]['need_to_clear']


        self.image = pygame.image.load(levels[current_level]['piece_img']).convert_alpha()
        self.rect = self.image.get_rect(topleft = (randint(1280,1300),randint(50,680)))

        self.ui_rect = self.image.get_rect(topleft = (70, 50))

        self.back_surf = pygame.Surface((164,44)).convert_alpha()
        self.back_surf.fill((255,255,255))
        self.back_rect = self.back_surf.get_rect(topleft=(69,49))

        self.font = pygame.font.Font(None, 40)

    
    def piece_UI(self, amount):
        self.display_surface.blit(self.back_surf,self.back_rect)
        self.display_surface.blit(self.image, self.ui_rect)
        piece_amount_surf = self.font.render(f'{amount}/{self.need_to_clear}', False, (0,0,0))
        piece_amount_rect = piece_amount_surf.get_rect(midleft = (self.ui_rect.right + 6,self.ui_rect.centery))
        self.display_surface.blit(piece_amount_surf,piece_amount_rect)

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.rect.x -= 4
        self.piece_UI(self.amount)
        self.destroy()
