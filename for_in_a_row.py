import pygame


background_colour = (0, 255, 0)
width = 700
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('ЧЕТЫРЕ В РЯД')

screen.fill(background_colour)
x = width/14
y = height/12
while y < height:
    while x < width:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), (width/14 - 4))
        pygame.draw.circle(screen, (0, 0, 0), (x, y), (width / 14 - 2), 4)
        x += width/7
    x = width / 14
    y += height/6
pygame.display.update()



# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

