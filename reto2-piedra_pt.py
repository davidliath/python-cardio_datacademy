def run():
    print('Con este programa podrás jugar ¡Piedra, Papel o Tijera!')

    jugador1 = input('Elección jugador 1: ')
    jugador2 = input('Elección jugador 2: ')

    juego(jugador1, jugador2)


if __name__ == '__main__':
    run()