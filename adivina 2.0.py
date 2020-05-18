import random
# Asignamos variables

limite_inf = 1
limite_sup = 20
n1 = random.randint (limite_inf, limite_sup)
posibilidades = 5
global intentos
intentos = 0
njuegos = 0

# Creamos funcion para preguntar si se quiere jugar
def preg():
    if njuegos == 0:
        print('Queres jugar?')
    else:
        print('Queres jugar de nuevo?')
    sn = input()
    while sn.lower() != 'si' and sn.lower() != 'no':
        print('Respuesta invalida, por favor solo responde Si o No.')
        sn = input()
    if sn.lower() == 'si':
        print('Genial! Voy a pensar un número del 1 al 30. Intentá adivinarlo.\nPero ojo, solo tenes 10 intentos\nIgual tranqui, te voy a ir ayudando.\nSuerte!')
        juego()
    else:
        print('Oh, que pena, quería divertirme un poco. Será la próxima entonces. Chau!')
    return sn


# Funcion del juego
def juego():
    while intentos < posibilidades:
        pos_res = posibilidades - intentos
        print('Adivina el numero: ')
        guess = int(input())
        while guess <= 0 or guess > 30:
            print(f'Acordate que es un numero entre {limite_inf} y {limite_sup}, '
                  f'asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
            guess = int(input('Ingresá el número: '))
        if n1 == guess and intentos == 0:
            print('Que suerte, ganaste a la primera!')
            break
        elif n1 == guess and intentos != 0:
            print('GANASTE!')
            break
        elif guess > n1 and intentos < posibilidades:
            intentos += 1
            print(f'Ups, te pasaste, proba con un numero mas chico. Te quedan {pos_res} intentos')
        elif guess < n1 and intentos < posibilidades:
            intentos += 1
            print(f'Ups, te quedaste corto, proba con un numero mas grande. Te quedan {pos_res} intentos'')
        intentos += 1


print(f'Hola, vamos a jugar un juego. Tenes que adivinar un numero entre {limite_inf} y {limite_sup}. Solo tienenes {posibilidades} intentos')
preg()
juego()
