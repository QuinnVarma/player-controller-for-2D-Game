import pygame
from spritesheet import SpriteSheet

def get_frames(state):
    SPRITE_PATH = {
        'IDLE': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Idle (32x32).png',
        'RUN': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Run (32x32).png',
        'JUMP': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Jump (32x32).png',
        'FALL': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Fall (32x32).png',
        'HIT': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Hit (32x32).png',
        'DOUBLE_JUMP': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Double Jump (32x32).png',
        'WALL_JUMP': './Assets/textures/Pixel Adventure 1/Free/Main Characters/Ninja Frog/Wall Jump (32x32).png'
    }

    SPRITE_FRAMES = {
        'IDLE_RIGHT': SpriteSheet(SPRITE_PATH['IDLE'], 32, 32, scale=pygame.math.Vector2(2, 2)).get_frames(),
        'IDLE_LEFT':SpriteSheet(SPRITE_PATH['IDLE'], 32, 32, scale=pygame.math.Vector2(-2, 2)).get_frames(),
        'RUN_RIGHT': SpriteSheet(SPRITE_PATH['RUN'], 32, 32, scale=pygame.math.Vector2(2, 2)).get_frames(),
        'RUN_LEFT': SpriteSheet(SPRITE_PATH['RUN'], 32, 32, scale=pygame.math.Vector2(-2, 2)).get_frames(),
        'HIT': SpriteSheet(SPRITE_PATH['JUMP'], 32, 32, scale=pygame.math.Vector2(2, 2)).get_frames(),
        'DODGE': SpriteSheet(SPRITE_PATH['DOUBLE_JUMP'], 32, 32,scale=pygame.math.Vector2(2, 2)).get_frames()
    }

    return SPRITE_FRAMES[state]


class Player:
    def __init__(self,init_pos, init_state = 'IDLE_LEFT'):

        self.sprites = get_frames(init_state)
        self.curr_frame = 0

        self.position = init_pos
        self.screen_pos = pygame.math.Vector2(init_pos)

        self.goal_velocity = pygame.math.Vector2(0,0)
        self.velocity = pygame.math.Vector2(0,0)
        self.MAX_VELOCITY = 250
        self.drag = 5

        self.state = init_state


    def update(self,dt):

        self.__stateThink()

        self.velocity = (self.velocity.lerp(self.goal_velocity, dt * 100 / self.drag))
        self.position += self.velocity * dt
        self.curr_frame = (self.curr_frame + (dt * 24)) % len(self.sprites)

    def draw(self, screen):
        screen.blit(self.sprites[int(self.curr_frame)], self.position)

    def setVelocity(self,new_goal):
        self.goal_velocity = new_goal

    # private

    def __switchStates(self,new_state):
        self.state = new_state
        self.curr_frame = 0
        self.sprites = get_frames(new_state)

    def __stateThink(self):
        epsilon = 80

        match self.state:
            case 'IDLE_RIGHT':
                if self.velocity.x > epsilon or (abs(self.velocity.y) > epsilon and abs(self.velocity.x) < epsilon):
                    self.__switchStates('RUN_RIGHT')
                elif self.velocity.x < -epsilon:
                    self.__switchStates('RUN_LEFT')
            case 'IDLE_LEFT':
                if self.velocity.x < -epsilon or (abs(self.velocity.y) > epsilon and abs(self.velocity.x) < epsilon):
                    self.__switchStates('RUN_LEFT')
                elif self.velocity.x > epsilon:
                    self.__switchStates('RUN_RIGHT')
            case 'RUN_RIGHT':
                if abs(self.velocity.length_squared()) < epsilon:
                    self.__switchStates('IDLE_RIGHT')
                if self.velocity.x < -epsilon:
                    self.__switchStates('RUN_LEFT')
            case 'RUN_LEFT':
                if abs(self.velocity.length_squared()) < epsilon:
                    self.__switchStates('IDLE_LEFT')
                if self.velocity.x > epsilon:
                    self.__switchStates('RUN_RIGHT')


