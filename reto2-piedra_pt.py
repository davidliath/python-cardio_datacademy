def juego(j1, j2):

    gana1 = 'El ganador es el jugador 1.'
    gana2 = 'El ganador es el jugador 2.'
    empate = "Empate. Juegen otra vez."
    
    if j1 == 'piedra':
        if j2 == 'papel':
            print(gana2)
        elif j2 == 'tijera':
            print(gana1)
        else:
            print(empate)
    if j1 == 'papel':
        if j2 == 'tijera':
            print(gana2)
        elif j2 == 'piedra':
            print(gana1)
        else:
            print(empate)
    if j1 == 'tijera':
        if j2 == 'piedra':
            print(gana2)
        elif j2 == 'papel':
            print(gana1)
        else:
            print(empate)


def run():
    print('Con este programa podrás jugar ¡Piedra, Papel o Tijera!')

    jugador1 = input('Elección jugador 1: ')
    jugador2 = input('Elección jugador 2: ')

    juego(jugador1, jugador2)


if __name__ == '__main__':
    run()