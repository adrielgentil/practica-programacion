import random

def display_board(resultado):
    default = ' '
    print(f' {default}  |  {default}  |  {default} ')
    print(f' {resultado[0]}  |  {resultado[1]}  |  {resultado[2]} ')
    print(f' {default}  |  {default}  |  {default} ')
    print('-----------------')
    print(f' {default}  |  {default}  |  {default} ')
    print(f' {resultado[3]}  |  {resultado[4]}  |  {resultado[5]} ')
    print(f' {default}  |  {default}  |  {default} ')
    print('-----------------')
    print(f' {default}  |  {default}  |  {default} ')
    print(f' {resultado[6]}  |  {resultado[7]}  |  {resultado[8]} ')
    print(f' {default}  |  {default}  |  {default} ')


def players_markers():
    marcador = input('Jugador 1 ingrese su marcador:\n>').upper()
    while marcador != 'X' and marcador != 'O':
        print('Respuesta incorrecta, ingrese X u O:\n>')
    if marcador == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def ubicacion(tablero, marcador, posicion):

    tablero[posicion] = marcador


def win_check(tablero, marcador):
    if tablero[0] == marcador and tablero[1] == marcador and tablero[2] == marcador:
        return True
    elif tablero[3] == marcador and tablero[4] == marcador and tablero[5] == marcador:
        return True
    elif tablero[6] == marcador and tablero[7] == marcador and tablero[8] == marcador:
        return True
    elif tablero[0] == marcador and tablero[3] == marcador and tablero[6] == marcador:
        return True
    elif tablero[1] == marcador and tablero[4] == marcador and tablero[7] == marcador:
        return True
    elif tablero[2] == marcador and tablero[5] == marcador and tablero[8] == marcador:
        return True
    elif tablero[0] == marcador and tablero[4] == marcador and tablero[8] == marcador:
        return True
    elif tablero[2] == marcador and tablero[4] == marcador and tablero[6] == marcador:
        return True
    else:
        return False

def eleccion_turno():
    turno = random.randint(1, 2)
    return turno


def checkeo_espacio(tablero, posicion):
    return tablero[posicion] == ' '


def tablero_lleno(tablero):
    for i in range(1, 10):
        if checkeo_espacio(tablero, i):
            return False
    return True


def eleccion_casilla(tablero):
    casilla = input('Ingrese una posicion:\n>')
    while casilla != [1, 2, 3, 4, 5, 6, 7, 8, 9] or not checkeo_espacio(tablero, casilla):
        casilla = int(input('Esa poscion no es valida, o ya esta en uso, por favor elija otra:\n>'))
    return casilla

    return casilla

def replay():
    respuesta = input('Quieren jugar de nuevo?:\n>').lower()
    while respuesta != 'si' or respuesta != 'no':
        print('Respuesta Inavlida, ingrese si o no:\n>')
    return respuesta == 'si'


while True:
    tablero = [' '] * 10
    jugador1, jugador2 = players_markers()
    turno = eleccion_turno()

    while True:
        if turno == 1:
            display_board(tablero)
            posicion = eleccion_casilla(tablero)
            ubicacion(tablero, jugador1, posicion)
            if win_check(tablero, jugador1):
                print('Felicidades Jugador 1, GANASTE!')
                break
            elif tablero_lleno():
                print('Fue un empate!')
                break

        else:
            

