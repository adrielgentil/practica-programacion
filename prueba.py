
import random

'''
var = 'yvan eht nioj'

list = [e for e in var]

print(list)
list.reverse()
print(list)

newvar = ''
for e in list:
    newvar += e

print(newvar)

print(var[::-1])

'''

'''
myset = set()
myset.add(1)
print(myset)
mylist = (1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4)
myset = set(mylist)
print(myset)
myset2 = {1, 2, 3, 4, 5, 5}
print(myset2)
'''

'''
archivo = open('aaaaa', 'w+')
'''
'''
print(4 ** (1/2))
'''
'''
list = [1, 2, [3, 4, 'hello']]
list[2][2] = 'goodby'
print(list)


d = {
    'k1': [1, 2, {'k2': ['this is tricky', {'though': [1, 2, 'hello']}]}]
}

print(d['k1'][2]['k2'][1]['though'][2])
'''

'''
frase_original = 'Print only the words that start with s in this sentence'

listafrase = frase_original.split()
print(listafrase)

for palabra in listafrase:
    if palabra[0].lower() == 's' and len(palabra) > 1:
        print(palabra)
'''


'''
for num in range(1,11):
    if num % 2 == 0:
        print(num)

'''

'''

mynum = [num for num in range(1, 50) if num % 3 == 0]
print(mynum)

'''
'''
storiginal = 'Print every word in this sentence that has an even number of letters'
stspliteado = storiginal.split()

for palabra in stspliteado:
    if len(palabra) % 2 == 0:
        print(f'{palabra}: EVEN')
    else:
        print(f'{palabra}: ODD')
'''

'''
for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num}: FizzBuzz')
    elif num % 5 == 0:
        print(f'{num}: Buzz')
    elif num % 3 == 0:
        print(f'{num}: Fizz')
    else:
        print(f'{num}: -')
'''
'''
frase = 'Create a list of the first letters of every word in this string'


first_letter = [palabra[0] for palabra in frase.split()]
print(first_letter)
'''

'''
def hola (pais, *arg, **kwargs1):
    print(f'Hola {arg[1]}, tienes {kwargs1[arg[1]]}, y eres de {pais}.')

hola('Latinoamerica', 'Adriel', 'Luciana', 'Jose', Adriel = 27, Luciana = 26, Jose = 30)
'''

'''
def lesser_of_two_evens(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return min(x, y)
    else:
        return max(x, y)

n1 = random.randint(0, 1000)
n2 = random.randint(0, 1000)
print(n1, n2)
print(lesser_of_two_evens(n1, n2))
'''
'''
def animal_craker(frase):
    palabra1 = frase.split()[0]
    palabra2 = frase.split()[1]
    return palabra1[0].lower() == palabra2[0].lower()

print(animal_craker('Falda fea'))
'''
'''
def old_macdonald(nombre):
    nombrenuevo = ''
    for l in nombre:
        if l == nombre[0] or l == nombre[3]:
            nombrenuevo += l.capitalize()
        else:
            nombrenuevo += l
    return nombrenuevo

print(old_macdonald('macgonagan'))
'''
'''
def master_yoda(frase):
    fraselista = frase.split()
    fraselista.reverse()
    fraseyoda = ' '.join(fraselista)
    return fraseyoda
'''
'''
    fraseyoda = ''
    for palabra in fraselista:
        fraseyoda += palabra + ' '
    return fraseyoda

print(master_yoda('I am home'))
'''
'''
def almost_there(n):
   return n in range(90, 111) or n in range(190, 211)

print(almost_there(111))
'''
'''
def contar(patron, texto):
    return texto.count(patron)

print(contar('ja', 'jajajajajajajajajajajajajajajjaaajajajja'))
'''
'''
def repetir(texto):
    nuevotexto = ''
    for palabra in texto:
        nuevotexto += palabra * 3
    return nuevotexto

print(repetir('hola'))
'''

'''
def black_jack(n1, n2, n3):
    suma = n1 + n2 + n3
    if suma <= 21:
        return suma
    else:
        if n1 == 11 or n2 == 11 or n3 == 11:
            suma -= 10
            if suma <=21:
                return suma
            else:
                return 'BUSTED'
        else:
            return 'BUSTED'

num1 = random.randint(1, 11)
print(num1)
num2 = random.randint(1, 11)
print(num2)
num3 = random.randint(1, 11)
print(num3, '\n')



print(black_jack(num1, num2, num3))
'''
'''
import math
pi = math.pi


def vol(rad):
    volumen = (4 / 3) * pi * (rad ** 3)
    return volumen
print(vol(1))
'''
'''
def ran_check(num, inferior, sup):
    if num in range(inferior, sup+1):
        return 'It is'
    else:
        return 'It is not'

def ran_bool(num, inferior, sup):
    return num in range(inferior, sup+1)

print(ran_check(5, 10, 100))
print(ran_bool(11, 1, 10))
'''
'''
frase = 'Me llamo Adriel Gentil y vivo en la ciudad de Wilde, Avellaneda'

def up_low(oracion):
    low = 0
    up = 0
    totalletras = 0
    oracion2 = oracion.split()
    print(oracion2)
    for palabra in oracion2:
        for letra in palabra:
            if letra == letra.upper():
                up += 1
                totalletras += 1
            elif letra == letra.lower():
                low += 1
                totalletras += 1
    return f'Hay {up} letras mayuscula, y {low} letras minusculas, de un total de {totalletras} letras'

print(up_low(frase))
'''
'''
lista = [1, 1, 2, 2, 2, 3, 4, 4, 5]


def unique_list(a):
    newlist = set(a)
    return newlist

print(unique_list(lista))

import string

def pengram(oracion):
    alfabeto = list(string.ascii_lowercase)
    oracion2 = set(oracion.lower())
    oracion3 = [elem for elem in oracion2]
    oracion3.sort()
    for letra in oracion3:
        if letra in alfabeto:
            alfabeto.pop(0)
        print(letra)
        print(alfabeto)
    if len(alfabeto) > 0:
        print('Esta palabra no es pengram')
    else:
        print('Esta palabra es pengram')


pengram('The quick yellow fox jumps over the lazy dog')

'''
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('TypeError\n')

x = 5
y = 0

try:
     z = x/y
     print(z)
except ZeroDivisionError:
    print('No se puede dividir por 0')
finally:
    print('Todo listo\n')


while True:
    try:
        x = int(input('Porfavor ingrese un numero:\n>'))
        print(x ** 2)
    except TypeError:
        print('Input invalido, solo se aceptan caracteres numericos')
    else:
        print('Proceso terminado')
        break


