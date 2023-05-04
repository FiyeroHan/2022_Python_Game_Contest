import pygame, sys
from module.overworld import Overworld
from module.level import Level
from module.intro import Intro

class Play:
    def __init__(self):
        self.max_level = 0
        self.status = 'intro'
        self.intro = Intro(screen, self.create_overworld)

    def create_level(self,current_level):
        self.level = Level(current_level, screen, self.create_overworld)
        self.status = 'level'

    def create_overworld(self,current_level, next_level):
        if next_level > self.max_level:
            self.max_level = next_level
        self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
        self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'level':
            self.level.run()
        else:
            self.intro.run()


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
play = Play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill('black')
    play.run()

    pygame.display.update()
    clock.tick(60)

