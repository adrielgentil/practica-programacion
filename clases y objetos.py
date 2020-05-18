

class Estudiante:
    def __init__(self, nombre, apellido, edad, cursos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cursos = cursos
        self.esta_activo = True


    def agregar_curso(self):
        nuevo_curso = input('Que curso quieres agregar?:\n>').capitalize()
        if nuevo_curso not in self.cursos:
            self.cursos.append(nuevo_curso)


    def eliminar_curso(self):
        curso_eliminado = input('Que curso quieres eliminar?:\n>').capitalize()
        if curso_eliminado in self.cursos:
            self.cursos.remove(curso_eliminado)






estudiante1 = Estudiante('Adriel', 27, ['Python'])
estudiante2 = Estudiante('Luciana', 26, ['JavaScript'])
estudiante3 = Estudiante('Daniel', 25, ['Java'])

print(estudiante1.cursos)

estudiante1.agregar_curso()

print(estudiante1.cursos)

estudiante1.eliminar_curso()

print(estudiante1.cursos)




