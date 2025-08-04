import pygame
import random

# intialize screen
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector-")

# intialize color
BACKGROUND_COLOR = (15, 23, 42)     
COIN_COLOR = (255, 215, 0)           
PLAYER_COLOR = (0, 255, 127)        
OBSTACLE_COLOR = (255, 76, 76)      
TEXT_COLOR = (241, 245, 249)

# intailze player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5