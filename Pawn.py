#A Pawnclasse é uma subclasse da Piececlasse, os peões são as peças utilizadas desde o início do jogo.
#A classe possui um __init__()método que chama o método pai __init__()para inicializar o objeto xe ya posição,
#colore board. Ele também carrega uma imagem para o peão e atribui a ele
#a notação 'p':
# /* Pawn.py
import pygame
from Piece import Piece

class Pawn(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, board)
        img_path = f'images/{color}-pawn.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'p'
#Vamos adicionar mais três métodos; o _possible_moves(), o valid_moves()e os valid_jumps()métodos
    def _possible_moves(self):
        # (x, y) move for left and right
        if self.color == "red":
            possible_moves = ((-1, -1), (+1, -1)) 
        else:
            possible_moves = ((-1, +1), (+1, +1))
        return possible_moves
#O _possible_moves()método retorna uma tupla de movimentos possíveis que um peão pode fazer na forma de (x, y)coordenadas
#para as direções esquerda e direita. Os movimentos possíveis dependem da cor do peão. Por exemplo, um peão vermelho pode
#mover-se para a esquerda e para a direita nas direções (-1, -1) e (+1, -1), respectivamente.
    def valid_moves(self):
        tile_moves = []
        moves = self._possible_moves()
        for move in moves:
            tile_pos = (self.x + move[0], self.y + move[-1])
            if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
                pass
            else:
                tile = self.board.get_tile_from_pos(tile_pos)
                if tile.occupying_piece == None:
                    tile_moves.append(tile)
        return tile_moves
#O valid_moves()método verifica todos os movimentos possíveis de um peão no tabuleiro e retorna uma lista de movimentos
#válidos. Isso é feito iterando os movimentos possíveis e verificando se cada movimento resulta em uma posição válida de
#peça no tabuleiro que não contém nenhuma peça ocupante. Se a posição do bloco for válida e vazia, ele anexa o objeto do
#bloco à lista de movimentos válidos.
    def valid_jumps(self):
        tile_jumps = []
        moves = self._possible_moves()
        for move in moves:
            tile_pos = (self.x + move[0], self.y + move[-1])
            if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
                pass
            else:
                tile = self.board.get_tile_from_pos(tile_pos)
                if self.board.turn == self.color:
                    if tile.occupying_piece != None and tile.occupying_piece.color != self.color:
                        next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[-1])
                        next_tile = self.board.get_tile_from_pos(next_pos)		
                        if next_pos[0] < 0 or next_pos[0] > 7 or next_pos[-1] < 0 or next_pos[-1] > 7:
                            pass
                        else:
                            if next_tile.occupying_piece == None:
                                tile_jumps.append((next_tile, tile))
        return tile_jumps
#O valid_jumps()método retorna uma lista de tuplas que representa um movimento de salto válido para o peão.
#Ele verifica saltos de maneira semelhante, valid_moves()mas também verifica a posição de uma peça com uma peça adversária.
#Se tal posição de bloco existir, ele verifica a próxima posição na direção do salto para garantir que esteja vazia.
#Se a próxima posição estiver vazia, ele acrescenta uma tupla contendo a peça atual e a peça que contém a peça do
#oponente à lista de saltos válidos.
    
