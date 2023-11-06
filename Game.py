#A Gameclasse contém métodos para verificar se o jogo acabou, verificar se há um salto disponível e exibir o vencedor do jogo:
# /* Game.py
class Game:
    def __init__(self):
        self.winner = None

#O __init__() método inicializa a winner variável para None.

    # checks if both colors still has a piece
    def check_piece(self, board):
        red_piece = 0
        black_piece = 0
        for y in range(board.board_size):
            for x in range(board.board_size):
                tile = board.get_tile_from_pos((x, y))
                if tile.occupying_piece != None:
                    if tile.occupying_piece.color == "red":
                        red_piece += 1
                    else:
                        black_piece += 1
        return red_piece, black_piece
#O check_piece()método itera sobre cada peça do tabuleiro e verifica se ela contém uma peça ocupante.
#Em caso afirmativo, adiciona à red_piececontagem se a cor da peça for "vermelha" ou à black_piececontagem se
#a cor da peça for "preta". Em seguida, ele retorna uma tupla contendo as contagens red_piecee black_piece.

    def is_game_over(self, board):
        red_piece, black_piece = self.check_piece(board)
        if red_piece == 0 or black_piece == 0:
            self.winner = "red" if red_piece > black_piece else "black"
            return True
        else:
            return False
#O is_game_over()método chama o check_piece()método para obter a contagem atual de peças para cada cor.
#Se uma cor não tiver mais peças, a outra cor é declarada vencedora e o método retorna True. Caso contrário,
#o método retorna False.
    def check_jump(self, board):
        piece = None
        for tile in board.tile_list:
            if tile.occupying_piece != None:
                piece = tile.occupying_piece
                if len(piece.valid_jumps()) != 0 and board.turn == piece.color:
                    board.is_jump = True
                    break
                else:
                    board.is_jump = False
        if board.is_jump:
            board.selected_piece = piece
            board.handle_click(piece.pos)
        return board.is_jump
    
#O check_jump()método verifica se existe alguma peça que consiga dar um salto.
#Se houver, ele define o is_jumpatributo do tabuleiro como True, define como selected_piecea
#primeira peça que pode saltar e retorna True. Se não houver, ele define o is_jumpatributo do
#tabuleiro como Falsee retorna False. Como estamos criando as Damas tradicionais onde os movimentos de
#salto não podem ser ignorados, isso check_jump()forçará os usuários a pular.
    
    def message(self):
        print(f"{self.winner} Wins!!")
        
