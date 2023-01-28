import pygame

# Initialize pygame
pygame.init()

# Set the screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Pong Game")

# Set the paddles and ball starting positions
paddle1_pos = [20, 200]
paddle2_pos = [660, 200]
ball_pos = [345, 195]

# Set the speed of the ball
ball_speed = [5, 5]

# Set the paddles' speed
paddle1_speed = 0
paddle2_speed = 0

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the font
font = pygame.font.Font(None, 30)

# Set the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the paddles
    paddle1_pos[1] += paddle1_speed
    paddle2_pos[1] += paddle2_speed
    
    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    
    # Check for ball hitting the top or bottom of the screen
    if ball_pos[1] <= 0 or ball_pos[1] >= 490:
        ball_speed[1] = -ball_speed[1]
    
    # Check for ball hitting the paddles
    if (ball_pos[0] <= paddle1_pos[0] + 20 and ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + 60) or (ball_pos[0] >= paddle2_pos[0] and ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + 60):
        ball_speed[0] = -ball_speed[0]
    
    # Check for ball going past the paddles
    if ball_pos[0] <= 0:
        running = False
        message = font.render("Player 2 wins!", True, white)
        screen.blit(message, (250, 250))
        pygame.display.flip()
        pygame.time.wait(3000)
    elif ball_pos[0] >= 680:
        running = False
        message = font.render("Player 1 wins!", True, white)
        screen.blit(message, (250, 250))
        pygame.display.flip()
        pygame.time.wait(3000)
    
    # Clear the screen
    screen.fill(black)
    
    # Draw the paddles and the ball
    pygame.draw.rect(screen, white, (paddle1_pos[0], paddle1_pos[1], 20, 60))
    pygame.draw.rect(screen, white, (paddle2_pos[0], paddle2_pos[1], 20, 60))
    pygame.draw.circle(screen, white, (int(ball_pos[0]), int(ball_pos[1])), 10)
    
        # Update the screen
    pygame.display.flip()
    
    # Control the speed of the game
    pygame.time.wait(10)
    
    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Move the paddles based on the keys pressed
    if keys[pygame.K_UP]:
        paddle2_speed = -5
    elif keys[pygame.K_DOWN]:
        paddle2_speed = 5
    else:
        paddle2_speed = 0
        
    if keys[pygame.K_w]:
        paddle1_speed = -5
    elif keys[pygame.K_s]:
        paddle1_speed = 5
    else:
        paddle1_speed = 0

# Exit pygame
pygame.quit()