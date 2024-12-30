from flask import Flask, render_template, jsonify
import chess
import chess.engine
import os

app = Flask(__name__)

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("C:/Users/avijn/Desktop/Projects/chess/stockfish/stockfish-windows-x86-64-avx2.exe")

def get_formatted_board():
    unicode_pieces = {
        'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
        'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
        '.': ' '
    }
    
    board_str = str(board)
    formatted_board = []
    ranks = '87654321'
    
    for idx, row in enumerate(board_str.split('\n')):
        formatted_row = f"{ranks[idx]} "
        for piece in row:
            formatted_row += unicode_pieces.get(piece, piece) + ' '
        formatted_board.append(formatted_row)
    
    formatted_board.append('  a b c d e f g h')
    return '\n'.join(formatted_board)

def get_board_state():
    squares = []
    for rank in range(8):
        for file in range(8):
            square = chess.square(file, 7-rank)
            piece = board.piece_at(square)
            squares.append({
                'square': chess.square_name(square),
                'piece': str(piece) if piece else None,
                'color': 'white' if piece and piece.color == chess.WHITE else 'black' if piece else None
            })
    return squares

@app.route('/')
def index():
    return render_template('chess.html', 
                         board=get_formatted_board(),
                         squares=get_board_state(), 
                         game_over=board.is_game_over(),
                         player_turn=board.turn == chess.WHITE,
                         chr=chr)  # Add this line to make chr available in template


@app.route('/move/<move>')
def make_move(move):
    if not board.is_game_over():
        try:
            # Player move
            board.push_san(move)
            
            # Computer move
            if not board.is_game_over():
                result = engine.play(board, chess.engine.Limit(time=0.1))
                board.push(result.move)
            
            return jsonify({
                'status': 'success',
                'board': get_formatted_board(),
                'squares': get_board_state(),
                'game_over': board.is_game_over(),
                'player_turn': board.turn == chess.WHITE,
                'last_move': move
            })
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    return jsonify({'status': 'error', 'message': 'Game is over'})

@app.route('/reset')
def reset_game():
    global board
    board = chess.Board()
    return jsonify({
        'status': 'success',
        'board': get_formatted_board(),
        'squares': get_board_state(),
        'game_over': False,
        'player_turn': True
    })

@app.route('/legal_moves')
def get_legal_moves():
    moves = [move.uci() for move in board.legal_moves]
    return jsonify({'moves': moves})

if __name__ == '__main__':
    app.run(debug=True)
