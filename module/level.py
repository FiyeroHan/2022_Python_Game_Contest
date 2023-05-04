import pygame
from random import choice

from module.game_data import levels
from module.player import Player
from module.obstacle import Obstacle
from module.piece import Piece

class Level:
    def __init__(self, current_level, surface, create_overworld):
        
        # 맵 기본 세팅
        pygame.mixer.init()
        self.display_surface = surface
        self.current_level = current_level
        level_data = levels[current_level]
        self.next_level = level_data['next']
        self.create_overworld = create_overworld
        self.need_to_clear = level_data['need_to_clear']
        self.bg_map = pygame.image.load(level_data['bg_map']).convert()
        pygame.mixer.music.load(level_data['music'])
        self.clear_sound = pygame.mixer.Sound(level_data['clear_sound'])
        self.get_piece_sound = pygame.mixer.Sound('module/items/level/get_piece.mp3')
        self.collision_sound = pygame.mixer.Sound('module/items/level/collision.mp3')

        # 플레이어
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())

        # 장애물
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_timer = 0
        
        # 조각
        self.piece_amount = 0
        self.piece_group = pygame.sprite.Group()
        self.piece_timer = 0

        # 음악재생
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)



    def result(self):
        if self.piece_amount >= self.need_to_clear:
            self.create_overworld(self.current_level,self.next_level)
            self.clear_sound.play()
            self.clear_sound.set_volume(0.4)
        if pygame.sprite.spritecollide(self.player.sprite,self.obstacle_group,False) or self.player.sprite.rect.y>800 or self.player.sprite.rect.y<-100:
            self.create_overworld(self.current_level,0)
            self.obstacle_group.empty()
            self.piece_group.empty()
            self.collision_sound.play()
            self.collision_sound.set_volume(0.4)
                

    
    def create_obstacle(self):
        self.obstacle_timer += 0.015
        if int(self.obstacle_timer) == 1:
            self.obstacle_group.add(Obstacle(choice(['long_bttm','long_top','short_bttm','short_top']),self.current_level))
            self.obstacle_timer = 0

    def create_piece(self):
        self.piece_timer += 0.05
        if int(self.piece_timer) == 1:
            self.piece_group.add(Piece(self.display_surface,self.current_level,self.piece_amount))
            self.piece_timer = 0

    def piece_collisions(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.piece_group,True):
            self.piece_amount += 1
            self.get_piece_sound.play()
            self.get_piece_sound.set_volume(0.1)

    def run(self):

        self.result()
        self.display_surface.blit(self.bg_map,(0,0))

        self.player.draw(self.display_surface)
        self.player.update()

        self.create_piece()
        self.piece_collisions()        
        self.piece_group.draw(self.display_surface)
        self.piece_group.update()

        self.create_obstacle()
        self.obstacle_group.draw(self.display_surface)
        self.obstacle_group.update()