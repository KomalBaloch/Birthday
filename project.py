import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Birthday Animation")

# Colors
BG_COLOR = (255, 236, 210)
CAKE_BOTTOM = (255, 111, 97)
CAKE_MID = (255, 138, 128)
CAKE_TOP = (255, 193, 193)
CANDLE = (255, 255, 255)
FLAME = (255, 223, 0)
GIRL = (51, 51, 51)
SPARKLE = (255, 215, 0)
TEXT_COLOR = (43, 43, 43)

# Fonts
pygame.font.init()
title_font = pygame.font.SysFont('PlayfairDisplay', 48)
subtitle_font = pygame.font.SysFont('GreatVibes', 36)
text_font = pygame.font.SysFont('Arial', 24)
footer_font = pygame.font.SysFont('PlayfairDisplay', 28)

# Sparkle positions
sparkles = [[random.randint(0, WIDTH), random.randint(0, HEIGHT//2)] for _ in range(20)]

# Hand animation
hand_x = 410
hand_y = 320
hand_dir = 1

clock = pygame.time.Clock()

def draw_cake():
    # Cake layers
    pygame.draw.rect(screen, CAKE_BOTTOM, (350, 350, 100, 30))
    pygame.draw.rect(screen, CAKE_MID, (360, 330, 80, 30))
    pygame.draw.rect(screen, CAKE_TOP, (370, 310, 60, 30))
    # Candle
    pygame.draw.rect(screen, CANDLE, (395, 290, 10, 20))
    pygame.draw.ellipse(screen, FLAME, (393, 280, 14, 14))

def draw_girl():
    # Body
    pygame.draw.rect(screen, GIRL, (400, 250, 20, 60))
    # Head
    pygame.draw.ellipse(screen, GIRL, (395, 230, 30, 30))
    # Hand (moving)
    pygame.draw.rect(screen, GIRL, (hand_x, hand_y, 30, 5))

def draw_sparkles():
    for s in sparkles:
        pygame.draw.circle(screen, SPARKLE, (s[0], s[1]), 4)
        s[1] -= 2
        s[0] += random.choice([-1,0,1])
        if s[1] < 0:
            s[1] = HEIGHT
            s[0] = random.randint(0, WIDTH)

def draw_texts():
    title = title_font.render("Dear Myself,", True, TEXT_COLOR)
    subtitle = subtitle_font.render("🎂 Happy Birthday!", True, TEXT_COLOR)
    message = text_font.render("May this year bring peace and happiness.", True, TEXT_COLOR)
    thought = text_font.render("Now I will be happy...", True, TEXT_COLOR)
    footer = footer_font.render("Komal Sakhidad", True, TEXT_COLOR)

    screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
    screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 90))
    screen.blit(message, (WIDTH//2 - message.get_width()//2, 140))
    screen.blit(thought, (WIDTH//2 - thought.get_width()//2, 200))
    screen.blit(footer, (WIDTH//2 - footer.get_width()//2, HEIGHT-50))

# Main loop
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animate hand
    hand_x += hand_dir
    if hand_x > 430 or hand_x < 390:
        hand_dir *= -1

    draw_cake()
    draw_girl()
    draw_sparkles()
    draw_texts()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
