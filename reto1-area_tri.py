def areatriangulo(base,altura):
    area = (base * altura) / 2
    return area


def run():
    print('Este programa calcula el área de un triángulo, dadas su base y altura.')

    b = int(input('Base: '))
    h = int(input('Altura: '))

    a = areatriangulo(b,h)
    
    print('El area de tu tiángulo es: \n' + str(a) + ' unidades cuadradas.')


if __name__ == '__main__':
    run()