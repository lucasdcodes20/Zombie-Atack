# menu/menu.py
import pygame
import sys
from pathlib import Path

# Configurações do menu
LARGURA_MENU, ALTURA_MENU = 800, 600
CORES = {
    "BRANCO": (255, 255, 255),
    "PRETO": (0, 0, 0),
    "VERDE": (0, 255, 0),
    "VERMELHO": (255, 0, 0)
}

class Menu:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_MENU, ALTURA_MENU))
        pygame.display.set_caption("Zombie Attack - Menu")
        self.fonte = pygame.font.SysFont("Arial", 40)
        self.opcoes = ["Iniciar Jogo", "Configurações", "Sair"]
        self.selecionado = 0

    def desenhar(self):
        self.tela.fill(CORES["PRETO"])
        for i, opcao in enumerate(self.opcoes):
            cor = CORES["VERDE"] if i == self.selecionado else CORES["BRANCO"]
            texto = self.fonte.render(opcao, True, cor)
            retangulo = texto.get_rect(center=(LARGURA_MENU // 2, ALTURA_MENU // 2 + i * 50))
            self.tela.blit(texto, retangulo)

    def executar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        self.selecionado = (self.selecionado + 1) % len(self.opcoes)
                    elif evento.key == pygame.K_UP:
                        self.selecionado = (self.selecionado - 1) % len(self.opcoes)
                    elif evento.key == pygame.K_RETURN:
                        if self.selecionado == 0:  # Iniciar Jogo
                            return "iniciar"
                        elif self.selecionado == 1:  # Configurações
                            print("Configurações selecionadas")  # Implemente depois
                        elif self.selecionado == 2:  # Sair
                            pygame.quit()
                            sys.exit()

            self.desenhar()
            pygame.display.flip()