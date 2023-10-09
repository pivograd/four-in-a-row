import pygame

class PlayingField():

    def __init__(self):
        pass

    def set_settings(self):

        self.width = 700
        self.height = 700
        self.colour = (0, 255, 0)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.playing_column = [[],[],[],[],[],[],[]]
        pygame.display.set_caption('ЧЕТЫРЕ В РЯД')

    def draw_a_field(self):

        self.screen.fill(self.colour)
        x = self.width / 14
        y = self.height / 12
        while y < self.height:
            while x < self.width:
                pygame.draw.circle(self.screen, (255, 255, 255), (x, y), (self.width / 14 - 4))
                pygame.draw.circle(self.screen, (0, 0, 0), (x, y), (self.width / 14 - 2), 4)
                pygame.draw.line(surface=self.screen, color=(0, 0, 0), start_pos=(x + self.width / 14 - 1, 0),
                                 end_pos=(x + self.width / 14 - 1, self.height), width=2)
                x += self.width / 7
            x = self.width / 14
            y += self.height / 6

    def to_create(self):

        self.set_settings()
        self.draw_a_field()
        pygame.display.update()

    def record_a_move(self, player, position):

        if player == 1:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        y_poz_list = [11 * self.height / 12, 9 * self.height / 12, 7 * self.height / 12, 5 * self.height / 12, 3 * self.height / 12, self.height / 12]
        column_index = position[0] // 100
        row_index = len(self.playing_column[column_index])
        y_poz = y_poz_list[row_index]
        x_poz = column_index * 100 + self.width / 14
        pygame.draw.circle(self.screen, color, (x_poz, y_poz), (self.width / 14 - 4))
        self.playing_column[column_index].append('1')
        pygame.display.update()

running = True

current_player = 1
next_player = 0

field = PlayingField()
field.to_create()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            field.record_a_move(position = pygame.mouse.get_pos(), player = current_player)
            current_player, next_player = next_player, current_player
