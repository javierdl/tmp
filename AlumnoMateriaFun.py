import sqlite3
import AlumnoFun
import MateriaFun
import CursoMateriaFun
import Validar

DB_FILE = "escueladb.db"

def cargar_alumno_materias(): #ingresando el ID alumno, busca su curso y devuelve todas las materias parejadas con el ID alumno en lista de tuplas.
    print("Recuerde haber cargado antes al alumno")
    id_alumno = Validar.input_ent("Ingrese el ID del alumno que quiere anotar en materias: ")
    AlumnoFun.existe_alumno_id(id_alumno)
    alumno = AlumnoFun.listar_alumno_id(id_alumno)
    #print(alumno)
    id_curso = alumno[4]
    materias = CursoMateriaFun.listar_materias_from_curso(id_curso)
    #print(materias)
    vuelta = []
    contador = 0
    for i in materias: #materias[0][1] = id_materia1 y materias[1][1] = id_materia2 ... etc ... materias[5][1] = id_materia5
        tupla = (id_alumno,materias[contador][1])
        #print(tupla)
        vuelta.append(tupla)
        contador += 1
    #print(vuelta)
    return vuelta #es una lista con tuplas aparejadas [(1,2),(1,3),etc] donde el primer num es el id_alumno y el segundo el Id_materia


"""antigua"""
# def agregar_alumno_materia(id_alumno, id_materia): #agrega individualmente una relacion en la tabla alumno-materia
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO alumno_materia (id_alumno, id_materia) VALUES (?, ?)",
#         (id_alumno, id_materia)
#         )
#     conn.commit()
#     conn.close()

def agregar_alumno_materia(id_alumno, id_materia): #agrega individualmente una relacion en la tabla alumno-materia
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    alumno = AlumnoFun.listar_alumno_id(id_alumno)
    materia = MateriaFun.listar_materia_id(id_materia)
    try:
        cursor.execute(
            "INSERT INTO alumno_materia (id_alumno, id_materia) VALUES (?, ?)",
            (id_alumno, id_materia)
            )
        return True
    except sqlite3.IntegrityError:
        print(f"Ya existe registro de alumno {alumno[1]} {alumno[2]} y materia {materia[1]}")
        return False
    conn.commit()
    conn.close()

def agregar_alumno_todas_materias(lista_tuplas_alumno_materia): #agrega todas las relaciones en la tabla alumno-materia con lista de tuplas relacional como parametro
    conn = sqlite3.connect(DB_FILE)
    relaciones = lista_tuplas_alumno_materia
    check = 0
    for id_alumno, id_materia in relaciones:
        agregar = agregar_alumno_materia(id_alumno, id_materia)
        if agregar == True:
            check += 1
        else:
            break
    conn.commit()
    conn.close()
    if check == len(relaciones):
        print("alumno y materias relacionados correctamente")
    else:
        print("Hubo un error por favor revise los registros y cargue manualmente las materias de este alumno")

def listar_alumnos_materias(): #lista todos los alumnos materias
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno_materia")
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_materias_de_alumno(id_alumno): #lista todos los alumnos materias
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno_materia WHERE id_alumno = (?)",(id_alumno,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_nombre_materias_de_alumno(id_alumno): #lista todos los alumnos materias
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT nombre FROM materia as m LEFT JOIN alumno_materia as am ON m.id_materia = am.id_materia WHERE am.id_alumno = (?)",(id_alumno,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_id_materias_de_alumno(id_alumno): #lista todos los alumnos materias
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT am.id_materia FROM alumno_materia as am WHERE am.id_alumno = (?)",(id_alumno,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta
