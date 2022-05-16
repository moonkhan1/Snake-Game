import random
import pygame
import time

# Init pygame
pygame.init()

white = (255, 255, 255)  # snake
black = (0, 0, 0)  # background
red = (255, 0, 0)  # Messages
orange = (255, 165, 0)  # foods, score

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)


def show_score(score):
    text = score_font.render("Score: " + str(score), True, orange)  # True - anti-alias
    game_display.blit(text, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])


def run_game():
    game_over = False
    game_close = False

    # Starting position
    x = width / 2
    y = height / 2

    # Till we have not done smt yet, snake will be at the center of the window:
    x_speed = 0
    y_speed = 0

    # Define snake as a list. He is going to grow and we will need to add more blocks
    snake_pixels = []
    snake_length = 1  # length of the snake at the beginning

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0  # width - snake_size will create enough space for snake itself
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    # MAIN game loop
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_UP:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size  # Cunki eded oxu uzerinde baxsaq, ilan sola getdikce x oxu menfi olan isdiqametde getmis olacaq
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        # Eger ilan serhedlerin xaricine cixarsa, oyunu bitir:
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        # Ilanini davamli hereketini temin edir
        x += x_speed
        y += y_speed

        game_display.fill(black)  # background color
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])  # target

        # ilan irellemesi onun quyrugunun son hissesinin head hissesine elave edilmesi ile devam edir
        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:  # All snke pixels except head
            if pixel == [x, y]:  # Eger ilan oz ozune beraber olarsa, yeni ozune deyerse
                game_close = True

        draw_snake(snake_size, snake_pixels)
        show_score(snake_length - 1)  # Oyuna baslarken 1 pixel ilan olaraq baslayir ve hedef yedikce xal qazanir. Baslarken 1 pixel oldugu ucun score da 0 olacaq

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0  # width - snake_size will create enough space for snake itself
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)  # Hedef yenildikce sureti artir
    pygame.quit()
    quit()
run_game()
