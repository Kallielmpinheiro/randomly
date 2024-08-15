import random

escolhas = {
    1 : "pedra",
    2 : "tesoura",
    3 : "papel",
    4 : "lagarto",
    5 : "Spock"
}

pc = random.randrange(1,6)

while True:
    user = input("Escolha (1: Pedra, 2: Tesoura, 3: Papel, 4: Lagarto, 5: Spock): ")
    if not user.isdigit() or int(user) not in range(1,6):
        print("Escolha um numero certo")
    else:
        user=int(user)
        print(f"Você escolheu: {escolhas[user]}")
        print(f"O computador escolheu: {escolhas[pc]}")

        if user == pc:
            print(f"Ambos escolheram {escolhas[user]}. Empate!")
        elif (user == 1 and pc in [2, 4]) or \
            (user == 2 and pc in [3, 4]) or \
            (user == 3 and pc in [1, 5]) or \
            (user == 4 and pc in [5, 3]) or \
            (user == 5 and pc in [1, 2]):
            print(f"Você ganhou! {escolhas[user]} vence {escolhas[pc]}.")
        else:
            print(f"Você perdeu! {escolhas[pc]} vence {escolhas[user]}.")
            
        retry = input("Deseja jogar novamente: ?")
        if retry not in ["s","sim"]:
            print("vlw")
            break
            