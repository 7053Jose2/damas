# A Main é o ponto de partida do nosso jogo. Ele configura a janela do jogo,
#inicializa os objetos do jogo e executa o loop do jogo.
#Primeiro, importamos os módulos e classes necessários dos outros arquivos do nosso jogo de Damas.
#Então, inicializamos o Pygame com a pygame.init()função:
## /* Main.py
import pygame
from Board import Board
from Game import Game

pygame.init()

#A Checkersclasse possui um __init__()método que recebe um screenparâmetro que inicializa vários atributos da classe,
#incluindo screen, runninge FPS. screen representa a janela do jogo, runningé um booleano que determina se o
#jogo ainda está em execução e FPSé um relógio Pygame que limita o jogo a uma determinada taxa de quadros.


class Checkers:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()
        
#Abaixo da __init__()função, adicione mais duas funções e nomeie-as _draw()e main().
#O _draw()método é um método auxiliar que recebe um boardparâmetro e desenha o
#tabuleiro do jogo na tela usando o board.draw()método.
#Em seguida, ele atualiza a exibição usando pygame.display.update().
        
    def _draw(self, board):
        board.draw(self.screen)
        pygame.display.update()
        
#O main()método é o loop principal do jogo. Ele recebe parâmetros window_widthe window_height,
#que são as dimensões da janela do jogo. board_sizeé definido como 8, que representa o tamanho
#do tabuleiro de jogo. tile_widthe tile_heightsão calculados com base no tamanho da janela e no tamanho do quadro:
        
    def main(self, window_width, window_height):
        board_size = 8
        tile_width, tile_height = window_width // board_size, window_height // board_size
        board = Board(tile_width, tile_height, board_size)
        game = Game()
        while self.running:
            game.check_jump(board)

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False

                if not game.is_game_over(board):
                    if self.event.type == pygame.MOUSEBUTTONDOWN:
                        board.handle_click(self.event.pos)
                else:
                    game.message()
                    self.running = False

            self._draw(board)
            self.FPS.tick(60)
        
    def main(self, window_width, window_height):
        board_size = 8
        tile_width, tile_height = window_width // board_size, window_height // board_size
        board = Board(tile_width, tile_height, board_size)
        game = Game()
        while self.running:
            game.check_jump(board)

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False

                if not game.is_game_over(board):
                    if self.event.type == pygame.MOUSEBUTTONDOWN:
                        board.handle_click(self.event.pos)
                else:
                    game.message()
                    self.running = False

            self._draw(board)
            self.FPS.tick(60)
#board é então inicializado com a Boardclasse, passando os parâmetros tile_width, tile_heighte board_size.
#gametambém é inicializado com a Gameclasse.
#O whileloop é executado enquanto self.runningfor True. Dentro do loop, chamamos game.check_jump(board)para
#verificar se há saltos disponíveis no tabuleiro. Em seguida, percorremos os eventos na fila de eventos do Pygame
#usando pygame.event.get().
#Se o tipo de evento for pygame.QUIT(quando o botão sair foi clicado), configuramos self.runningpara Falsesair do jogo.
#Abaixo da classe, vamos chamar o jogo com a main()função.
if __name__ == "__main__":
    window_size = (640, 640)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Checkers")

    checkers = Checkers(screen)
    checkers.main(window_size[0], window_size[1])
    
#Definimos window_sizecomo (640, 640), criamos uma tela de exibição do Pygame com esse tamanho usando pygame.display.
#set_mode(window_size)e definimos a legenda da janela como "Damas" usando pygame.display.set_caption("Checkers").
#Em seguida, criamos uma instância da Checkersclasse chamada checkers, passando o screencomo parâmetro.
#Então, chamamos o main()método on checkers, passando as window_sizedimensões. Este código configura a tela do Pygame,
#cria uma instância da Checkersclasse e inicia o loop do jogo chamando o main()método.
#Se o jogo não terminar, verificamos se o usuário clicou em uma peça do tabuleiro usando board.handle_click().
#Se o jogo terminar, exibimos uma mensagem usando game.message()e saímos do loop do jogo configurando self.runningcomo False.
    

#Em seguida, chamamos o _draw()método para desenhar o tabuleiro do jogo na tela e atualizar a exibição usando
#pygame.display.update(). Por fim, limitamos self.FPS.tick(60)o jogo a 60 frames por segundo.
 