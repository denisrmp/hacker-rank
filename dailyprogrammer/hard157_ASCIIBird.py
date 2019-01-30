# python 2 script

import numpy as np
import random, math


class AsciiBird:

    def __init__(self):
        self.nrow = 10
        self.ncol = 20
        self.next_ceil_pipe = 0
        self.next_floor_pipe = 0
        self.board = np.vstack([np.array([['.'] * self.nrow]) for _ in xrange(self.ncol)]).transpose()
        self.board[4, 1] = '@'
        self.bird_pos = 4
        self.score = 0
        self.game_over = False

    def __str__(self):
        return "\n".join(["".join(self.board[x]) for x in xrange(0, 10)])

    def game_step(self, option):
        if option == 0:
            option = -2
        self.update_board(int(math.ceil(option / 2.0)))
        self.update_board(int(math.floor(option / 2.0)))

    def update_board(self, option):
        self.board = np.column_stack([self.board, self.draw_column()])
        self.board = np.delete(self.board, 0, 1)
        self.board[self.bird_pos, 0] = '.'
        self.bird_pos = self.bird_pos - option
        if self.bird_pos < 0:
            self.bird_pos = 0

        if self.check_colision():
            self.game_over = True
        else:
            self.board[self.bird_pos, 1] = '@'
            if np.where(ab.board[:, 1] == '#')[0].shape[0] > 0:
                self.score = self.score + 1

    def check_colision(self):
        if self.bird_pos >= 10 or self.board[self.bird_pos, 1] == '#':
            return True
        else:
            return False

    def draw_column(self):
        pipe_size = 0
        if self.next_ceil_pipe == 0:
            self.next_ceil_pipe = random.randint(7, 10)
            pipe_size = random.randint(2, 4)
        else:
            self.next_ceil_pipe = self.next_ceil_pipe - 1
        pipe = ['#'] * pipe_size + ['.'] * ((self.nrow / 2) - pipe_size)

        pipe_size = 0
        if self.next_floor_pipe == 0:
            self.next_floor_pipe = random.randint(7, 10)
            pipe_size = random.randint(2, 4)
        else:
            self.next_floor_pipe = self.next_floor_pipe - 1
        return np.array(pipe + ['.'] * ((self.nrow / 2) - pipe_size) + ['#'] * pipe_size)


# game loop
ab = AsciiBird()
print(ab)
print("\n(score %s) 0-4?" % ab.score)

while not ab.game_over:
    option = int(raw_input())
    ab.game_step(option)
    print(ab)
    print("\n(score %s) 0-4?" % ab.score)

print("\nGame Over.")
print("Final Score: %s" % ab.score)
