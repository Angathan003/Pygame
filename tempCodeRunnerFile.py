import pygame

# Set up the game window
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up the game objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_paddle = pygame.Rect(50, screen_height/2 - 70, 20, 140)
opponent_paddle = pygame.Rect(screen_width - 70, screen_height/2 - 70, 20, 140)

# Set up the game variables
ball_speed_x = 2
ball_speed_y = 2
player_speed = 0
opponent_speed = 1
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 64)

# Set up the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -5
            elif event.key == pygame.K_DOWN:
                player_speed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Move the player paddle
    player_paddle.y += player_speed
    if player_paddle.top <= 0:
        player_paddle.top = 0
    elif player_paddle.bottom >= screen_height:
        player_paddle.bottom = screen_height

    # Move the opponent paddle
    if ball.y < opponent_paddle.y:
        opponent_paddle.y -= opponent_speed
    elif ball.y > opponent_paddle.y:
        opponent_paddle.y += opponent_speed
    if opponent_paddle.top <= 0:
        opponent_paddle.top = 0
    elif opponent_paddle.bottom >= screen_height:
        opponent_paddle.bottom = screen_height

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        opponent_score += 1
        ball_speed_x = -ball_speed_x
    elif ball.right >= screen_width:
        player_score += 1
        ball_speed_x = -ball_speed_x

    # Check for collisions with the paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x = -ball_speed_x

    # Draw the game objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player_paddle)
    pygame.draw.rect(screen, (255, 255, 255), opponent_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width/2, 0), (screen_width/2, screen_height))

    # Draw the scores
    player_text = font.render(str(player_score), True, (255, 255, 255))
    opponent_text = font.render(str(opponent_score), True, (255, 255, 255))
    screen.blit(player_text, (screen_width/4, 10))
    screen.blit(opponent_text, (screen_width*3/4 - opponent_text.get_width(), 10))

    # Update the screen
    pygame.display.flip()
