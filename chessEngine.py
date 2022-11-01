import chess
import chess.engine


class ChessEngine:
    def __init__(self, method="negamax", color=chess.BLACK):

        self.color = color
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

        if method == 'negamax':
            self.getBestMove = self.negaMax

    def evaluate(self, board, depthLimit=1):

        result = self.engine.analyse(board, chess.engine.Limit(depth=depthLimit))

        if self.color:
            return result["score"].white()

        return result["score"].black()

    def negaMax(self, board, depth=1):

        bestScore = chess.engine.Cp(-999999)
        bestMove = chess.Move.null()
        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)
            score = -self.minimax(depth - 1, newBoard)
            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove

    def minimax(self, depth, board):

        if depth == 0:
            return -self.evaluate(board)

        bestScore = chess.engine.Cp(-999999)
        bestMove = chess.Move.null()
        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)
            score = -self.minimax(depth - 1, newBoard)
            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestScore
