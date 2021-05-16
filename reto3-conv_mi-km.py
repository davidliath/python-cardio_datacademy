def conversor(mi):
    km = mi * 1.609344
    print(str(mi) + ' mi  =  ' + str(km) + ' km.')


def run():
    print('Conversor de Millas a Kilómetros.')
    m = float(input('Millas: '))

    conversor(m)


if __name__ == '__main__':
    run()