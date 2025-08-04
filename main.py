import pygame
import random

pygame.init()
screen_width, screen_height = 600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector")

# Colors
BACKGROUND_COLOR = (15, 23, 42)
COIN_COLOR = (255, 215, 0)
PLAYER_COLOR = (0, 255, 127)
OBSTACLE_COLOR = (255, 76, 76)
TEXT_COLOR = (241, 245, 249)

# Player
player_width, player_height = 50, 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Obstacle
obstacle_width, obstacle_height = 100, 20
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_increase = 0.2

# Coin
coin_radius = 15
coin_x = random.randint(coin_radius, screen_width - coin_radius)
coin_y = -coin_radius
coin_speed = 4
coin_speed_increase = 0.2

# Game state
clock = pygame.time.Clock()
score = 0
normal_font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 72)
dark_mode = True

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                player_x = screen_width // 2 - player_width // 2
                player_y = screen_height - player_height - 10
                obstacle_x = random.randint(0, screen_width - obstacle_width)
                obstacle_y = -obstacle_height
                obstacle_speed = 3
                coin_x = random.randint(coin_radius, screen_width - coin_radius)
                coin_y = -coin_radius
                coin_speed = 4
                score = 0

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            if player_x < 0:
                player_x = 0
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            if player_x > screen_width - player_width:
                player_x = screen_width - player_width

        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacle_speed += obstacle_speed_increase

        coin_y += coin_speed
        if coin_y > screen_height:
            coin_x = random.randint(coin_radius, screen_width - coin_radius)
            coin_y = -coin_radius
            coin_speed += coin_speed_increase

        # Rectangles for collision detection
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius, coin_radius*2, coin_radius*2)

        if player_rect.colliderect(obstacle_rect):
            game_over = True

        if player_rect.colliderect(coin_rect):
            score += 10
            coin_x = random.randint(coin_radius, screen_width - coin_radius)
            coin_y = -coin_radius

    # Draw
    if dark_mode:
        screen.fill(BACKGROUND_COLOR)
    else:
        screen.fill((255, 255, 255))

    if game_over:
        game_over_text = game_over_font.render("GAME OVER", True, TEXT_COLOR)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                     screen_height // 2 - game_over_text.get_height() // 2))
        score_text = normal_font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2,
                                 screen_height // 2 + game_over_text.get_height() // 2))
    else:
        pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle_rect)
        pygame.draw.circle(screen, COIN_COLOR, (coin_x, coin_y), coin_radius)
        score_text = normal_font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
