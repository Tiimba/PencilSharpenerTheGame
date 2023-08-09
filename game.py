import pygame
from pygame.locals import *
 
class PencilSharpenerGame:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
    
    # START GAME STATES
    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type in (KEYDOWN, KEYUP):
            keys = pygame.key.get_pressed()
            self.handle_keys(keys)

    def on_loop(self):
        self.clock.tick(60)

    def on_render(self):
        pass

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
        # pass