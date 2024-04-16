import pygame
import sys

# 게임 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 블록 크기 및 개수
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 40
BLOCK_ROWS = 5
BLOCK_COLS = 8

# 패들 크기
PADDLE_WIDTH = 500
PADDLE_HEIGHT = 20
PADDLE_SPEED = 7

# 공 속도
BALL_SPEED = 5

# 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("블럭 깨기")

clock = pygame.time.Clock()

# 블록 그리기
def draw_blocks(block_list):
    for block in block_list:
        pygame.draw.rect(screen, BLUE, block)

# 패들 그리기
def draw_paddle(paddle_x):
    pygame.draw.rect(screen, RED, (paddle_x, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT))

# 공 그리기
def draw_ball(ball_x, ball_y):
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

# 게임 루프
def game_loop():
    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_dx = BALL_SPEED
    ball_dy = -BALL_SPEED

    # 블록 생성
    block_list = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block_rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
            block_list.append(block_rect)

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            paddle_x += PADDLE_SPEED

        # 패들이 화면 밖으로 나가지 않도록 제한
        paddle_x = max(0, min(SCREEN_WIDTH - PADDLE_WIDTH, paddle_x))

        # 공과 블록 충돌 감지
        ball_rect = pygame.Rect(ball_x - 10, ball_y - 10, 20, 20)
        for block in block_list[:]:
            if ball_rect.colliderect(block):
                block_list.remove(block)
                ball_dy = -ball_dy
                break

        # 벽과 충돌 감지
        if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy

        # 패들과 공 충돌 감지
        if ball_y >= SCREEN_HEIGHT - PADDLE_HEIGHT and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
            ball_dy = -ball_dy

        ball_x += ball_dx
        ball_y += ball_dy

        draw_blocks(block_list)
        draw_paddle(paddle_x)
        draw_ball(int(ball_x), int(ball_y))

        pygame.display.flip()
        clock.tick(60)

game_loop()
