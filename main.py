import pygame
from defs import Settings
from player import Player

class TheGame:

    # public:

    def __init__(self):
        #init
        self.settings = None
        self.dt = None
        self.running = None
        self.clock = None
        self.screen = None
        #setup
        self.player = None

    def init_game(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.get_width(), self.settings.get_height()))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def setup_game(self):
        self.player = Player(pygame.math.Vector2(self.settings.player_pos()))

    def main_loop(self):
        while self.running:
            self.__get_input()
            self.__update_objects()
            self.__draw_objects()
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

    # private:

    def __get_input(self):
        for event in pygame.event.get():
            self.__quit(event)

        keys = pygame.key.get_pressed()
        self.__control_player(keys)

    def __update_objects(self):
        self.player.update(self.dt)

    def __draw_objects(self):
        self.screen.fill(self.settings.bg_color())
        self.player.draw(self.screen)

    def __quit(self,event):
        if event.type == pygame.QUIT:
            self.running = False

    def __control_player(self,keys):
        vel_x = (keys[pygame.K_d] - keys[pygame.K_a]) * self.player.MAX_VELOCITY
        vel_y = (keys[pygame.K_s] - keys[pygame.K_w]) * self.player.MAX_VELOCITY
        self.player.setVelocity(pygame.math.Vector2(vel_x, vel_y))






if __name__ == "__main__":
    game = TheGame()
    game.init_game()
    game.setup_game()
    game.main_loop()
