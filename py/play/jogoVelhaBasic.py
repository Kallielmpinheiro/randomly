import random

posicoes = {
    '1': (0,0),
    '2': (0, 1),
    '3': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (2, 0),
    '8': (2, 1),
    '9': (2, 2)
}


tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    for linha in tabuleiro:
        print("[", end="")
        print("][".join(linha), end="")
        print("]")

    user = input("Escolha uma posição (1-9): ")
    if user not in posicoes or tabuleiro[posicoes[user][0]][posicoes[user][1]] != ' ':
        print("Posição inválida! Tente novamente.")
        continue
    tabuleiro[posicoes[user][0]][posicoes[user][1]] = 'X'

    vitoria_jogador = False
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == 'X':  # Verifica linhas
            vitoria_jogador = True
            break
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == 'X':  # Verifica colunas
            vitoria_jogador = True
            break
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X':      # Verifica diagonal principal
        vitoria_jogador = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':      # Verifica diagonal secundária
        vitoria_jogador = True

    if vitoria_jogador:
        for linha in tabuleiro:
            print("[", end="")
            print("][".join(linha), end="")
            print("]")
        print("Você venceu!")
        break

    empate = True
    for linha in tabuleiro:
        if ' ' in linha:
            empate = False
            break

    if empate:
        for linha in tabuleiro:
            print("[", end="")
            print("][".join(linha), end="")
            print("]")
        print("Empate!")
        break

    while True:
        pc = str(random.randint(1, 9))
        if tabuleiro[posicoes[pc][0]][posicoes[pc][1]] == ' ':
            tabuleiro[posicoes[pc][0]][posicoes[pc][1]] = 'O'
            break

    vitoria_computador = False
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == 'O':  # Verifica linhas
            vitoria_computador = True
            break
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == 'O':  # Verifica colunas
            vitoria_computador = True
            break
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O':      # Verifica diagonal principal
        vitoria_computador = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':      # Verifica diagonal secundária
        vitoria_computador = True

    if vitoria_computador:
        for linha in tabuleiro:
            print("[", end="")
            print("][".join(linha), end="")
            print("]")
        print("O computador venceu!")
        break
