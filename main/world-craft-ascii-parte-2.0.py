import random
import string

def generar_cdia():
    generador = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0,10)))

    return generador

def itens(iten):
    iten_ = iten
    return iten_


if __name__ == '__main__':
    cont = 0
    cdias = []
    escalafon = []
    nombres = []

    while True:
        print('Opciones:\n1.Crear nuevo jugador\n2.Salir')
        opc = int(input('Ingresar opcion: '))

        if opc == 1:
            nombre = input('nombre: ')
            nombres.append(itens(nombre))
            escalafon.append(itens(cont))
            cdias.append(itens(generar_cdia()))
            cont +=1
        elif opc == 2:
            break
    print(nombres,'\n')
    print(cdias,'\n')
    print(escalafon,'\n')
