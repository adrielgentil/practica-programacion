
import random



def gencuadrados(n):
    for num in range(n):
        yield num ** 2

generator = gencuadrados(11)

print(next(generator))



def rand_num(min, max, n):
    random.randint(min, max)