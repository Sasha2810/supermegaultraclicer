import pygame
from boss import Boss
from level_changer import LevelChanger

class BossMenu:
    def __init__(self):
        self.blocks = []
        self.fill_boss_info()
        self.fill_level_changers()

    def fill_boss_info(self):
        for i in range(1, 5):
            self.blocks.append(Boss(i,  i * 100))

    def fill_level_changers(self):
        self.blocks.insert(0, LevelChanger('left'))
        self.blocks.append(LevelChanger('right'))


    def draw_blocks(self, screen):
        for block in self.blocks:
            block.draw_block(screen)






























































