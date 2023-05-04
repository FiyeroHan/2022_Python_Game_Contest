import pygame

class Intro:
    def __init__(self, surface, create_overworld):
        self.display_surface = surface
        self.create_overworld = create_overworld
        self.page = 0
        self.min_page=1
        self.max_page=3
        self.page_timer=0

        pygame.mixer.init()

        pygame.mixer.music.load('module/items/overworld/OverWorld.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)


   

    def input(self):
        keys = pygame.key.get_pressed()

        self.page_timer += 1

        if self.page==0 and keys[pygame.K_SPACE]:
            self.page = 1
            self.page_timer=0

        elif keys[pygame.K_RIGHT] and self.page < self.max_page and self.page_timer>10:
            self.page_timer = 0
            self.page += 1
        elif keys[pygame.K_LEFT] and self.min_page<self.page and self.page_timer>10:
            self.page_timer = 0
            self.page -= 1
        elif keys[pygame.K_SPACE] and self.page == self.max_page and self.page_timer>10:
            self.page_timer = 0
            self.create_overworld(0,0)

    def setup_page(self):
        if self.page == 0:
            self.bg_img=pygame.image.load('module/items/intro/first.png')

        elif self.page == 1:
            self.bg_img=pygame.image.load('module/items/intro/page_0.png')
        
        elif self.page == 2:
            self.bg_img=pygame.image.load('module/items/intro/page_1.png')

        elif self.page == 3:
            self.bg_img=pygame.image.load('module/items/intro/page_2.png')     

    def run(self):
        self.input()
        self.setup_page()
        self.display_surface.blit(self.bg_img,(0,0))
