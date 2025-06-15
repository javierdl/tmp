import sqlite3
import ProfesorFun

DB_FILE = "escueladb.db"

def cargar_materia(): #pide el nombre como input el nombre de materia y ID profesor
    vuelta = []
    nombre = input("Nombre de la Materia: ")
    print(ProfesorFun.listar_profesores())
    id_profesor = int(input("ID del profesor a cargo: "))
    vuelta.append(nombre)
    vuelta.append(id_profesor)
    #print(vuelta)
    return vuelta #vuelta[0] = nombre(materia) y vuelta[1] = id_profesor

def agregar_materia(nombre, id_profesor): #agrega materias con nombre(materia) y ID del profesor a cargo (id_profesor)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO materia (nombre, id_profesor) VALUES (?, ?)",
        (nombre, id_profesor)
    )
    conn.commit()
    conn.close()

def listar_materias(): #lista todas las materias
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia")
    #traer.fetchall()
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_materia_id(id_materia): #lista toda las materia con ID
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia WHERE id_materia = (?)",(id_materia,))
    vuelta = traer.fetchone()
    #traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta
