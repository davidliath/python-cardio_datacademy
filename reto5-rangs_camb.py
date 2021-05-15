def comparacion(inf, sup):
    pass


def run():
    print('En este programa jugaremos a dar un número que se encuentre dentro de cierto rango dado.\nPara esto, primero estableceremos el rango dando un límite inferior y uno superior:')

    inferior = float(input('Límite inferior = '))
    superior = float(input('Límite superior = '))

    print('Ahora sí, da un número para checar si está dentro del rango:')

    comparacion(inferior, superior)

if __name__ == '__main__':
    run()