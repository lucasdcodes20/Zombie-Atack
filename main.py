import pygame
from comandos import *  # Importa tudo do arquivo Comandos.py

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura_janela, altura_janela = 878, 494
janela = pygame.display.set_mode([largura_janela, altura_janela])
pygame.display.set_caption('Doupo Xiao')

# Carrega as imagens
try:
    imagem_fundo = pygame.image.load('asset/imagens/fundo maior.png')
    # Spritesheets para cada animação
    spritesheet_parado = pygame.image.load('asset/imagens/Parado.png').convert_alpha()
    spritesheet_atirando = pygame.image.load('asset/imagens/Atirando.png').convert_alpha()
    spritesheet_agachado = pygame.image.load('asset/imagens/agachado.png').convert_alpha()
    spritesheet_pulando = pygame.image.load('asset/imagens/Hurt.png').convert_alpha()
    spritesheet_correndo = pygame.image.load('asset/imagens/Run.png').convert_alpha()
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")
    pygame.quit()
    exit()

# Tamanho de cada frame nos spritesheets
largura_frame_parado = 115  # Tamanho do frame parado
altura_frame_parado = 128
largura_frame_outros = 128  # Tamanho dos frames das outras animações
altura_frame_outros = 128

# Número de frames de cada animação (ajuste conforme necessário)
NUM_FRAMES_PARADO = 1    # Parado tem 1 frame
NUM_FRAMES_ATIRANDO = 4  # Atirando tem 4 frames
NUM_FRAMES_AGACHADO = 4  # Agachado tem 2 frames
NUM_FRAMES_PULANDO = 3   # Pulando tem 4 frames
NUM_FRAMES_CORRENDO = 8  # Correndo tem 4 frames

# Recorta os frames de cada animação
frames_parado = recortar_frames(spritesheet_parado, NUM_FRAMES_PARADO, largura_frame_parado, altura_frame_parado)
frames_atirando = recortar_frames(spritesheet_atirando, NUM_FRAMES_ATIRANDO, largura_frame_outros, altura_frame_outros)
frames_agachado = recortar_frames(spritesheet_agachado, NUM_FRAMES_AGACHADO, largura_frame_outros, altura_frame_outros)
frames_pulando = recortar_frames(spritesheet_pulando, NUM_FRAMES_PULANDO, largura_frame_outros, altura_frame_outros)
frames_correndo = recortar_frames(spritesheet_correndo, NUM_FRAMES_CORRENDO, largura_frame_outros, altura_frame_outros)

# Variáveis de animação
estado_atual = ESTADO_PARADO  # Estado inicial
frame_atual = 0  # Frame atual da animação
contador_animacao = 0  # Contador para controlar a velocidade da animação
velocidade_animacao = 10  # Velocidade da animação (quanto maior, mais lenta)

# Posição inicial do soldier (canto inferior esquerdo)
pos_x_player = 0  # Colado na borda esquerda
pos_y_player = altura_janela - altura_frame_parado  # Colado na base
vel_soldier_player = 4

loop = True

# Loop principal do jogo
while loop:
    # Verifica eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            loop = False

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Atualiza a posição e o estado do soldado
    pos_x_player, pos_y_player, estado_atual = atualizar_soldado(
        teclas, pos_x_player, pos_y_player, estado_atual, vel_soldier_player,
        largura_janela, altura_janela, largura_frame_parado, altura_frame_parado
    )

    # Atualiza a animação do soldado
    frame_atual, contador_animacao = atualizar_animacao(
        estado_atual, frame_atual, contador_animacao, velocidade_animacao,
        frames_parado, frames_atirando, frames_agachado, frames_pulando, frames_correndo
    )

    # Desenha o fundo (limpa a tela)
    janela.blit(imagem_fundo, (0, 0))

    # Desenha o soldier na tela com a animação correspondente
    if estado_atual == ESTADO_PARADO:
        janela.blit(frames_parado[0], (pos_x_player, pos_y_player))  # Sempre usa o primeiro frame
    elif estado_atual == ESTADO_ATIRANDO:
        janela.blit(frames_atirando[frame_atual], (pos_x_player, pos_y_player))
    elif estado_atual == ESTADO_AGACHADO:
        janela.blit(frames_agachado[frame_atual], (pos_x_player, pos_y_player))
    elif estado_atual == ESTADO_PULANDO:
        janela.blit(frames_pulando[frame_atual], (pos_x_player, pos_y_player))
    elif estado_atual == ESTADO_CORRENDO:
        janela.blit(frames_correndo[frame_atual], (pos_x_player, pos_y_player))

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
pygame.quit()