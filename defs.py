import argparse
import pygame


# SETTINGS
def Settings():

    def get_width():
        return 500
    def get_height():
        return 500
    def player_pos():
        return pygame.math.Vector2(get_width()/2, get_height()/2)
    def bg_color():
        return "black"

    return argparse.Namespace(**locals())

