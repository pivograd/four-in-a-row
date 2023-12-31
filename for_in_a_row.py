from itertools import groupby
from random import randint

import pygame


class PlayingField():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ЧЕТЫРЕ В РЯД')
        self.current_player = self.Player(color=(255, 0, 0))
        self.next_player = self.Player(color=(0, 0, 255))
        self.game_mod = 2

    class Player():

        def __init__(self, color):
            self.list_of_moves = []
            self.color = color
            self.last_move = (0, 0)

        def new_game(self):
            self.list_of_moves = []
            self.last_move = (0, 0)

        def __str__(self):
            return f"{self.color}"

    class ComputerPlayer(Player):

        def get_random_move(self):
            y = randint(0, 700)
            return (y, 100)

    def set_settings(self):

        self.stop_record = False
        self.width = 700
        self.height = 700
        self.colour = (137, 112, 74)
        self.screen = pygame.display.set_mode((self.width, self.height + 200))
        self.playing_column = [[], [], [], [], [], [], []]
        self.font = pygame.font.SysFont(name='Arial', size=110)
        self.font_2 = pygame.font.SysFont(name='Arial', size=55)

    def swap_players(self):

        self.current_player, self.next_player = self.next_player, self.current_player

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
        self.new_game_button()
        self.game_mod_buttons(self.game_mod)

    def new_game_button(self):

        button_rectangle = pygame.Rect(0, self.height, self.width, 100)
        pygame.draw.rect(self.screen, (0, 114, 0), button_rectangle)
        pygame.draw.line(surface=self.screen, color=(0, 0, 0), start_pos=(0, self.height),
                         end_pos=(self.width, self.height), width=3)
        text = self.font.render("Новая игра", True, (129, 255, 173))
        text_rect = text.get_rect(center=button_rectangle.center)
        self.screen.blit(text, text_rect)

    def game_mod_buttons(self, current_game_mod):

        if current_game_mod == 1:
            color_1 = (0, 104, 0)
            color_2 = (0, 156, 0)
        elif current_game_mod == 2:
            color_1 = (0, 156, 0)
            color_2 = (0, 104, 0)

        button_rectangle_1 = pygame.Rect(0, self.height + 100, self.width / 2, 100)
        button_rectangle_2 = pygame.Rect(self.width / 2, self.height + 100, self.width / 2, 100)
        pygame.draw.rect(self.screen, color_1, button_rectangle_1)
        pygame.draw.rect(self.screen, color_2, button_rectangle_2)
        pygame.draw.line(surface=self.screen, color=(0, 0, 0), start_pos=(0, self.height + 100),
                         end_pos=(self.width, self.height + 100), width=3)

        pygame.draw.line(surface=self.screen, color=(0, 0, 0), start_pos=(self.width / 2, self.height + 100),
                         end_pos=(self.width / 2, self.height + 200), width=3)
        text = self.font_2.render("Игра для 2", True, (129, 255, 173))
        text_rect = text.get_rect(center=button_rectangle_1.center)
        self.screen.blit(text, text_rect)
        text = self.font_2.render("Игра для 1", True, (129, 255, 173))
        text_rect = text.get_rect(center=button_rectangle_2.center)
        self.screen.blit(text, text_rect)

    def display_message(self, message, color):

        text_surface = self.font.render(message, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width // 2, self.height // 5)
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()

    def to_create(self):

        self.set_settings()
        self.draw_a_field()
        self.current_player.new_game()
        self.next_player.new_game()
        pygame.display.update()

    def record_a_move(self, player, position):

        y_poz_list = [11 * self.height / 12, 9 * self.height / 12, 7 * self.height / 12, 5 * self.height / 12,
                      3 * self.height / 12, self.height / 12]
        column_index = position[0] // 100
        row_index = len(self.playing_column[column_index])
        y_poz = y_poz_list[row_index]
        x_poz = column_index * 100 + self.width / 14

        player.list_of_moves.append((column_index, row_index))
        player.last_move = (column_index, row_index)

        pygame.draw.circle(self.screen, player.color, (x_poz, y_poz), (self.width / 14 - 4))
        self.playing_column[column_index].append('1')
        pygame.display.update()

    def game_vs_ai(self):

        self.game_mod = 1
        self.current_player = self.Player(color=(255, 0, 0))
        self.next_player = self.ComputerPlayer(color=(0, 0, 255))

    def two_people_game(self):

        self.game_mod = 2
        self.current_player = self.Player(color=(255, 0, 0))
        self.next_player = self.Player(color=(0, 0, 255))


    def has_consecutive_sequence(self, list):
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


    def group_and_check(self, player, key_func, extract_func):
        player.list_of_moves.sort(key=key_func)
        result = {}
        for key, group in groupby(player.list_of_moves, key=key_func):
            result[key] = list(group)

        for row in result.values():
            if len(row) >= 4:
                values = [extract_func(x) for x in row]
                if self.has_consecutive_sequence(values):
                    return True


    def is_the_game_over(self, player):
        if self.group_and_check(player, lambda x: x[1], lambda x: x[0]):
            return True
        if self.group_and_check(player, lambda x: x[0], lambda x: x[1]):
            return True
        if self.checking_the_victory_diagonally(player.last_move, player.list_of_moves):
            return True
        return False


    def checking_the_victory_diagonally(self, move, moves):
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



def main():

    running = True

    field = PlayingField()
    field.to_create()

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if field.height <= pos[1] <= field.height + 100:
                    field.to_create()

                elif field.height + 100 <= pos[1] <= field.height + 203:
                    if pos[0] >= field.width / 2:
                        if field.game_mod == 1:
                            pass
                        else:
                            field.game_vs_ai()
                            field.to_create()

                    elif pos[0] <= field.width / 2:
                        if field.game_mod == 2:
                            pass
                        else:
                            field.two_people_game()
                            field.to_create()
                else:
                    if not field.stop_record:
                        try:
                            field.record_a_move(position=pos, player=field.current_player)
                            if field.is_the_game_over(field.current_player):
                                field.stop_record = True
                                field.display_message(f'Победа', field.current_player.color)
                        except:
                            break

                    if not field.stop_record:

                        if field.game_mod == 2:
                            field.swap_players()
                        elif field.game_mod == 1:
                            not_move = True
                            while not_move:
                                pos = field.next_player.get_random_move()
                                try:
                                    field.record_a_move(position=pos, player=field.next_player)
                                    not_move = False
                                    if field.is_the_game_over(field.next_player):
                                        field.stop_record = True
                                        field.display_message(f'Победа', field.next_player.color)
                                except:
                                    pass

if __name__ == "__main__":
    main()