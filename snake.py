import pygame
import random
import serial
import time

# ==== CONFIGURAÇÃO DA SERIAL ====
# Troque COM3 pelo nome da porta que seu Arduino aparece
# No Linux/Mac pode ser algo como "/dev/ttyUSB0"
ser = serial.Serial('COM3', 9600)
time.sleep(2)  # tempo para estabilizar a conexão

# ==== CONFIGURAÇÃO DO JOGO ====
pygame.init()

# Tamanho da tela
largura = 600
altura = 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake com Arduino")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Tamanho do bloco da cobrinha
tamanho_bloco = 20
velocidade = 10

# Fonte para o placar
fonte = pygame.font.SysFont(None, 35)

# Função para mostrar a pontuação
def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, VERMELHO)
    janela.blit(texto, [10, 10])

# Função principal do jogo
def jogo():
    fim_de_jogo = False

    # Posição inicial
    x = largura / 2
    y = altura / 2

    # Movimento inicial
    dx = 0
    dy = 0

    # Corpo da cobra
    cobra = []
    tamanho_cobra = 1

    # Primeira comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20

    clock = pygame.time.Clock()
    pontos = 0

    while not fim_de_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True

        # ==== RECEBE COMANDO DO ARDUINO ====
        if ser.in_waiting > 0:
            comando = ser.readline().decode('utf-8').strip()
            direcao, botao = comando.split(";")

            if direcao == "UP" and dy == 0:
                dx = 0
                dy = -tamanho_bloco
            elif direcao == "DOWN" and dy == 0:
                dx = 0
                dy = tamanho_bloco
            elif direcao == "LEFT" and dx == 0:
                dx = -tamanho_bloco
                dy = 0
            elif direcao == "RIGHT" and dx == 0:
                dx = tamanho_bloco
                dy = 0

        # Atualiza posição
        x += dx
        y += dy

        # Verifica se bateu na parede
        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        # Atualiza a tela
        janela.fill(PRETO)
        pygame.draw.rect(janela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Corpo da cobra
        cabeca = [x, y]
        cobra.append(cabeca)
        if len(cobra) > tamanho_cobra:
            del cobra[0]

        # Verifica colisão com o próprio corpo
        for parte in cobra[:-1]:
            if parte == cabeca:
                fim_de_jogo = True

        # Desenha a cobra
        for parte in cobra:
            pygame.draw.rect(janela, VERDE, [parte[0], parte[1], tamanho_bloco, tamanho_bloco])

        mostrar_pontuacao(pontos)
        pygame.display.update()

        # Comeu a comida?
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20
            tamanho_cobra += 1
            pontos += 1

        clock.tick(velocidade)

    pygame.quit()

# Executa o jogo
jogo()
