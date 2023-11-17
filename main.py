# Tamanho do tabuleiro de damas
tam_tabuleiro = 8

# Inicializar o tabuleiro de damas
tabuleiro = [[' ' for _ in range(tam_tabuleiro)] for _ in range(tam_tabuleiro)]

# Função para exibir o tabuleiro de damas
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * (tam_tabuleiro * 4 - 1))

# Função para inicializar as peças no tabuleiro
def inicializar_pecas(tabuleiro):
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            if (i + j) % 2 == 1:
                if i < 3:
                    tabuleiro[i][j] = 'O'  # Peças do jogador 1 (O)
                elif i > 4:
                    tabuleiro[i][j] = 'X'  # Peças do jogador 2 (X)

# Função para mover uma peça
def mover_peca(tabuleiro, movimento, jogador):
    # Separar as coordenadas de origem e destino a partir do movimento
    origem, destino = movimento.split()

    # Converter as coordenadas para índices da matriz
    origem_x, origem_y = ord(origem[0].lower()) - ord('a'), int(origem[1]) - 1
    destino_x, destino_y = ord(destino[0].lower()) - ord('a'), int(destino[1]) - 1

    # Verificar se a origem e o destino estão dentro dos limites do tabuleiro
    if not (0 <= origem_x < tam_tabuleiro and 0 <= origem_y < tam_tabuleiro and
            0 <= destino_x < tam_tabuleiro and 0 <= destino_y < tam_tabuleiro):
        print("Movimento fora dos limites do tabuleiro.")
        return False

    # Verificar se a origem contém uma peça do jogador atual
    if tabuleiro[origem_y][origem_x] != jogador:
        print("Você não possui uma peça na posição de origem.")
        return False

    # Verificar se o movimento é diagonal de uma casa para frente
    if abs(destino_x - origem_x) == 1 and abs(destino_y - origem_y) == 1:
        # Verificar se o destino está vazio
        if tabuleiro[destino_y][destino_x] == ' ':
            # Realizar o movimento
            tabuleiro[origem_y][origem_x] = ' '
            tabuleiro[destino_y][destino_x] = jogador
            return True
        else:
            print("A casa de destino já está ocupada.")
            return False
    else:
        print("Movimento inválido. Movimento diagonal de uma casa para frente permitido.")
        return False

# Função principal do jogo de damas
def jogar_damas():
    inicializar_pecas(tabuleiro)
    jogador_atual = 'O'

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f'É a vez do jogador {jogador_atual}')
        movimento = input('Informe o movimento (por exemplo, "e3 d4"): ')

        if mover_peca(tabuleiro, movimento, jogador_atual):
            # Troque o jogador após um movimento válido
            jogador_atual = 'X' if jogador_atual == 'O' else 'O'

# Iniciar o jogo de damas
jogar_damas()
