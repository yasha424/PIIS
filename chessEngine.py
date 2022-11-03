import chess
import chess.engine
from util import Util

class ChessEngine:
    def __init__(self, method="negamax", color=chess.BLACK):

        self.color = color
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

        if method == "negamax":
            self.getBestMove = self.negaMax
        elif method == "negascout":
            self.getBestMove = self.negaScout
        elif method == "pvs":
            self.getBestMove = self.pvs

    def evaluate(self, board, depthLimit=1):

        # result = self.engine.analyse(board, chess.engine.Limit(depth=depthLimit))
        #
        # if self.color:
        #     return result["score"].white()
        #
        # return result["score"].black()

        if board.is_checkmate():
            if self.color == board.turn:
                return chess.engine.Mate(-1)

            return chess.engine.Mate(1)

        score = 0
        for i in range(64):
            piece = board.piece_type_at(chess.SQUARES[i])
            color = board.color_at(chess.SQUARES[i])

            if piece is not None and piece is not chess.KING:
                score += Util.pieces[piece] * Util.colors[color]

        if self.color:
            return chess.engine.Cp(score)

        return chess.engine.Cp(-score)

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

        if depth == 0 or board.is_game_over():
            return -self.evaluate(board)

        bestScore = chess.engine.Cp(-999999)
        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)
            score = -self.minimax(depth - 1, newBoard)
            if score > bestScore:
                bestScore = score

        return bestScore


    def negaScout(self, board, depth=1):

        bestMove = chess.Move.null()
        bestScore = chess.engine.Cp(-999999)
        alpha = chess.engine.Cp(-999999)
        beta = chess.engine.Cp(999999)

        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)
            score = -self.negaScoutUtil(newBoard, alpha, beta, depth - 1)

            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove
    def negaScoutUtil(self, board, alpha, beta, depth):

        if depth == 0 or board.is_game_over():
            return -self.evaluate(board)

        a = alpha
        b = beta
        i = 0
        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)
            score = -self.negaScoutUtil(newBoard, -b, -a, depth - 1)

            if score > a and score < beta and depth > 0 and i > 0:
                a = -self.negaScoutUtil(newBoard, -beta, -score, depth - 1)
            if score > a:
                a = score

            if a >= beta:
                return a

            b = chess.engine.Cp(a.score(mate_score=100000) + 1)
            i += 1
        return a

    def pvs(self, board, depth=1):

        bestMove = chess.Move.null()
        bestScore = chess.engine.Cp(-999999)
        alpha = chess.engine.Cp(-999999)
        beta = chess.engine.Cp(999999)

        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)

            score = -self.pvsUtil(newBoard, alpha, beta, depth - 1)

            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove

    def pvsUtil(self, board, alpha, beta, depth):

        if depth == 0:
            return -self.evaluate(board)

        bSearchPv = True

        for move in board.legal_moves:
            newBoard = board.copy()
            newBoard.push(move)

            if bSearchPv:
                score = -self.pvsUtil(newBoard, -beta, -alpha, depth - 1)
            else:
                newAlpha = chess.engine.Cp(-alpha.score(mate_score=100000) - 1)
                score = -self.pvsUtil(newBoard, newAlpha, alpha, depth - 1)

                if score > alpha and score < beta:
                    score = -self.pvsUtil(newBoard, -beta, -alpha, depth - 1)

            if score >= beta:
                return beta

            if score > alpha:
                alpha = score
                bSearchPv = False

        return alpha