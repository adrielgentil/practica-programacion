print('\nHola! Vamos a jugar al tateti. Espero te diviertas\n')


listres = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

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


while True:
    jugador1 = input('Jugador 1, quieres ser X o O?\n>').upper()
    if jugador1 == 'X':
        jugador2 = 'O'
    else:
        jugador2 = 'X'
    while True:
        res1 = int(input(f'Jugador 1, ingrese la coordenada de su {jugador1} (posicion del 1 al 9):\n>'))
        listres[res1 - 1] = jugador1
        if listres[0] == jugador1 and listres[1] == jugador1 and listres[2] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[3] == jugador1 and listres[4] == jugador1 and listres[5] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[6] == jugador1 and listres[7] == jugador1 and listres[8] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[0] == jugador1 and listres[3] == jugador1 and listres[6] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[1] == jugador1 and listres[4] == jugador1 and listres[7] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[2] == jugador1 and listres[5] == jugador1 and listres[8] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[0] == jugador1 and listres[4] == jugador1 and listres[8] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[2] == jugador1 and listres[4] == jugador1 and listres[6] == jugador1:
            print('Felicidades Jugador 1, GANASTE!')
            break
        display_board(listres)
        res2 = int(input(f'Jugador 2, ingrese la coordenada de su {jugador2} (posicion del 1 al 9):\n>'))
        listres[res2 - 1] = jugador2
        if listres[0] == jugador2 and listres[1] == jugador2 and listres[2] == jugador2:
            print('Felicidades Jugador 2, GANASTE!')
            break
        elif listres[3] == jugador2 and listres[4] == jugador2 and listres[5] == jugador2:
            print('Felicidades Jugador 2, GANASTE!')
            break
        elif listres[6] == jugador2 and listres[7] == jugador2 and listres[8] == jugador2:
            print('Felicidades Jugador 2, GANASTE!')
            break
        elif listres[0] == jugador2 and listres[3] == jugador2 and listres[6] == jugador2:
            print('Felicidades Jugador 2, GANASTE!')
            break
        elif listres[1] == jugador2 and listres[4] == jugador2 and listres[7] == jugador2:
            print('Felicidades Jugador 2, GANASTE!')
            break
        elif listres[2] == jugador2 and listres[5] == jugador2 and listres[8] == jugador2:
            print('Felicidades Jugador 2, GANASTE!')
            break
        elif listres[0] == jugador2 and listres[4] == jugador2 and listres[8] == jugador2:
            print('Felicidades Jugador 1, GANASTE!')
            break
        elif listres[2] == jugador2 and listres[4] == jugador2 and listres[6] == jugador2:
            print('Felicidades Jugador 1, GANASTE!')
            break
        display_board(listres)
        print('\n'*2)
    resp = input('Quieres jugar de nuevo?\n>')
    if resp.lower() == 'no':
        print('Gracias por jugar!')
        break