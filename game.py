import pygame
from pygame.locals import *
from sprites.pencil_sharper import PencilSharpener
import random


class PencilSharpenerGame:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
    
    # START GAME STATES
    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self._running = True
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.pencil_shaperner = PencilSharpener(image_path="sprites/up-seta.png", x= self.player_pos.x, y=self.player_pos.y)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type in (KEYDOWN, KEYUP):
            keys = pygame.key.get_pressed()
            self.handle_keys(keys)

    def on_loop(self):
        self.clock.tick(60)

    def on_render(self):
        self.screen.fill("black")
        self.screen.blit(self.pencil_shaperner.image, self.pencil_shaperner.rect)
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    # END GAME STATES

    def handle_keys(self, keys:any) -> None:
        if keys[pygame.K_w]:
            print("W pressed")
        if keys[pygame.K_s]:
            print("S pressed")
        if keys[pygame.K_a]:
            print("A pressed")
        if keys[pygame.K_d]:
            print("D pressed")
    
    def random_key_generator(self) -> any:
        possible_keys = (pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a)
        random_key_selected = random.choice(possible_keys)
        return random_key_selected