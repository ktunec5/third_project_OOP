from gameparts import Board
from inspect import getsource


def main():
    game = Board()
    game.display()
    game.make_move(1, 0, 'X')
    print('Ход сделан!')
    game.display()
    print()
    print(getsource(Board))

if __name__ == '__main__':
    main()

