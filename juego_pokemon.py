import random
import pickle
from Clases import Pokemon as P

def tirar_dado(valor):
    return random.randint(1, valor)

class ListaPokemones:
    listapoke = []

    def __init__(self):
        archivopoke = open('lista_pokemones', 'ab+')
        archivopoke.seek(0)

        try:
            self.listapoke = pickle.load(archivopoke)
            print('Tabla de resultados cargada exitosamente')
        except EOFError:
            print('No hay una tabla de resultados disponible')
        finally:
            archivopoke.close()
            del archivopoke

    def agregarPokemon(self, p):
        self.listapoke.append(p)
        self.guardarPokemones()

    def guardarPokemones(self):
        lista = open('lista_pokemones', "wb")
        pickle.dump(self.listapoke, lista)
        lista.close()
        del lista

    def mostrarPokemones(self):
        for p in self.listapoke:
            print(p)


lista = ListaPokemones()

lista.mostrarPokemones()

turno = tirar_dado(2)

while True:
    pokemon1 = None
    pokemon2 = None
    print('\nJugador 1, ¿Qué pokemon quieres usar?')
    p1 = input('>').capitalize()
    while pokemon1 is None:
        for pokemon in lista.listapoke:
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
        for pokemon in lista.listapoke:
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
        pokemon2.victorias += 1
        print(pokemon2)
        lista.guardarPokemones()
    else:
        print()
        pokemon1.gano()
        pokemon1.victorias += 1
        print(pokemon1)
        lista.guardarPokemones()
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

lista.mostrarPokemones()
