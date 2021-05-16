from math import pi


def volumen_cil(r, h):
    area_circulo = pi * r**2
    vol = area_circulo * h
    print('V_cilindro = ' + str(round(vol,4)) + ' cm^2')


def run():
    print('Esta es una calculadora de volúmenes de cilindros.\nDame el radio y la altura del cilindro para calcularlo:')

    radio = float(input('Radio (cm)    = '))
    altura = float(input('Altura (cm)   = '))
    volumen_cil(radio, altura)


if __name__ == '__main__':
    run()