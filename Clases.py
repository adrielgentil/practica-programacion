class Pokemon:
    def __init__(self, nombre, ataque, vida, tipo, victorias):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.tipo = tipo
        self.victorias = victorias

    def gano(self):
        print(f'{self.nombre} ha ganado!!!\n')

    def __str__(self):
        return f'{self.nombre} lleva {self.victorias} batallas ganadas'