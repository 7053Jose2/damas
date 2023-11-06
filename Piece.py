#A Piececlasse é uma classe pai para todas as peças de xadrez do jogo. Ele contém atributos e métodos comuns que
#são compartilhados entre todas as peças, como o positionda peça no tabuleiro, seu color, e a capacidade de mover
#para determinadas peças no tabuleiro com base nas regras do jogo.
# /* Piece.py
import pygame

class Piece:
    def __init__(self, x, y, color, board):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.board = board
        self.color = color
#Especificamente para as classes Pawne King, eles substituem alguns dos métodos da Piececlasse para dar conta das
#regras específicas que se aplicam a essas peças no jogo de damas. Por exemplo, o valid_moves()método da Pawnclasse
#retorna os movimentos válidos que um peão pode fazer no tabuleiro com base nas regras do jogo para um peão (pode se
#mover ou pular para frente/contra apenas o lado inicial). Da mesma forma, o valid_moves()método da Kingclasse retorna
#os movimentos válidos que um rei pode fazer no tabuleiro com base nas regras do jogo para um rei (pode mover-se ou pular
#para frente ou para trás).

#Além disso, a Pawnclasse inclui uma implementação específica para promoção de peões, que ocorre quando um peão chega
#ao extremo oposto do tabuleiro. A Kingclasse não requer uma implementação específica para promoção, pois os reis já
#são as peças de maior classificação no jogo.

#Aqui na Pieceaula também definimos o move()método para ambas as peças.
    def _move(self, tile):
        for i in self.board.tile_list:
            i.highlight = False
        # ordinary move/s
        if tile in self.valid_moves() and not self.board.is_jump:
            prev_tile = self.board.get_tile_from_pos(self.pos)
            self.pos, self.x, self.y = tile.pos, tile.x, tile.y
            prev_tile.occupying_piece = None
            tile.occupying_piece = self
            self.board.selected_piece = None
            self.has_moved = True
            # Pawn promotion
            if self.notation == 'p':
                if self.y == 0 or self.y == 7:
                    from King import King
                    tile.occupying_piece = King(
                        self.x, self.y, self.color, self.board
                    )
            return True
        # jump move/s
        elif self.board.is_jump:
            for move in self.valid_jumps():
                if tile in move:
                    prev_tile = self.board.get_tile_from_pos(self.pos)
                    jumped_piece = move[-1]
                    self.pos, self.x, self.y = tile.pos, tile.x, tile.y
                    prev_tile.occupying_piece = None
                    jumped_piece.occupying_piece = None
                    tile.occupying_piece = self
                    self.board.selected_piece = None
                    self.has_moved = True
                    # Pawn promotion
                    if self.notation == 'p':
                        if self.y == 0 or self.y == 7:
                            from King import King
                            tile.occupying_piece = King(
                                self.x, self.y, self.color, self.board
                            )
                    return True
        else:
            self.board.selected_piece = None
            return False
#O _move()método recebe um tileobjeto que representa a nova posição da peça. Primeiro verifica se a nova posição é
#um movimento válido para a peça chamando o valid_moves()método. Se o movimento for válido e nenhum salto estiver
#ocorrendo, o método atualiza a posição da peça e o occupying_pieceatributo das peças relevantes para refletir a nova
#posição da peça. Se a peça for um peão e chegar à última linha, será promovida a rei.
#Se um salto estiver ocorrendo, o _move()método verifica se a nova posição é um movimento de salto válido chamando o
#valid_jumps()método. Se o movimento for válido, o método atualiza a posição da peça, o occupying_pieceatributo das peças
#relevantes, e remove a jumped_piece(peça do oponente que causou o salto). O método verifica se o peão atingiu a última linha
#e o promove a rei, se necessário.
#Se a movimentação não for válida, o método simplesmente retorna False.