# Importamos libreria random
import random

# Generamos número aleatorio
n1 = random.randint(1, 30)

# Funcion para preguntar si quiere jugar o no


def pregunta():
    sn = input()
    if sn.lower() == 'no':
        print('Oh, que pena, quería divertirme un poco. Será la próxima entonces. Chau!')
    elif sn.lower() == 'si':
        print('Genial! Voy a pensar un número del 1 al 30. Intentá adivinarlo.\nPero ojo, solo tenes 10 intentos\nIgual tranqui, te voy a ir ayudando.\nSuerte!')
        juego()
    else:
        print('Respuesta invalida, por favor solo responde Si o No.')
        pregunta()


def preg():
    sn = input()
    while sn.lower() != 'si' and sn.lower() != 'no':
        print('Respuesta invalida, por favor solo responde Si o No.')
        sn = input()
    if sn.lower() == 'si':
        print('Genial! Voy a pensar un número del 1 al 30. Intentá adivinarlo.\nPero ojo, solo tenes 10 intentos\nIgual tranqui, te voy a ir ayudando.\nSuerte!')
        juego()
    else:
        print('Oh, que pena, quería divertirme un poco. Será la próxima entonces. Chau!')





# Generamos una funcion del juego


def juego():
    num = int(input('Ingresá el número: '))
    while num <= 0 or num > 30:
        print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
        num = int(input('Ingresá el número: '))
    if num == n1:
        print('¡Que suerte! ¡Ganaste a la primera! ¿Queres jugar de nuevo?')
        preg()
    else:
        if num > n1:
            print('Ups, te pasaste. Proba de nuevo, te quedan 9 intentos: ')
        else:
            print('Ups, te quedaste corto. Proba de nuevo, te quedan 9 intentos: \n')
        num = int(input('Ingresá el número: '))
        while num <= 0 or num > 30:
            print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
            num = int(input('Ingresá el número: '))
        if num == n1:
            print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
            preg()
        else:
            if num > n1:
                print('Ups, te pasaste. Proba de nuevo, te quedan 8 intentos: ')
            else:
                print('Ups, te quedaste corto. Proba de nuevo, te quedan 8 intentos: \n')
            num = int(input('Ingresá el número: '))
            while num <= 0 or num > 30:
                print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                num = int(input('Ingresá el número: '))
            if num == n1:
                print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                preg()
            else:
                if num > n1:
                    print('Ups, te pasaste. Proba de nuevo, te quedan 7 intentos: ')
                else:
                    print('Ups, te quedaste corto. Proba de nuevo, te quedan 7 intentos: \n')
                num = int(input('Ingresá el número: '))
                while num <= 0 or num > 30:
                    print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                    num = int(input('Ingresá el número: '))
                if num == n1:
                    print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                    preg()
                else:
                    if num > n1:
                        print('Ups, te pasaste. Proba de nuevo, te quedan 6 intentos: ')
                    else:
                            print('Ups, te quedaste corto. Proba de nuevo, te quedan 6 intentos: \n')
                    num = int(input('Ingresá el número: '))
                    while num <= 0 or num > 30:
                        print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                        num = int(input('Ingresá el número: '))
                    if num == n1:
                        print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                        preg()
                    else:
                        if num > n1:
                            print('Ups, te pasaste. Proba de nuevo, te quedan 5 intentos: ')
                        else:
                            print('Ups, te quedaste corto. Proba de nuevo, te quedan 5 intentos: \n')
                        num = int(input('Ingresá el número: '))
                        while num <= 0 or num > 30:
                            print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                            num = int(input('Ingresá el número: '))
                        if num == n1:
                            print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                            preg()
                        else:
                            if num > n1:
                                print('Ups, te pasaste. Proba de nuevo, te quedan 4 intentos: ')
                            else:
                                print('Ups, te quedaste corto. Proba de nuevo, te quedan 4 intentos: \n')
                            num = int(input('Ingresá el número: '))
                            while num <= 0 or num > 30:
                                print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                                num = int(input('Ingresá el número: '))
                            if num == n1:
                                print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                                preg()
                            else:
                                if num > n1:
                                    print('Ups, te pasaste. Proba de nuevo, te quedan 3 intentos: ')
                                else:
                                    print('Ups, te quedaste corto. Proba de nuevo, te quedan 3 intentos: \n')
                            num = int(input('Ingresá el número: '))
                            while num <= 0 or num > 30:
                                print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                                num = int(input('Ingresá el número: '))
                            if num == n1:
                                print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                                preg()
                            else:
                                if num > n1:
                                    print('Ups, te pasaste. Proba de nuevo, te quedan 2 intentos: ')
                                else:
                                    print('Ups, te quedaste corto. Proba de nuevo, te quedan 2 intentos: \n')
                                num = int(input('Ingresá el número: '))
                                while num <= 0 or num > 30:
                                    print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                                    num = int(input('Ingresá el número: '))
                                if num == n1:
                                    print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                                    preg()
                                else:
                                    if num > n1:
                                        print('Ups, te pasaste. Proba de nuevo, solo te queda un intento, asi que piensalo bien: ')
                                    else:
                                        print('Ups, te quedaste corto. Proba de nuevo, solo te queda un intento, asi que piensalo bien: \n')
                                    num = int(input('Ingresá el número: '))
                                    while num <= 0 or num > 30:
                                        print('Acordate que es un numero entre 1 y 30, asi que intentalo de nuevo. Tranqui, esto no cuenta como intento')
                                        num = int(input('Ingresá el número: '))
                                    if num == n1:
                                        print('¡Que bien! ¡Ganaste! ¿Queres jugar de nuevo?')
                                        preg()
                                    else:
                                        print('Uhhh, perdiste, lo lamento, realmente queria que adivinaras, te di pistas y todo.'
                                          '\nPero bueno, que se le va a hacer. ¿querés intentar de nuevo?')
                                    preg()



# Introducción e inicio del juego

print('\nHola! ¿Cómo te llamas?')
nombre = input()

print('Bien ' + nombre.capitalize() + ', ¿querés jugar un juego?')

preg()
