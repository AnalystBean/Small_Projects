import pygame

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong")

# Create the ball and paddles
ball = pygame.Surface((10, 10))
ball.fill((255, 255, 255))
ball_rect = ball.get_rect(center=(250, 250))

left_paddle = pygame.Surface((10, 50))
left_paddle.fill((255, 255, 255))
left_paddle_rect = left_paddle.get_rect(midleft=(10, 250))

right_paddle = pygame.Surface((10, 50))
right_paddle.fill((255, 255, 255))
right_paddle_rect = right_paddle.get_rect(midright=(490, 250))

# Set the ball's initial velocity
ball_velocity = [5, 5]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_rect.y -= 5
    if keys[pygame.K_s]:
        left_paddle_rect.y += 5
    if keys[pygame.K_UP]:
        right_paddle_rect.y -= 5
    if keys[pygame.K_DOWN]:
        right_paddle_rect.y += 5

    # Keep the paddles on the screen
    if left_paddle_rect.top < 0:
        left_paddle_rect.top = 0
    if left_paddle_rect.bottom > 500:
        left_paddle_rect.bottom = 500
    if right_paddle_rect.top < 0:
        right_paddle_rect.top = 0
    if right_paddle_rect.bottom > 500:
        right_paddle_rect.bottom = 500

    # Move the ball
    ball_rect = ball_rect.move(ball_velocity)

    # Check for collisions with the paddles
    if ball_rect.colliderect(left_paddle_rect) or ball_rect.colliderect(right_paddle_rect):
        ball_velocity[0] = -ball_velocity[0]

    # Check for collisions with the top and bottom of the screen
    if ball_rect.top < 0 or ball_rect.bottom > 500:
        ball_velocity[1] = -ball_velocity[1]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball and paddles
    screen.blit(ball, ball_rect)
    screen.blit(left_paddle, left_paddle_rect)
    screen.blit(right_paddle, right_paddle_rect)

    # Update the display
    pygame.display.flip()

    