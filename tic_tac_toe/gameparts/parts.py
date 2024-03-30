class Board:

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Обьект игрового поля размером '
            f'{self.field_size}X{self.field_size}'
        )
