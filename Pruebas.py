
"""TABLA Curso-------------------------------------------------------------------------------------------------------"""

import CursoFun

#Agregar curso
"""a=CursoFun.cargar_curso() #cargacurso
CursoFun.agregar_curso(a)""" #agrega curso a la tabla

#listar cursos
"""vuelta=CursoFun.listar_cursos() #lista todos los cursos en la tabla
print(vuelta)

print(CursoFun.listar_cursos())""" #se puede hacer directo sin variable tmb

#por nombre

"""a=input("nombre curso: ")
vuelta=CursoFun.listar_curso_nombre(a) #ingresa nombre de curso y devuelve un listado con todos los que tengan ese nombre y sus datos en tuplas
print(vuelta)"""

#por id

"""a=int(input("id curso: "))
vuelta=CursoFun.listar_curso_id(a) #ingresa ID de curso y devuelve sus datos en tupla
print(vuelta)"""

"""TABLA Materia-------------------------------------------------------------------------------------------------------"""

import MateriaFun
#cargar materia con inputs
"""a = MateriaFun.cargar_materia()"""

#subir/agregar materia a la base de datos en Tabla Materia
"""MateriaFun.agregar_materia(a[0], a[1])"""

#listar materias cargadas
"""print(MateriaFun.listar_materias())"""


"""TABLA Profesor-------------------------------------------------------------------------------------------------------"""

import ProfesorFun

#carga datos de profe
"""prof_inputDatos_lista = ProfesorFun.cargar_profesor()
print(prof_inputDatos_lista)"""

#agrega profe a la base de datos con la lista de carga como parametros
"""ProfesorFun.agregar_profesor(prof_inputDatos_lista[0], prof_inputDatos_lista[1], prof_inputDatos_lista[2], prof_inputDatos_lista[3])"""

#imprime listado de profes en tabla profe
"""print(ProfesorFun.listar_profesores())"""

#listar materias que da un profe
"""a=int(input("ingrese ID de profe que quiera ver materias: "))
b=ProfesorFun.listar_sus_materias(a)
print(b)"""

#encontrar profe por ID
"""a=int(input("ingrese ID de profe que quiera ver: "))
b=ProfesorFun.listar_profesor_id(a)
print(b)"""

#encontrar profe por apellido
"""a=(input("ingrese APELLIDO de profe que quiera ver: "))
b=ProfesorFun.listar_profesores_apellido(a)
print(b)"""

#encontrar profe por nombre
"""a=(input("ingrese NOMBRE de profe que quiera ver: "))
b=ProfesorFun.listar_profesores_nombre(a)
print(b)"""

"""TABLA CursoMateria-------------------------------------------------------------------------------------------------------"""

import CursoMateriaFun

#cargar relacion curso materia
"""a = CursoMateriaFun.cargar_curso_materia()"""

#agregar relacion curso materia
"""CursoMateriaFun.agregar_curso_materia(a[0], a[1])"""

#listar cursos materias
"""print(CursoMateriaFun.listar_cursos_materias())"""

#listar materias del curso
"""a=int(input("idcurso: "))
print(CursoMateriaFun.listar_materias_from_curso(a))"""

#listar left joinn con Curso y Materia
"""print(CursoFun.listar_cursos())
curso=int(input("idcurso: "))
print(CursoMateriaFun.listar_lefjoin_curso(curso))"""

#listar left joinn con Curso y Materia Solo nombres*
"""print(CursoFun.listar_cursos())
curso=int(input("idcurso: "))
print(CursoMateriaFun.listar_lefjoin_curso_nombre(curso))"""

"""TABLA Alumno-------------------------------------------------------------------------------------------------------"""

import AlumnoFun

#cargar alumno
"""a = AlumnoFun.cargar_alumno()"""

#agregar alumno
"""AlumnoFun.agregar_alumno(a[0],a[1],a[2],a[3])"""

#listar alumnos
"""print(AlumnoFun.listar_alumnos())"""

#listar alumno por id
"""print(AlumnoFun.listar_alumno_id(1))"""

#lista alumnos con apellido
"""print(AlumnoFun.listar_alumnos_apellido("Gata"))"""

#lista alumnos con nombre
"""print(AlumnoFun.listar_alumnos_nombre("Javier"))"""

#lista alumnos con dni
"""print(AlumnoFun.listar_alumnos_dni(11222333))"""

#menu para buscar alumno:
"""AlumnoFun.buscar_alumno()"""

#Eliminar alumno
"""id_eliminado = int(input("Ingrese ID del usuario a eliminar: "))
AlumnoFun.borrar_alumno(id_eliminado)"""

"""TABLA AlumnoMateria-------------------------------------------------------------------------------------------------------"""

import AlumnoMateriaFun

#Con el ID de un alumno ya cargado, relacionarlo a traves de su curso con todas las materias para tener una lista de relaciones
"""lista_tuplas = AlumnoMateriaFun.cargar_alumno_materias()
print(lista_tuplas)"""

 #con es a lista de tuplas relacionales, cargar todas las materias, se cortas si hay un error:
"""AlumnoMateriaFun.agregar_alumno_todas_materias(lista_tuplas)"""

#con un ID alumno y un ID materia, los relaciona individual y manualmente
"""AlumnoMateriaFun.agregar_alumno_materia(id_alumno, id_materia)"""

#Lista todas las relaciones alumnos mateerias que hay [(1,2,3)(2,1,4)] 1 = PK tabla, 2 = id_alumno 3 = id_materia
"""print(AlumnoMateriaFun.listar_alumnos_materias())"""



"""LISTADOS DE TABLAS------------------------------------------------------------------------------------------------------"""

print("CURSOS:")
print(CursoFun.listar_cursos())

print("Alumnos:")
print(AlumnoFun.listar_alumnos())

print("Profesores:")
print(ProfesorFun.listar_profesores())

print("Materias:")
print(MateriaFun.listar_materias())

print("relación de cursos y materias:")
print(CursoMateriaFun.listar_cursos_materias())
cursos=(CursoFun.listar_cursos())
for i in cursos:
    id_curso= i[0]
    print(CursoMateriaFun.listar_lefjoin_curso_nombre(id_curso))

print("Alumnos_Materias: ")
print(AlumnoMateriaFun.listar_alumnos_materias())







import sqlite3
DB_FILE = "escueladb.db"

def borrar_tabla(Nombre_tabla):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DROP TABLE profesor")
    print("tabla borrada")
    conn.commit()
    conn.close()

