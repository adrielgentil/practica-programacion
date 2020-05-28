import random
'''
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def mostrar_carta(self):
        print(f'{self.valor} de {self.palo}')

class Mazo:
    def __init__(self):
        self.cartas = []
        self.crear_mazo()

    def crear_mazo(self):
        for p in ['Pica', 'Trebol', 'Diamante', 'Corazones']:
            for val in range(1, 14):
                self.cartas.append(Carta(val, p))

    def mostrar_mazo(self):
        for c in self.cartas:
            c.mostrar_carta()
'''

palos = ('Diamante', 'Pica', 'Corazones', 'Trebol')
rangos = ('dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'Jack', 'Queen', 'King', 'Ace')
valores = {
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5,
    'seis': 6,
    'siete': 7,
    'ocho': 8,
    'nueve': 9,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
}


class Cartas:
    def __init__(self, rango, palo):
        self.rango = rango
        self.palo = palo

    def __str__(self):
        return f'{self.rango} de {self.palo}'


class Mazo:
    def __init__(self):
        self.mazo = []
        self.crear_mazo()

    def __str__(self):
        mazostr = ''
        for carta in self.mazo:
            mazostr += f'\n{carta.__str__()}'
        return mazostr

    def crear_mazo(self):
        for palo in palos:
            for rango in rangos:
                self.mazo.append(Cartas(rango, palo))

    def mezclar(self):
        random.shuffle(self.mazo)

    def repartir(self):
        carta = self.mazo.pop()
        return carta



class Jugador:
    def __init__(self):
        self.cartas = []
        self.suma = 0
        self.aces = 0

    def sumar_carta(self, carta):
        self.cartas.append(carta)
        self.suma += valores[carta.rango]
        if carta.rango == 'Ace':
            self.aces += 1

    def opcion_ace(self):
        while self.suma > 21 and self.aces:
            self.suma -= 10
            self.aces -= 1

class Billetera:
    def __init__(self):
        self.total = 100
        self.apuesta = 0

    def gana_apuesta(self):
        self.total += self.apuesta

    def pierde_apuesta(self):
        self.total -= self.apuesta


def tomar_apuesta(monto):
    while True:
        try:
            monto.apuesta = int(input(f'\nCuanto quieres apostar? Tienes {monto.total} fichas restante:\n>'))
        except ValueError:
            print('\nSe necesita ingresar un numero. Intenta de nuevo.')
        else:
            if monto.apuesta > monto.total:
                print(f'\nTe has exedido del monto total en tu billetera, te quedan {monto.total} fichas')
            else:
                break

def hit(jugador, mazo):
    jugador.sumar_carta(mazo.repartir())
    jugador.opcion_ace()

def hit_o_stay(mazo, jugador):
    while True:
            respuesta = input('\nOtra carta o te quedas?:\n>').lower()
            if 'q' in respuesta:
                print('\nEl jugador se queda, turno del Dealer')
                break
            elif 'otr' in respuesta:
                hit(jugador, mazo)
                for carta in jugador.cartas:
                    print(carta)
                print(f'Total: {jugador.suma}')
                if jugador.suma > 21:
                    break
            else:
                print('\nRespuesta invalida, ingrese "Otra carta" o "me quedo"')
                continue


def mostrar_algunas_cartas(jugador, dealer):
    print('\nMano del dealer:')
    print('- carta oculta -')
    print(dealer.cartas[0])
    print(f'Total: {valores[dealer.cartas[0].rango]}')
    print('\nMano del jugador')
    for carta in jugador.cartas:
        print(carta)
    print(f'Total: {jugador.suma}')


def mostrar_cartas(jugador, dealer):
    print('\nMano del Dealer:')
    for carta in dealer.cartas:
        print(carta)
    print(f'Total: {dealer.suma}')
    print('\nMano del jugador')
    for carta in jugador.cartas:
        print(carta)
    print(f'Total: {jugador.suma}')


def jugador_gana(billetera):
    print('\nGana el Jugador')
    billetera.gana_apuesta()


def jugador_pierde(billetera):
    print('\nPierde el jugador')
    billetera.pierde_apuesta()





billetera_jugador = Billetera()
while True:
    mazo = Mazo()
    mazo.mezclar()

    jugador = Jugador()
    jugador.sumar_carta(mazo.repartir())
    jugador.sumar_carta(mazo.repartir())

    dealer = Jugador()
    dealer.sumar_carta(mazo.repartir())
    dealer.sumar_carta(mazo.repartir())

    mostrar_algunas_cartas(jugador, dealer)

    tomar_apuesta(billetera_jugador)

    while True:
        hit_o_stay(mazo, jugador)

        if jugador.suma > 21:
            jugador_pierde(billetera_jugador)
            print(f'La billetera del jugador tiene {billetera_jugador.total}')
            break

        if jugador.suma <= 21:
            while dealer.suma < jugador.suma:
                hit(dealer, mazo)
        mostrar_cartas(jugador, dealer)
        if dealer.suma > 21:
            jugador_gana(billetera_jugador)
        elif dealer.suma > jugador.suma:
            jugador_pierde(billetera_jugador)
        elif dealer.suma < jugador.suma:
            jugador_gana(billetera_jugador)
        else:
            print('\nEs un empate!')

        print(f'La billetera del jugador tiene {billetera_jugador.total}')
        break
        
    if billetera_jugador.total <= 0:
        print('Te has quedado sin fichas, gracias por jugar!')
        break

    respuesta = input('Quieres seguir jugando?\n>').lower()
    while respuesta != 'si' and respuesta != 'no':
        respuesta = input('Respuesta invalida, ingresar si o no:>').lower()
    if respuesta == 'no':
        break






