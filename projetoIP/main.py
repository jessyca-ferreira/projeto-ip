import pygame
from interface.nivel.layout import Nivel
from personagem.jogador import Jogador

# constantes
TELA_FUNDO = '#18041f'
TELA_LARGURA = 1200
TELA_ALTURA = 700

pygame.init()

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Projeto IP')

clock = pygame.time.Clock() # responsável pela quantidade de frames por segundo

jogador = Jogador()

rolagem = [0, 0]

nivel = Nivel(jogador.jogador_rect, rolagem)



# loop do jogo
executando = True
pause = False
while executando:
    for entrada in pygame.event.get():
        if entrada.type == pygame.QUIT:
            executando = False
            pygame.quit()
            exit()

        if entrada.type == pygame.KEYDOWN:
            if entrada.key == pygame.K_ESCAPE:
                if pause == True:
                    pause = False
                else:
                    pause = True

    if not pause:
        tela.fill(TELA_FUNDO) # inicia a tela
        rolagem[0] += (jogador.jogador_rect.x - rolagem[0] - 600)/5
        rolagem[1] += (jogador.jogador_rect.y - rolagem[1] - 40)/5

        camera = nivel.cam_rolagem()
        nivel.plataformas_nivel() # desenha as plataformas
        jogador.entrada_movimento()
        jogador_pos = camera[0]
        jogador.desenhar_jogador(jogador_pos)


    pygame.display.update()
    clock.tick(60)