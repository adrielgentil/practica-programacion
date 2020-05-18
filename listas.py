
fruta = ['Manzana', 'Naranja', 'Uva', 'Pera', 'Banana', 'Mandarina']

fruta.insert(1, 'Anana')

print(fruta)

print(len(fruta))

print(fruta.index('Mandarina'))

fruta2 = fruta.copy()

print(fruta2)

fruta2.reverse()
print(fruta2)
fruta2.insert(4, 6)

print(fruta2)
fruta.remove('Pera')
print(fruta2)
print(fruta)

print(fruta.count(fruta))
print(fruta2.count(fruta))