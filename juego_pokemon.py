import random


def tirar_dado(valor):
    return random.randint(1, valor)


class Pokemon:
    def __init__(self, nombre, ataque, vida, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.tipo = tipo

    def gano(self):
        print(f'{self.nombre} ha ganado!!!\n')


pokemones = []
pokemones.append(Pokemon('Starmie', 15, 115, 'agua'))
pokemones.append(Pokemon('Charmander', 17, 110, 'fuego'))
pokemones.append(Pokemon('Bulbasaur', 13, 125, 'planta'))
pokemones.append(Pokemon('Pikachu', 15, 110, 'electrico'))
turno = tirar_dado(2)


def agregar_pokemon():
    print('Que pokemon queres agregar?')
    nombre = input('>').capitalize()
    print('Cual es el ataque de tu pokemon?')
    ataque = input('>')
    print('Cual es la vida de tu pokemon?')
    vida = input('>')
    print('Cual es el tipo de tu pokemon?')
    tipo = input('>').lower
    pokemones.append(Pokemon(nombre, ataque, vida, tipo))

while True:
    print('\nHay algun pokemon que quieras agregar?')
    op = input('>').lower()
    while op != 'si' and op != 'no':
        print('Respuesta invalida, por favor ingresa si o no:')
        op = input('>').lower()
    if op == 'si':
        agregar_pokemon()
    else:
        break

while True:
    pokemon1 = None
    pokemon2 = None
    print('\nJugador 1, ¿Qué pokemon quieres usar?')
    p1 = input('>').capitalize()
    while pokemon1 is None:
        for pokemon in pokemones:
            if p1 == pokemon.nombre:
                pokemon1 = pokemon
        if pokemon1 is None:
            print('\nEste pokemon no esta disponible, por favor elige otro:')
            p1 = input('>').capitalize()
    print('\nJugador 2, ¿Qué pokemon quieres usar?')
    p2 = input('>').capitalize()
    while p1 == p2:
        print('\nEse pokemon ya fue elegido, escoge otro por favor:')
        p2 = input('>').capitalize()
    while pokemon2 is None:
        for pokemon in pokemones:
            if p2 == pokemon.nombre:
                pokemon2 = pokemon
        if pokemon2 is None:
            print('\nEste pokemon no esta disponible, por favor elige otro:')
            p1 = input('>').capitalize()
    vida_poke1 = pokemon1.vida
    ataque_poke1 = pokemon1.ataque
    vida_poke2 = pokemon2.vida
    ataque_poke2 = pokemon2.ataque
    if pokemon1.tipo == 'agua' and pokemon2.tipo == 'fuego':
        ataque_poke1 = pokemon1.ataque * 1.5
    elif pokemon1.tipo == 'fuego' and pokemon2.tipo == 'planta':
        ataque_poke1 = pokemon1.ataque * 1.5
    elif pokemon1.tipo == 'planta' and pokemon2.tipo == 'agua':
        ataque_poke1 = pokemon1.ataque * 1.5
    elif pokemon1.tipo == 'electrico' and pokemon2.tipo == 'agua':
        ataque_poke1 = pokemon1.ataque * 1.5
    elif pokemon2.tipo == 'agua' and pokemon1.tipo == 'fuego':
        ataque_poke2 = pokemon2.ataque * 1.5
    elif pokemon2.tipo == 'fuego' and pokemon1.tipo == 'planta':
        ataque_poke2 = pokemon2.ataque * 1.5
    elif pokemon2.tipo == 'planta' and pokemon1.tipo == 'agua':
        ataque_poke2 = pokemon2.ataque * 1.5
    elif pokemon2.tipo == 'electrico' and pokemon1.tipo == 'agua':
        ataque_poke1 = pokemon1.ataque * 1.5
    while vida_poke1 > 0 and vida_poke2 > 0:
        if turno == 1:
            vida_poke2 -= ataque_poke1
            print(f'\n{pokemon2.nombre} recibio {ataque_poke1} de daño, ahora su vida es {vida_poke2}\n')
            turno = 2
        else:
            vida_poke1 -= ataque_poke2
            print(f'\n{pokemon1.nombre} recibio {ataque_poke2}, ahora su vida es {vida_poke1}\n')
            turno = 1
        if vida_poke1 > 0 and vida_poke2 > 0:
            print('====PROXIMA BATALLA=====')
    if vida_poke1 <= 0:
        print()
        pokemon2.gano()
    else:
        print()
        pokemon1.gano()
    print('Quieres jugar de nuevo?')
    respuesta = input('>').lower()
    while respuesta != 'si' and respuesta != 'no':
        print('Respuesta invalida, por favor ingresa si o no:')
        respuesta = input('>').lower()
    if respuesta == 'no':
        print('Muchas gracias por jugar!')
        break
    else:
        turno = tirar_dado(2)
