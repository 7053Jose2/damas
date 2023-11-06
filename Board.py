# A Boardclasse define o comportamento de um tabuleiro de jogo de damas e como ele responde à entrada do usuário.
# Possui um __init__()método que inicializa a placa com os especificados tile_width, tile_height, e board_size.
# Ele também inicializa várias variáveis, como selected_piece,turne is_jump:
# /* Board.py
import pygame
from Tile import Tile
from Pawn import Pawn

class Board:
    def __init__(self,tile_width, tile_height, board_size):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.board_size = board_size
        self.selected_piece = None

        self.turn = "black"
        self.is_jump = False

        self.config = [
            ['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
            ['bp', '', 'bp', '', 'bp', '', 'bp', ''],
            ['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['rp', '', 'rp', '', 'rp', '', 'rp', ''],
            ['', 'rp', '', 'rp', '', 'rp', '', 'rp'],
            ['rp', '', 'rp', '', 'rp', '', 'rp', '']
        ]

        self.tile_list = self._generate_tiles()
        self._setup()

#Contém self.configa configuração inicial do tabuleiro para o nosso jogo.
#O tile_listchama o _generate_tiles()método que cria cada peça para o tabuleiro e o _setup()método define a
#posição inicial dos peões na base do jogo config.
    def _generate_tiles(self):
        output = []
        for y in range(self.board_size):
            for x in range(self.board_size):
                output.append(
                    Tile(x,  y, self.tile_width, self.tile_height)
                )
        return output

    def get_tile_from_pos(self, pos):
        for tile in self.tile_list:
            if (tile.x, tile.y) == (pos[0], pos[1]):
                return tile
#O _generate_tiles()método gera uma lista de peças usando a largura, a altura e o tamanho do tabuleiro especificados.
#O get_tile_from_pos()método retorna o objeto ladrilho em uma determinada posição.
    def _setup(self):
        for y_ind, row in enumerate(self.config):
            for x_ind, x in enumerate(row):
                tile = self.get_tile_from_pos((x_ind, y_ind))
                if x != '':
                    if x[-1] == 'p':
                        color = 'red' if x[0] == 'r' else 'black'
                        tile.occupying_piece = Pawn(x_ind, y_ind, color, self)
#O _setup() método define a configuração inicial do tabuleiro iterando pela self.configlista,
#que representa as posições iniciais das peças, e definindo o occupying_pieceatributo do objeto
#ladrilho correspondente para um Pawnobjeto.
    def handle_click(self, pos):
        x, y = pos[0], pos[-1]
        if x >= self.board_size or y >= self.board_size:
            x = x // self.tile_width
            y = y // self.tile_height
        clicked_tile = self.get_tile_from_pos((x, y))

        if self.selected_piece is None:
            if clicked_tile.occupying_piece is not None:
                if clicked_tile.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_tile.occupying_piece
        elif self.selected_piece._move(clicked_tile):
            if not self.is_jump:
                self.turn = 'red' if self.turn == 'black' else 'black'
            else:
                if len(clicked_tile.occupying_piece.valid_jumps()) == 0:
                    self.turn = 'red' if self.turn == 'black' else 'black'
        elif clicked_tile.occupying_piece is not None:
            if clicked_tile.occupying_piece.color == self.turn:
                self.selected_piece = clicked_tile.occupying_piece

#O handle_click()método toma como argumento uma posição ( pos), que representa as coordenadas em pixels do
#local no tabuleiro do jogo que foi clicado pelo jogador.
#Primeiro, o método extrai as coordenadas xe ydo posargumento. Se as coordenadas estiverem fora do tamanho do tabuleiro,
#o método calcula qual bloco foi
#clicado com base na posição do clique em relação ao tamanho de cada bloco. Em seguida, o método recupera o Tileobjeto que
#foi clicado chamando o get_tile_from_pos()método, passando as coordenadas ( x, y) do bloco clicado.

#Se não houver selected_pieceatualmente, o método verifica se a peça clicada contém um Pawnobjeto e se esse Pawnobjeto
#pertence ao turno do jogador atual. Se houver um Pawnobjeto na peça clicada e ele pertencer ao turno do jogador atual,
#o selected_pieceatributo do Boardobjeto será definido para esse Pawnobjeto.

#Se já existir selected_piece, o método tenta mover o Pawnobjeto para o bloco clicado chamando o _move()método do
#Pawnobjeto, passando o Tileobjeto como argumento. Se o movimento for bem sucedido, o turnatributo do Boardobjeto é
#atualizado para refletir a vez do próximo jogador.

#Se o movimento for um salto, o is_jumpatributo do Boardobjeto será definido como True. O método então verifica se há mais
#saltos válidos disponíveis para o mesmo Pawnobjeto, chamando o valid_jumps()método do Pawnobjeto. Se não houver mais saltos
#válidos, o turnatributo do Boardobjeto é atualizado para refletir a vez do próximo jogador.
#Se a peça clicada tiver um Pawnobjeto e pertencer ao turno do jogador atual, o selected_pieceatributo do Boardobjeto
#será definido para o Pawnobjeto na peça clicada.
    def draw(self, display):
        if self.selected_piece is not None:
            self.get_tile_from_pos(self.selected_piece.pos).highlight = True
            if not self.is_jump:
                for tile in self.selected_piece.valid_moves():
                    tile.highlight = True
            else:
                for tile in self.selected_piece.valid_jumps():
                    tile[0].highlight = True

        for tile in self.tile_list:
            tile.draw(display)
#O draw()método é usado para desenhar o tabuleiro e as peças. É chamado para atualizar a exibição com quaisquer
#alterações feitas pelo handle_click()método. Se uma peça for selecionada, a peça em que ela está e seus movimentos
#ou saltos válidos serão destacados.