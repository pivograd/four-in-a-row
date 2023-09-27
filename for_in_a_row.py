import pygame


background_colour = (0, 255, 0)
width = 700
height = 600

playing_field = [[('0, 0'),('0, 1'),('0, 2'),('0, 3'),('0, 4'),('0, 5')],
                 [('1, 0'),('1, 1'),('1, 2'),('1, 3'),('1, 4'),('1, 5')],
                 [('2, 0'),('2, 1'),('2, 2'),('2, 3'),('2, 4'),('2, 5')],
                 [('3, 0'),('3, 1'),('3, 2'),('3, 3'),('3, 4'),('3, 5')],
                 [('4, 0'),('4, 1'),('4, 2'),('4, 3'),('4, 4'),('4, 5')],
                 [('5, 0'),('5, 1'),('5, 2'),('5, 3'),('5, 4'),('5, 5')]]


playing_column = [[],[],[],[],[],[],[]]



screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('ЧЕТЫРЕ В РЯД')

screen.fill(background_colour)
x = width/14
y = height/12
while y < height:
    while x < width:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), (width/14 - 4))
        pygame.draw.circle(screen, (0, 0, 0), (x, y), (width / 14 - 2), 4)
        pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(x + width/14 - 1, 0), end_pos=(x + width/14 - 1, height), width=2)
        x += width/7
    x = width / 14
    y += height/6

def make_move(position):
    y_poz_list = [11 * height / 12, 9 * height / 12, 7 * height / 12, 5 * height / 12, 3 * height / 12, height / 12]
    column_index = position[0]//100
    row_index = len(playing_column[column_index])
    y_poz = y_poz_list[row_index]
    x_poz = column_index*100 + width/14
    pygame.draw.circle(screen, (123, 23, 32), (x_poz,y_poz), (width/14 - 4))
    playing_column[column_index].append('1')
    pygame.display.update()

pygame.display.update()

running = True












while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            make_move(pygame.mouse.get_pos())
