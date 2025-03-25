import pygame
import os

class Inimigo:
    def __init__(self, x, y):
        # Estados
        self.ESTADO_PARADO = 0
        self.ESTADO_ATACANDO = 1
        self.estado = self.ESTADO_PARADO
        
        # Posição fixa
        self.x = x
        self.y = y
        
        # Animação
        self.frame_atual = 0
        self.contador_animacao = 0
        self.velocidade_animacao = 8
        
        # Carrega sprites com tratamento de erro robusto
        try:
            base_path = os.path.dirname(__file__)
            correr_path = os.path.join(base_path, 'C:/Jogo/asset/imagens/inimigos/Run.png')
            atacar_path = os.path.join(base_path, 'C:/Jogo/asset/imagens/inimigos/Attack_1.png')
            
            self.spritesheet_correr = pygame.image.load(correr_path).convert_alpha()
            self.spritesheet_atacar = pygame.image.load(atacar_path).convert_alpha()
            
            print("Sprites dos inimigos carregados com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar sprites: {e}")
            # Fallback visual
            self.spritesheet_correr = pygame.Surface((128, 128), pygame.SRCALPHA)
            self.spritesheet_correr.fill((255, 0, 0, 255))
            self.spritesheet_atacar = pygame.Surface((128, 128), pygame.SRCALPHA)
            self.spritesheet_atacar.fill((255, 100, 0, 255))
        
        # Recorta frames
        self.frames_correr = self.recortar_frames(self.spritesheet_correr, 8)
        self.frames_atacar = self.recortar_frames(self.spritesheet_atacar, 4)

    def recortar_frames(self, spritesheet, num_frames):
        frames = []
        largura = spritesheet.get_width() // num_frames
        altura = spritesheet.get_height()
        for i in range(num_frames):
            frame = spritesheet.subsurface((i * largura, 0, largura, altura))
            frames.append(frame)
        return frames

    def atualizar(self):
        self.contador_animacao += 1
        if self.contador_animacao >= self.velocidade_animacao:
            if self.estado == self.ESTADO_PARADO:
                self.frame_atual = (self.frame_atual + 1) % len(self.frames_correr)
            else:
                self.frame_atual = (self.frame_atual + 1) % len(self.frames_atacar)
            self.contador_animacao = 0

    def desenhar(self, tela):
        if self.estado == self.ESTADO_PARADO:
            frame = self.frames_correr[self.frame_atual]
        else:
            frame = self.frames_atacar[self.frame_atual]
        
        # Desenha virado para esquerda
        tela.blit(pygame.transform.flip(frame, True, False), (self.x, self.y))