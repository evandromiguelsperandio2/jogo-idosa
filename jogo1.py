import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações da tela
LARGURA_TELA = 600
ALTURA_TELA = 600
TAMANHO_CELULA = 200
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo da Velha")

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    # Desenha as linhas do tabuleiro
    for i in range(1, 3):
        pygame.draw.line(tela, PRETO, (i * TAMANHO_CELULA, 0), (i * TAMANHO_CELULA, ALTURA_TELA), 5)
        pygame.draw.line(tela, PRETO, (0, i * TAMANHO_CELULA), (LARGURA_TELA, i * TAMANHO_CELULA), 5)

# Função para desenhar os símbolos X e O
def desenhar_simbolos(tabuleiro):
    fonte = pygame.font.Font(None, 100)
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] != " ":
                texto = fonte.render(tabuleiro[linha][coluna], True, VERMELHO if tabuleiro[linha][coluna] == "X" else AZUL)
                tela.blit(texto, (coluna * TAMANHO_CELULA + 50, linha * TAMANHO_CELULA + 50))

# Função para verificar vitória
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Função para verificar empate
def tabuleiro_cheio(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return True

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    turno = 0
    jogo_rodando = True

    while jogo_rodando:
        tela.fill(BRANCO)  # Limpar tela
        desenhar_tabuleiro()
        desenhar_simbolos(tabuleiro)

        # Checar eventos (cliques do mouse)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                coluna = x // TAMANHO_CELULA
                linha = y // TAMANHO_CELULA

                # Garantir que a célula está vazia
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogadores[turno % 2]

                    if verificar_vitoria(tabuleiro, jogadores[turno % 2]):
                        tela.fill(BRANCO)
                        desenhar_tabuleiro()
                        desenhar_simbolos(tabuleiro)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        print(f"Jogador {jogadores[turno % 2]} venceu!")
                        jogo_rodando = False

                    elif tabuleiro_cheio(tabuleiro):
                        tela.fill(BRANCO)
                        desenhar_tabuleiro()
                        desenhar_simbolos(tabuleiro)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        print("Empate!")
                        jogo_rodando = False

                    turno += 1

        pygame.display.update()

    pygame.quit()
    sys.exit()

# Iniciar o jogo
jogo_da_velha()

