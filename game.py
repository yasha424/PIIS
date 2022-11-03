import chess.engine
from chessEngine import ChessEngine


class Game:
    def __init__(self, board=chess.Board(), color=chess.WHITE, engineDepth=1, method="negamax"):

        self.__board = board
        self.__playerColor = color
        self.__engine = ChessEngine(method=method, color=not color)
        self.__engineDepth = engineDepth
        self.__method = method

    def makeMove(self, move):

        self.__board.push(move)

    def makeAiMove(self):

        move = self.__engine.getBestMove(self.__board, depth=self.__engineDepth)
        self.makeMove(move)


    def start(self):

        while not self.__board.is_game_over():
            print(self.__board, "\n")
            if self.__board.turn == self.__playerColor:
                i = 1
                legalMoves = self.__board.legal_moves
                print("Choose your move:")
                for move in legalMoves:
                    print("\t" + str(i) + ") " + move.__str__())
                    i += 1

                self.makeMove(list(legalMoves)[int(input("Enter your move index: ")) - 1])

            elif self.__board.turn != self.__playerColor:
                self.makeAiMove()
                print("\tAi move:", "\n")

        print(self.__board)
        return