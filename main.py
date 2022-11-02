import chess
from game import Game
from chessEngine import ChessEngine

if __name__ == '__main__':
    game = Game(board=chess.Board('8/7k/8/R7/1R6/8/8/7K'), color=chess.BLACK, engineDepth=4, method="pvs")
    # game = Game(color=chess.BLACK, engineDepth=3, method="pvs")
    game.start()