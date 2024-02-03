import pygame


class SpriteSheet:

    # public :

    def __init__(self, image_path, width, height, scale):
        self.sheet = pygame.image.load(image_path)
        self.sprite_dimensions = (width, height)

        num_cols = int(self.sheet.get_width() / width)
        num_rows = int(self.sheet.get_height() / height)
        self.sheet_dimensions = (num_cols, num_rows)
        self.num_frames = num_rows * num_cols

        self.frames = []
        self.scale = scale
        self.__init_frame_list()


    def get_frames(self):
        return self.frames

    # private :

    def __get_frame_loc(self, frame):
        x = (frame % self.sheet_dimensions[0]) * self.sprite_dimensions[0]
        y = (frame // self.sheet_dimensions[0]) * self.sprite_dimensions[1]

        area = (x, y, x + self.sprite_dimensions[0], y + self.sprite_dimensions[1])

        return area

    def __get_image(self, frame, color):
        image = pygame.Surface(self.sprite_dimensions).convert_alpha()

        image.blit(self.sheet, (0, 0), self.__get_frame_loc(frame))
        image = pygame.transform.scale(image, (self.sprite_dimensions[0] * abs(self.scale.x), self.sprite_dimensions[1] * abs(self.scale.y)))
        image = pygame.transform.flip(image, self.scale.x < 0, self.scale.y < 0)
        image.set_colorkey(color)

        return image

    def __init_frame_list(self):
        for frame in range(self.num_frames):
            self.frames.append(self.__get_image(frame, "black"))