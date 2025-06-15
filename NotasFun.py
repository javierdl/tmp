import sqlite3
import AlumnoFun
import AlumnoMateriaFun
import Validar

DB_FILE = "escueladb.db"

# def listar_notas_alumno()
# def listar_notas_alumno_materia()
# def listar_notas_trimestre()
# def listar_notas_trimestre_alumno()

def listar_notas():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM notas")
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def cargar_nota():
    vuelta = []
    id_alumno = Validar.input_ent("Ingrese el ID del alumno: ")
    existe = AlumnoFun.existe_alumno_id(id_alumno)
    if existe == False:
        print("ID de alumno incorrecto o alumno inexitente")
        return False
    nombre_materias = AlumnoMateriaFun.listar_nombre_materias_de_alumno(id_alumno)
    id_materias = AlumnoMateriaFun.listar_id_materias_de_alumno(id_alumno)
    if len(id_materias) > 0:
        print(id_materias)
        cont = 0
        print("Seleccione la materia que desea cargar en el alumno")
        for i in nombre_materias:
            cont += 1
            print(f"{cont}) {i[0]}")
        elegida = Validar.input_opcion("Seleccione el numero de la materia",len(nombre_materias))
        if elegida == 1:
            print("eligio1")
        elif elegida == 2: 
            print("eligio2")
        elif elegida == 3:
            print("eligio3")
        elif elegida == 4:
            print("eligio4")
        elif elegida == 5:
            print("eligio5")
        # id_alumno_materia = input("id_alumno_materia: ")
        # trismestre = input("trimestre: ")
        # nota = input("nota: ")
        # vuelta.append(id_alumno_materia)
        # vuelta.append(trismestre)
        # vuelta.append(nota)
        # return vuelta
    else:
        print("El alumno no tiene materias asociadas")

cargar_nota()


def agregar_nota(id_alumno_materia, trismestre, nota):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notas (id_alumno_materia, trimestre, nota) VALUES (?, ?, ?)",
        (id_alumno_materia, trismestre, nota)
    )
    conn.commit()
    conn.close()

"""a = cargar_nota()
agregar_nota(a[0],a[1],a[2])
print(listar_notas())"""