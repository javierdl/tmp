import sqlite3
import Validar

DB_FILE = "escueladb.db"

def cargar_profesor(): #acepta datos como input
    vuelta = []
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = int(input("DNI: "))
    clave = int(input("Clave: "))
    vuelta.append(nombre)
    vuelta.append(apellido)
    vuelta.append(dni)
    vuelta.append(clave)
    #print(vuelta)
    return vuelta #vuelta[0] = nombre(prof.) / vuelta[1] = apellido(prof.) / vuelta[2] = dni(prof.) int / vuelta[3] = clave(prof.)


def agregar_profesor(nombre, apellido, dni, clave): #carga los datos en la base de datos
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO profesor (nombre, apellido, dni, clave) VALUES (?, ?, ?, ?)",
        (nombre, apellido, dni, clave)
    )
    conn.commit()
    conn.close()

def listar_profesores():  #devuelve todos los profesores en tabla Profesor como una lista de tuplas
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor")
    #traer.fetchall()
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_sus_materias(id_profesor): #ingresando ID profe vuelve todas las materias que da
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia WHERE id_profesor = (?)",(id_profesor,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesor_id(id_profesor):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE id_profesor = (?)",(id_profesor,))
    vuelta = traer.fetchone()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesores_apellido(apellido):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE apellido = (?)",(apellido,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesores_nombre(nombre):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE nombre = (?)",(nombre,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesores_dni(dni):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE dni = (?)",(dni,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta
