import pygame
from pathlib import Path

class Inimigo:
    def __init__(self, x, y):
        # Estados do inimigo (apenas 2 como solicitado)
        self.ESTADO_PARADO = 0
        self.ESTADO_ATACANDO = 1
        self.estado = self.ESTADO_PARADO
        
        # Posição fixa no canto inferior direito
        self.x = x
        self.y = y
        
        # Controle de animação
        self.frame_atual = 0
        self.contador_animacao = 0
        self.velocidade_animacao = 10
        
        # Carrega spritesheets
        try:
            self.spritesheet_correr = pygame.image.load('assets/inimigos/Correr.png').convert_alpha()
            self.spritesheet_atacar = pygame.image.load('assets/inimigos/Atacar.png').convert_alpha()
        except:
            # Fallback visual caso as imagens não existam
            self.spritesheet_correr = pygame.Surface((128, 128), pygame.SRCALPHA)
            self.spritesheet_correr.fill((255, 0, 0, 128))  # Vermelho transparente
            self.spritesheet_atacar = pygame.Surface((128, 128), pygame.SRCALPHA)
            self.spritesheet_atacar.fill((255, 100, 100, 200))  # Vermelho mais claro
        
        # Recorta frames das animações
        self.frames_correr = self.recortar_frames(self.spritesheet_correr, 8)  # 8 frames de corrida
        self.frames_atacar = self.recortar_frames(self.spritesheet_atacar, 6)  # 6 frames de ataque
    
    def recortar_frames(self, spritesheet, num_frames):
        """Recorta os frames da spritesheet"""
        frames = []
        largura_frame = spritesheet.get_width() // num_frames
        for i in range(num_frames):
            frame = spritesheet.subsurface((i * largura_frame, 0, largura_frame, spritesheet.get_height()))
            frames.append(frame)
        return frames
    
    def atualizar(self):
        """Atualiza a animação (sem movimento, como solicitado)"""
        self.contador_animacao += 1
        if self.contador_animacao >= self.velocidade_animacao:
            if self.estado == self.ESTADO_PARADO:
                # Fica alternando entre os frames de corrida mesmo parado
                self.frame_atual = (self.frame_atual + 1) % len(self.frames_correr)
            else:
                # Anima o ataque
                self.frame_atual = (self.frame_atual + 1) % len(self.frames_atacar)
            self.contador_animacao = 0
    
    def desenhar(self, tela):
        """Desenha o inimigo na tela"""
        if self.estado == self.ESTADO_PARADO:
            frame = self.frames_correr[self.frame_atual]
        else:
            frame = self.frames_atacar[self.frame_atual]
        
        # Desenha o sprite virado para esquerda (flip horizontal)
        tela.blit(pygame.transform.flip(frame, True, False), (self.x, self.y))