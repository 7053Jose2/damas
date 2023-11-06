# A Tileclasse representa uma única peça no tabuleiro de jogo.
# /* Tile.py
import pygame

class Tile:
    def __init__(self, x, y, tile_width, tile_height):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.abs_x = x * tile_width
        self.abs_y = y * tile_height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 189, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.tile_width,
            self.tile_height
        )
        
# O __init__()método inicializa as propriedades do objeto, incluindo as coordenadas xe ydo bloco, seu widthe height,
# sua posição absoluta ( abs_xe abs_y) e tupla de posição ( abs_pos).

# A colorpropriedade é determinada pelo fato de a soma dos blocos xe ydas coordenadas ser par ou ímpar.
# Se for uniforme, o ladrilho é de cor clara, caso contrário, é escuro. As propriedades draw_colore highlight_colorsão
# tuplas que representam valores RGB para a cor de preenchimento e cor de destaque do bloco, respectivamente.

# A occupying_piecepropriedade é definida Nonepor padrão, mas pode receber um Pieceobjeto se houver uma peça ocupando
# o ladrilho.
# Teremos também os métodos get_coord()e draw():

    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)

        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
#O get_coord()método retorna uma string representando a coordenada da peça na notação padrão do xadrez, usando colunas
#com letras e linhas numeradas.

#O draw()método desenha o bloco na tela usando pygame.draw.rect, usando a draw_colorpropriedade como cor
#de preenchimento. Se a propriedade de destaque estiver definida como True, o bloco será desenhado com
#highlight_colorem vez disso. Se houver um occupying_piece, a imagem da peça será espalhada no centro do
#ladrilho usando pygame.Surface.blit(). A imagem é primeiro centralizada usando as propriedades get_rect()e
#center da imagem da peça.
