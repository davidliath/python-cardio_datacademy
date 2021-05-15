def run():
    print('Esta es una calculadora de volúmenes de cilindros.\nDame el radio y la altura del cilindro para calcularlo:')

    radio = float(input('Radio (cm)    = '))
    altura = float(input('Altura (cm)   = '))
    volumen_cil(radio, altura)



if __name__ == '__main__':
    run()