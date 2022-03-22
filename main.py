from Ej1 import Docente, Alumno, SistemaGC, Curso

fer = Docente("Fer")
dinhos = Docente("Dinhos")
lio = Docente("Lio")
Cris = Alumno("Cris")
Juan = Alumno("Juan")
Pedro = Alumno("Pedro")
Daniel = Alumno("Daniel")

print(Docente.docentes)


informatica = SistemaGC("id1")
informatica.vincularDocente("Fer")
matematica = SistemaGC("id2")
print(SistemaGC.cursos)
print(SistemaGC.cursosTomados)
print(Docente.cantidadDeCursosTomados)
print(Docente.getsalary(fer))
informatica.agregarAlumnos("Juan")
matematica.agregarAlumnos("Juan")
print(Alumno.alumnos_p_curso)
print(Alumno.paga(Juan))
