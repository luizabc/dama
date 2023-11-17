import tkinter as tk

# Tamanho do tabuleiro de damas
tam_tabuleiro = 8
tamanho_celula = 60  # Tamanho de cada célula do tabuleiro em pixels

# Inicializar o tabuleiro de damas
tabuleiro = [[' ' for _ in range(tam_tabuleiro)] for _ in range(tam_tabuleiro)]
jogador_atual = 'O'
peca_selecionada = None  # Nenhuma peça selecionada inicialmente

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    global canvas
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            cor = 'white' if (i + j) % 2 == 0 else 'gray'
            canvas.create_rectangle(j * tamanho_celula, i * tamanho_celula, 
                                    (j + 1) * tamanho_celula, (i + 1) * tamanho_celula, 
                                    fill=cor)

# Função para inicializar as peças no tabuleiro
def inicializar_pecas():
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            if (i + j) % 2 == 1:
                if i < 3:
                    tabuleiro[i][j] = 'O'  # Peças do jogador 1 (O)
                elif i > 4:
                    tabuleiro[i][j] = 'X'  # Peças do jogador 2 (X)

# Função para desenhar as peças no tabuleiro
def desenhar_pecas():
    global canvas
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            peca = tabuleiro[i][j]
            if peca != ' ':
                centro_x = j * tamanho_celula + tamanho_celula // 2
                centro_y = i * tamanho_celula + tamanho_celula // 2
                canvas.create_oval(centro_x - 20, centro_y - 20, 
                                   centro_x + 20, centro_y + 20, 
                                   fill='black' if peca == 'X' else 'red')

# Função para atualizar o tabuleiro
def atualizar_tabuleiro():
    global canvas
    canvas.delete("all")
    desenhar_tabuleiro()
    desenhar_pecas()

# Função para lidar com o clique do mouse no tabuleiro
def clique_tabuleiro(event):
    global jogador_atual, peca_selecionada
    coluna = event.x // tamanho_celula
    linha = event.y // tamanho_celula

    if peca_selecionada:
        if movimento_valido(linha, coluna):
            # Movimentar a peça selecionada
            linha_origem, coluna_origem = peca_selecionada
            tabuleiro[linha][coluna] = jogador_atual
            tabuleiro[linha_origem][coluna_origem] = ' '

            # Verificar e realizar captura de peça
            if abs(linha - linha_origem) == 2:
                linha_captura = (linha_origem + linha) // 2
                coluna_captura = (coluna_origem + coluna) // 2
                tabuleiro[linha_captura][coluna_captura] = ' '

            limpar_selecao()
            alternar_jogador()
        else:
            limpar_selecao()
    else:
        if tabuleiro[linha][coluna] == jogador_atual:
            # Selecionar uma peça
            peca_selecionada = (linha, coluna)

    atualizar_tabuleiro()

def movimento_valido(linha_destino, coluna_destino):
    linha_origem, coluna_origem = peca_selecionada
    oponente = 'X' if jogador_atual == 'O' else 'O'
    direcao = 1 if jogador_atual == 'O' else -1

    # Movimento simples para frente
    movimento_simples = linha_destino == linha_origem + direcao and abs(coluna_destino - coluna_origem) == 1

    # Captura para frente
    captura_frente = (
        linha_destino == linha_origem + 2 * direcao and 
        abs(coluna_destino - coluna_origem) == 2 and 
        tabuleiro[linha_origem + direcao][coluna_origem + (coluna_destino - coluna_origem) // 2] == oponente
    )

    # Captura para trás
    captura_tras = (
        linha_destino == linha_origem - 2 * direcao and 
        abs(coluna_destino - coluna_origem) == 2 and 
        tabuleiro[linha_origem - direcao][coluna_origem + (coluna_destino - coluna_origem) // 2] == oponente
    )

    return movimento_simples or captura_frente or captura_tras

def limpar_selecao():
    global peca_selecionada
    peca_selecionada = None

def alternar_jogador():
    global jogador_atual
    jogador_atual = 'X' if jogador_atual == 'O' else 'O'

# Inicializa a janela do Tkinter
def iniciar_jogo():
    global canvas
    root = tk.Tk()
    root.title("Jogo de Damas")
    canvas = tk.Canvas(root, width=tam_tabuleiro * tamanho_celula, height=tam_tabuleiro * tamanho_celula)
    canvas.pack()
    canvas.bind("<Button-1>", clique_tabuleiro)

    inicializar_pecas()
    atualizar_tabuleiro()

    root.mainloop()

# Iniciar o jogo
iniciar_jogo()

