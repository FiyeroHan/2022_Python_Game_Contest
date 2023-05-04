import pygame
from module.game_data import levels
from time import sleep

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status):
        super().__init__()
        if status == 'clear':
            self.image = pygame.image.load('module/items/overworld/node_clear_yellow.png').convert_alpha()
        elif status == 'available':
            self.image = pygame.image.load('module/items/overworld/node_available_yellow.png').convert_alpha()
        else:
            self.image = pygame.image.load('module/items/overworld/node_locked.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)

class Icon(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('module/items/sprite4.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)

class Overworld:
    def __init__(self, start_level, max_level, surface, create_level):
        # setup
        self.display_surface = surface
        self.max_level= max_level
        self.current_level = start_level
        self.create_level = create_level
        self.game_active = True
        self.bg_map = pygame.image.load('module/items/overworld/OverWorld.png')
        if self.max_level == 4:
            self.game_active = False
            self.bg_map = pygame.image.load('module/items/overworld/clear_screen.png')

        # sprites
        self.setup_nodes()
        self.setup_icon()

        # 음악 재생
        pygame.mixer.init()

        pygame.mixer.music.load('module/items/overworld/OverWorld.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels):
            if index < self.max_level:
                node_sprite = Node(node_data['pos'],'clear')
            elif index == self.max_level:
                node_sprite = Node(node_data['pos'],'available')
            else:
                node_sprite = Node(node_data['pos'],'locked')
            self.nodes.add(node_sprite)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.current_level < self.max_level and not(self.current_level>=3):
            self.current_level += 1
            sleep(0.1)
        elif keys[pygame.K_LEFT] and self.current_level > 0:
            self.current_level -= 1
            sleep(0.1)
        elif keys[pygame.K_RETURN]:
            self.create_level(self.current_level)



    def update_icon_pos(self):
        self.icon.sprite.rect.center = (self.nodes.sprites()[self.current_level].rect.centerx-40,self.nodes.sprites()[self.current_level].rect.centery)

    def run(self):
        if self.game_active:
            self.display_surface.blit(self.bg_map,(0,0))
            self.input()
            self.update_icon_pos()
            self.nodes.draw(self.display_surface)
            self.icon.draw(self.display_surface)
        else:
            self.display_surface.blit(self.bg_map,(0,0))
