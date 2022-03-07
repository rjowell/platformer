import pygame, random

class Platforms(pygame.sprite.Sprite):

    def __init__(self, pos, img_path, width=70, height=70):
        super().__init__()
        self.image = pygame.Surface([width, height]).convert()
        self.image.blit(pygame.image.load(img_path).convert(), (0, 0), (0, 0, width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def scroll(self, change):
        screen_info = pygame.display.Info()
        self.rect.top += change
        if self.rect.top > screen_info.current_h:
            self.rect.top = -50
            self.rect.left = random.randint(5, (screen_info.current_w-50)//10)*10


    '''
    create a Platforms class, subclass of pygame.sprite.Sprite
  needs pygame and random
 init method: position, img_path, width, height
  add a scroll method with 1 param ' change'
  
  '''
