

import random
# Asignacion de algunas variables
limite_inf = 1
limite_sup = 20
posibilidades = 5


print(f'Vamos a jugar un juego. Voy a adivinar un numero del {limite_inf} al {limite_sup}. '
      f'Tienes {posibilidades} oportunidades para adivinar, pensalo bien')

#Asignacion de ms variables
n1 = random.randint(limite_inf, limite_sup)
intentos = 1

# Creacion de un ciclo infito para el juego
while True:
    while intentos <= posibilidades:
        pos_res = posibilidades - intentos
        num = int(input('Ingresa tu numero: '))
        while num > limite_sup or num < limite_inf:
            print(f'El numero esta fuera del rango, intentalo de nuevo con un numero entre {limite_inf} y {limite_sup}')
            num = int(input('Ingresa tu numero: '))
        if n1 == num and intentos == 1:
            print('Que suerte, ganaste a la primera!')
            break
        elif n1 == num and intentos != 1:
            print('GANASTE!')
            break
        elif num > n1 and intentos < posibilidades:
            print(f'Ups, te pasaste, proba con un numero mas chico. Te quedan {pos_res} intentos')
        elif num < n1 and intentos < posibilidades:
            print(f'Ups, te quedaste corto, proba con un numero mas grande. Te quedan {pos_res} intentos')
        intentos += 1
    if num != n1:
        print('PERDISTE!')
    print('Queres seguir jugando?')
    sn = input()
    while sn.lower() != 'si' and sn.lower() != 'no':
        print('Respuesta invalida, por favor solo responde Si o No.')
        sn = input()
    if sn.lower() == 'si':
        print()
        intentos = 1
    else:
        print('Oh, que pena, quería divertirme un poco. Será la próxima entonces. Chau!')
        break