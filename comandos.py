import pygame

# Estados do soldado
ESTADO_PARADO = 0
ESTADO_ATIRANDO = 1
ESTADO_AGACHADO = 2
ESTADO_PULANDO = 3
ESTADO_CORRENDO = 4

# Função para recortar os frames de um spritesheet
def recortar_frames(spritesheet, num_frames, largura_frame, altura_frame):
    frames = []
    for i in range(num_frames):
        frame = spritesheet.subsurface((i * largura_frame, 0, largura_frame, altura_frame))
        frames.append(frame)
    return frames

# Função para atualizar a posição e o estado do soldado
def atualizar_soldado(teclas, pos_x_player, pos_y_player, estado_atual, vel_soldier_player, largura_janela, altura_janela, largura_frame, altura_frame):
    # Movimentação do soldier
    if teclas[pygame.K_w]:  # Tecla W: Move para cima
        pos_y_player -= vel_soldier_player
    if teclas[pygame.K_s]:  # Tecla S: Move para baixo
        pos_y_player += vel_soldier_player
    if teclas[pygame.K_a]:  # Tecla A: Move para a esquerda
        pos_x_player -= vel_soldier_player
    if teclas[pygame.K_d]:  # Tecla D: Move para a direita
        pos_x_player += vel_soldier_player

    # Verifica se a tecla CTRL está pressionada (atirar)
    if teclas[pygame.K_LCTRL] or teclas[pygame.K_RCTRL]:
        estado_atual = ESTADO_ATIRANDO
    # Verifica se a tecla SHIFT está pressionada (agachar)
    elif teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
        estado_atual = ESTADO_AGACHADO
    # Verifica se a tecla ESPAÇO está pressionada (pular)
    elif teclas[pygame.K_SPACE]:
        estado_atual = ESTADO_PULANDO
    # Verifica se a tecla TAB está pressionada (correr)
    elif teclas[pygame.K_TAB]:
        estado_atual = ESTADO_CORRENDO
    else:
        estado_atual = ESTADO_PARADO  # Parado se nenhuma tecla de ação estiver pressionada

    # Limita a movimentação para dentro da tela
    pos_x_player = max(0, min(pos_x_player, largura_janela - largura_frame))
    pos_y_player = max(0, min(pos_y_player, altura_janela - altura_frame))

    return pos_x_player, pos_y_player, estado_atual

# Função para atualizar a animação do soldado
def atualizar_animacao(estado_atual, frame_atual, contador_animacao, velocidade_animacao, frames_parado, frames_atirando, frames_agachado, frames_pulando, frames_correndo):
    contador_animacao += 1
    if contador_animacao >= velocidade_animacao:
        # Avança para o próximo frame da animação atual
        if estado_atual == ESTADO_PARADO:
            frame_atual = 0  # Sempre usa o primeiro frame (não há animação)
        elif estado_atual == ESTADO_ATIRANDO:
            frame_atual = (frame_atual + 1) % len(frames_atirando)
        elif estado_atual == ESTADO_AGACHADO:
            frame_atual = (frame_atual + 1) % len(frames_agachado)
        elif estado_atual == ESTADO_PULANDO:
            frame_atual = (frame_atual + 1) % len(frames_pulando)
        elif estado_atual == ESTADO_CORRENDO:
            frame_atual = (frame_atual + 1) % len(frames_correndo)
        contador_animacao = 0  # Reinicia o contador

    return frame_atual, contador_animacao