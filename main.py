# import chess
# from chessEngine import ChessEngine
import chess

from game import Game

if __name__ == '__main__':
    # engine = ChessEngine(chess.Board('8/7k/8/R7/1R6/8/8/7K'), depth=4)
    # engine = ChessEngine(depth=3)
    # print(engine.evaluate(engine.board))
    # print(engine.board.legal_moves.count())
    # print(engine.getBestMove())
    # print(engine.board)
    # while not engine.board.is_stalemate():
    #     engine.board.push(engine.getBestMove()[1])
    #     print(engine.board)
    #     print('')
    game = Game(color=chess.WHITE, engineDepth=3)
    game.start()
