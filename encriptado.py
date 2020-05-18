
def encriptar2 (frase, caracter_existente, caracter_para_remplazar):
    encriptada = ''
    for letra in frase:
        if letra == caracter_existente:
            encriptada += caracter_para_remplazar
        else:
            encriptada += letra
    return encriptada


def encriptar (frase, caracter1, caracter2, caracter3, caracter4, caracter5):
    encriptada = ''
    for letra in frase:
        if letra.lower() in 'aá':
            if letra.isupper():
                encriptada += caracter1.upper()
            else:
                encriptada = encriptada + caracter1.lower()
        elif letra.lower() in 'eé':
            if letra.isupper():
                encriptada += caracter2.upper()
            else:
                encriptada += caracter2.lower()
        elif letra.lower() in 'ií':
            if letra.isupper():
                encriptada += caracter3.upper()
            else:
                encriptada += caracter3.lower()
        elif letra.lower() in 'oó':
            if letra.isupper():
                encriptada += caracter4.upper()
            else:
                encriptada += caracter4.lower()
        elif letra.lower() in 'uú':
            if letra.isupper():
                encriptada += caracter5.upper()
            else:
                encriptada += caracter5.lower()
        else:
            encriptada += letra
    return encriptada

c1 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra A:\n>')
c2 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra E:\n>')
c3 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra I:\n>')
c4 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra O:\n>')
c5 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra U:\n>')

while True:
    fra = str(input('Por favor, ingresa tu frase:\n>'))
    print(encriptar(fra, c1, c2, c3, c4, c5))
    print()
    print('Quieres encriptar otra frase? Si o no')
    opcion = input('>')
    while opcion.lower() != 'si' and opcion.lower() != 'no':
        print('Respuesta no valida, por favor ingresa si o no')
        opcion = input('>')
    if opcion.lower == 'no':
        print('Muchs gracias!')
        break
    print('Queres cambiar los caracteres?')
    opcion2 = input('>')
    while opcion2.lower() != 'si' and opcion2.lower() != 'no':
        print('Respuesta no valida, por favor ingresa si o no')
        opcion2 = input('>')
    if opcion2 == 'si':
        c1 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra A:\n>')
        c2 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra E:\n>')
        c3 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra I:\n>')
        c4 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra O:\n>')
        c5 = input('Por favor, ingresa la letra por la que quieres reemplazar a la letra U:\n>')

