#import pygame
from comandos import *
from menu import Menu
from inimigo import Inimigo

def rodar_jogo():
    # Configurações da janela
    largura_janela, altura_janela = 878, 494
    janela = pygame.display.set_mode([largura_janela, altura_janela])
    pygame.display.set_caption('Doupo Xiao')

    # Carrega as imagens
    try:
        imagem_fundo = pygame.image.load('asset/imagens/fundo maior.png').convert()
        spritesheet_parado = pygame.image.load('asset/imagens/Parado.png').convert_alpha()
        spritesheet_atirando = pygame.image.load('asset/imagens/Atirando.png').convert_alpha()
        spritesheet_agachado = pygame.image.load('asset/imagens/agachado.png').convert_alpha()
        spritesheet_pulando = pygame.image.load('asset/imagens/Hurt.png').convert_alpha()
        spritesheet_correndo = pygame.image.load('asset/imagens/Run.png').convert_alpha()
    except Exception as e:
        print(f"Erro ao carregar imagens: {e}")
        pygame.quit()
        exit()

    # Recorta frames do soldado
    frames_parado = recortar_frames(spritesheet_parado, 1, 115, 128)
    frames_atirando = recortar_frames(spritesheet_atirando, 4, 128, 128)
    frames_agachado = recortar_frames(spritesheet_agachado, 4, 128, 128)
    frames_pulando = recortar_frames(spritesheet_pulando, 3, 128, 128)
    frames_correndo = recortar_frames(spritesheet_correndo, 8, 128, 128)

    # Variáveis do soldado
    estado_atual = ESTADO_PARADO
    frame_atual = 0
    contador_animacao = 0
    velocidade_animacao = 10
    pos_x_player = 0
    pos_y_player = altura_janela - 128
    vel_soldier_player = 4

    # Cria o inimigo (canto inferior direito)
    inimigo = Inimigo(largura_janela - 150, altura_janela - 128)

    clock = pygame.time.Clock()
    running = True

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "menu"

        # Atualizações
        teclas = pygame.key.get_pressed()
        pos_x_player, pos_y_player, estado_atual = atualizar_soldado(
            teclas, pos_x_player, pos_y_player, estado_atual,
            vel_soldier_player, largura_janela, altura_janela, 128, 128
        )
        
        inimigo.atualizar()

        # Desenho
        janela.blit(imagem_fundo, (0, 0))
        inimigo.desenhar(janela)

        # Desenha o soldado
        if estado_atual == ESTADO_PARADO:
            janela.blit(frames_parado[0], (pos_x_player, pos_y_player))
        elif estado_atual == ESTADO_ATIRANDO:
            janela.blit(frames_atirando[frame_atual], (pos_x_player, pos_y_player))
        elif estado_atual == ESTADO_AGACHADO:
            janela.blit(frames_agachado[frame_atual], (pos_x_player, pos_y_player))
        elif estado_atual == ESTADO_PULANDO:
            janela.blit(frames_pulando[frame_atual], (pos_x_player, pos_y_player))
        elif estado_atual == ESTADO_CORRENDO:
            janela.blit(frames_correndo[frame_atual], (pos_x_player, pos_y_player))

        pygame.display.flip()
        clock.tick(60)

    return "sair"

def main():
    pygame.init()
    while True:
        menu = Menu()
        acao = menu.executar()
        if acao == "iniciar":
            resultado = rodar_jogo()
            if resultado == "sair":
                break
        elif acao == "sair":
            break
    pygame.quit()

if __name__ == "__main__":
    main()