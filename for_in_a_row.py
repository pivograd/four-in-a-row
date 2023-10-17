from itertools import groupby

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

        y_poz_list = [11 * self.height / 12, 9 * self.height / 12, 7 * self.height / 12, 5 * self.height / 12, 3 * self.height / 12, self.height / 12]
        column_index = position[0] // 100
        row_index = len(self.playing_column[column_index])
        y_poz = y_poz_list[row_index]
        x_poz = column_index * 100 + self.width / 14

        player.list_of_moves.append((column_index, row_index))
        player.last_move = (column_index, row_index)


        pygame.draw.circle(self.screen, player.color, (x_poz, y_poz), (self.width / 14 - 4))
        self.playing_column[column_index].append('1')
        pygame.display.update()

class Player():

    def __init__(self, color):

        self.list_of_moves = []
        self.color = color
        self.last_move = (0, 0)


def has_consecutive_sequence(list):
    list.sort()
    count = 0
    for i in range(1, len(list)):
        if list[i] == list[i - 1] + 1:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

def group_and_check(player, key_func, extract_func):
    player.list_of_moves.sort(key=key_func)
    result = {}
    for key, group in groupby(player.list_of_moves, key=key_func):
        result[key] = list(group)

    for row in result.values():
        if len(row) >= 4:
            values = [extract_func(x) for x in row]
            if has_consecutive_sequence(values):
                return True

def is_the_game_over(player):
    if group_and_check(player, lambda x: x[1], lambda x: x[0]):
        return True
    if group_and_check(player, lambda x: x[0], lambda x: x[1]):
        return True
    if checking_the_victory_diagonally(player.last_move, player.list_of_moves):
        return True
    return False

def checking_the_victory_diagonally(move, moves):
    def check_adjacent_move(deltas_list):
        counter = 1
        for dx, dy in deltas_list:
            x, y = move
            for _ in range(3):
                x, y = x + dx, y + dy
                if (x, y) in moves:
                    counter += 1
                else:
                    break
        if counter >= 4:
            return True

    if check_adjacent_move(deltas_list=[(1, 1), (-1, -1)]):
        return True
    elif check_adjacent_move(deltas_list=[(1, -1), (-1, 1)]):
        return True


running = True


field = PlayingField()
field.to_create()

player_1 = Player(color= (255, 0, 0))
player_2 = Player(color= (0, 0, 255))

current_player = player_1
next_player = player_2

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            field.record_a_move(position = pygame.mouse.get_pos(), player = current_player)
            current_player, next_player = next_player, current_player

        if is_the_game_over(next_player):
            running = False

