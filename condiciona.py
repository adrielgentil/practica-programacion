'''
sos_alto = True
sos_gordo = False
sos_narigon = True


if sos_alto or sos_gordo or sos_narigon:
    print('Sos alto, gordo y narigon')
elif not sos_alto and sos_gordo and sos_narigon:
    print('No eres alto, pero eres gordo y narigon')
elif not sos_alto and not sos_gordo and sos_narigon:
    print('No sos alto, pero sos flaco y narigon')
elif sos_alto and not sos_gordo and sos_narigon:
    print('Eres alto, flaco y narigon')
elif sos_alto and not sos_gordo and not sos_narigon:
    print('Sos alto, flaco y no narigon')
elif sos_alto and sos_gordo and not sos_narigon:
    print('Sos algo, gorno y no narigon')
else:
    print('No sos ni alto ni gordo ni narigon')
'''


def mayor_numero (n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

a = input('Ingresa numero: ')
b = input('Ingresa otro numero: ')
c = input('Ingresa otro numero: ')

print(mayor_numero(a, b, c))





