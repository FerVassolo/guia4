from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

class Docente(Persona):

    docentes = []
    cantidadDeCursosTomados = {}
    salario_p_curso = 10000

    def __init__(self, nombre):
        super().__init__(nombre)
        self.docentes.append(self.nombre)

    def getsalary(self):
        if self.nombre in self.cantidadDeCursosTomados:
            return self.cantidadDeCursosTomados[self.nombre] * self.salario_p_curso


class Alumno(Persona):

    paga_p_curso = 600
    alumnos = []
    alumnos_p_curso = {"Informática Básica": [], "Matemática": [], "Biología": [], "Geografía": []}

    def __init__(self, nombre):
        super().__init__(nombre)
        self.alumnos.append(self.nombre)

    def paga(self):
        pagaInicial = 0
        for curso in self.alumnos_p_curso:
            if self.nombre in self.alumnos_p_curso[curso]:
                pagaInicial += self.paga_p_curso
        return pagaInicial


class Curso:

    cursos = {"id1": "Informática Básica", "id2": "Matemática", "id3": "Biología", "id4": "Geografía"}
    cursosTomados = {}

    def __init__(self, identificador):
        self.identificador = identificador


class SistemaGC(Curso):

    def __init__(self, identificador):
        Curso.__init__(self, identificador)

    def vincularDocente(self, docente):

        if docente in Docente.docentes and Curso.cursos[self.identificador] not in Curso.cursosTomados:
        # dictionary_name[key] = value
             self.cursosTomados[self.cursos[self.identificador]] = docente

        elif docente in Docente.docentes and Curso.cursos[self.identificador] in Curso.cursosTomados:
            return "El curso ya esta tomado"

        else:
            return "Ese docente no existe"


        if docente in Docente.cantidadDeCursosTomados and Docente.cantidadDeCursosTomados[docente] < 3:
            Docente.cantidadDeCursosTomados[docente] += 1
        elif docente not in Docente.cantidadDeCursosTomados:
            Docente.cantidadDeCursosTomados[docente] = 1
        else:
            return "El docente tiene un máximo de cursos tomados"


    def agregarAlumnos(self, alumno):
        if alumno in Alumno.alumnos and alumno not in Alumno.alumnos_p_curso[Curso.cursos[self.identificador]]:
            Alumno.alumnos_p_curso[Curso.cursos[self.identificador]].append(alumno)
        else:
            return "Alumno no existe o Ya esta vinculado al curso"

# la parte del identificador está mal, no es dificil corregir, solo entendí mal la premisa y me da fiaca cambiar
