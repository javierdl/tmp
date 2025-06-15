import sqlite3

DB_FILE = "escueladb.db"

def cargar_curso(): #pide el nombre como input
    nombre = input("Nombre del nuevo curso: ")
    return nombre

def agregar_curso(nombre): #dandole el nombre como str lo inserta en la tabla curso
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO curso (nombre) VALUES (?)",
        (nombre,)
    )
    conn.commit()
    conn.close()

def listar_cursos(): #devuelve todos los cursos en tabla curso como una lista de tuplas
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso")
    #traer.fetchall()
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_curso_id(id_curso): #devuelve el curso del ID(Parametro) como una tupla
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso WHERE id_curso = (?)",(id_curso,))
    vuelta = traer.fetchone()
    conn.commit()
    conn.close()
    return vuelta

def listar_curso_nombre(nombre): #devuelve el curso del nombre(Parametro) como una lista de tuplas con todos los cursos con ese nombre
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso WHERE nombre = (?)",(nombre,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta
