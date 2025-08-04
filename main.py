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

# intailze obtacle
obstacle_widht = 100
obstacle_height = 20
obstacle_width_x = random.randint(0, screen_width - obstacle_widht)
obstacle_height_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_incrase = 0.2

# intailize coin

coin_radius = 15
coin_x = random.randint(coin_radius, screen_width - coin_radius)
coin_y = -coin_radius
coin_speed = 4
coin_speed_incrase = 0.2

# Initialize game state variables and fonts

clock = pygame.time.Clock()
score = 0
normal_font = pygame.font(None, 36)
game_over_font = pygame.font(None, 72)
dark_mode = True

running = True
game_over = False

# game loop
while running:
  
    pygame.display.update()
    clock.tick(60)
pygame.quit()
