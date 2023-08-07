import random

player = 0
maquina = 0

while True:
    numero = random.randint(0, 3)

    numero_player = int(input("¿Qué número crees que es del 0 al 3?: "))

    if numero_player == numero:
        print("¡Has ganado!")
        player += 1
        print(f"El contador es de {player} - {maquina}")
    else:
        print(f"Has perdido, el número de la máquina era {numero}")
        maquina += 1
        print(f"El contador es de {player} - {maquina}")

    seguir = input("¿Quieres continuar? (si/no)")

    if seguir == "no":
        break

    if seguir != "si":
        print("Respuesta inválida. Continuando el juego...")

print(f"El contador es de {player} - {maquina}")