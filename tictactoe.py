# tictactoe.py

class TicTacToe:
    def __init__(self):
        self.board = ['_' for _ in range(9)]
        self.p1_turn = True
        self.finished = False
        self.winner = None
    def __str__(self):
        b = self.board
        return f'{b[0]}{b[1]}{b[2]}\n{b[3]}{b[4]}{b[5]}\n{b[6]}{b[7]}{b[8]}'
    def __repr__(self):
        return self.__str__()

    def restart(self):
        self.__init__()
        self.run()

    def run(self):
        while not self.finished:
            print(game)
            cur_player = 'Player 1' if self.p1_turn else 'Player 2'
            try:
                play_idx = int(input(f"{cur_player}'s turn to play: "))
                self.play_at(play_idx)
            except (ValueError, IndexError) as e:
                print('Invalid input, please input an integer between 0 and 8 at an empty cell.')

        if self.winner != 'Draw':
            print(f'Game Over, winner is: {self.winner}')
        else:
            print("Game Over, it's a draw!")
        print(game)

    def play_at(self, idx: int):
        if idx not in range(9) or self.board[idx] != '_':
            raise IndexError('Index was not in range or cell is not empty.')
        symbol = 'O'
        if self.p1_turn:
            symbol = 'X'
        self.p1_turn = not self.p1_turn
        self.board[idx] = symbol
        self.check_game_state()

    def check_game_state(self):
        b = self.board
        winning_lines = {b[0+idx] + b[3+idx] + b[6+idx] for idx in range(3)}  # columns
        winning_lines |=  set([''.join(b[:3]), ''.join(b[3:6]), ''.join(b[6:9])]) # rows
        winning_lines |=  set([b[0]+b[4]+b[8], b[2]+b[4]+b[6]]) # diagonals
        if 'XXX' in winning_lines:
            self.finished = True
            self.winner = 'Player 1'
        elif 'OOO' in winning_lines:
            self.finished = True
            self.winner = 'Player 2'
        elif not '_' in b:
            self.finished = True
            self.winner = 'Draw'

if __name__ == '__main__':
    game = TicTacToe()
    game.run()
