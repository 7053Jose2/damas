#A Kingclasse é muito semelhante à Pawnclasse em termos de estrutura e métodos. Contudo, o _possible_moves()método agora
#retorna todas as direções diagonais, já que um rei pode se mover diagonalmente em qualquer direção.
#O valid_moves()método retorna uma lista de peças para as quais o rei pode se mover, que são peças
#vazias e dentro dos limites do tabuleiro. O valid_jumps()método retorna uma lista de tuplas, onde cada
#tupla contém duas peças, representando um salto que o rei pode dar sobre uma peça adversária.
#A implementação de valid_jumps()é muito semelhante à da Pawnclasse, com a única diferença de que Kingpode
#saltar sobre peças opostas em qualquer direção diagonal:
# /* King.py
#import pygame
#from Piece import Piece

#class King(Piece):
    #def __init__(self, x, y, color, board):
        #super().__init__(x, y, color, board)
        #img_path = f'images/{color}-king.png'
        #self.img = pygame.image.load(img_path)
        #self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        #self.notation = 'k'

    #def _possible_moves(self):
        #possible_moves = ((-1, -1), (+1, -1), (-1, +1), (+1, +1))
        #return possible_moves

    #def valid_moves(self):
        #tile_moves = []
        #moves = self._possible_moves()
        #for move in moves:
            #tile_pos = (self.x + move[0], self.y + move[-1])
            #if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
                #pass
            #else:
                #tile = self.board.get_tile_from_pos(tile_pos)
                #if tile.occupying_piece == None:
                   #tile_moves.append(tile)
        #return tile_moves

    #def valid_jumps(self):
        #tile_jumps = []
        #moves = self._possible_moves()
        #for move in moves:
            #tile_pos = (self.x + move[0], self.y + move[-1])
            #if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
                #pass
            #else:
                #tile = self.board.get_tile_from_pos(tile_pos)
                #if self.board.turn == self.color:
                    #if tile.occupying_piece != None and tile.occupying_piece.color != self.color:
                        #next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[-1])
                        #next_tile = self.board.get_tile_from_pos(next_pos)		
                        #if next_pos[0] < 0 or next_pos[0] > 7 or next_pos[-1] < 0 or next_pos[-1] > 7:
                            #pass
                        #else:
                            #if next_tile.occupying_piece == None:
                                #tile_jumps.append((next_tile, tile))
        #return tile_jumps
import pygame
from Piece import Piece

class King(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, board)
        img_path = f'images/{color}-king.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'k'

    def _possible_moves(self):
        possible_moves = ((-1, -1), (+1, -1), (-1, +1), (+1, +1))
        return possible_moves

    def valid_moves(self):
        tile_moves = []
        moves = self._possible_moves()
        for move in moves:
            for i in range(1, 8):  # Permite movimentos em todas as direções por no máximo 7 espaços
                tile_pos = (self.x + move[0] * i, self.y + move[1] * i)
                if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[1] < 0 or tile_pos[1] > 7:
                    break  # Sai do loop se estiver fora do tabuleiro
                tile = self.board.get_tile_from_pos(tile_pos)
                if tile.occupying_piece is not None:
                    break  # Sai do loop se encontrar uma peça no caminho
                tile_moves.append(tile)
        return tile_moves

    def valid_jumps(self):
        tile_jumps = []
        moves = self._possible_moves()
        for move in moves:
            for i in range(1, 8):  # Permite saltos em todas as direções por no máximo 7 espaços
                tile_pos = (self.x + move[0] * i, self.y + move[1] * i)
                if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[1] < 0 or tile_pos[1] > 7:
                    break  # Sai do loop se estiver fora do tabuleiro
                tile = self.board.get_tile_from_pos(tile_pos)
                if tile.occupying_piece is not None and tile.occupying_piece.color != self.color:
                    next_pos = (self.x + move[0] * (i + 1), self.y + move[1] * (i + 1))
                    if next_pos[0] < 0 or next_pos[0] > 7 or next_pos[1] < 0 or next_pos[1] > 7:
                        break  # Sai do loop se estiver fora do tabuleiro
                    next_tile = self.board.get_tile_from_pos(next_pos)
                    if next_tile.occupying_piece is None:
                        tile_jumps.append((next_tile, tile))
                else:
                    break  # Sai do loop se encontrar uma peça do mesmo jogador
        return tile_jumps
