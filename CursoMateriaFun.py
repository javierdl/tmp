import sqlite3
import CursoFun
import MateriaFun

DB_FILE = "escueladb.db"

def cargar_curso_materia():
    vuelta = []
    print(CursoFun.listar_cursos())
    id_curso = input("id del curso: ")
    print(MateriaFun.listar_materias())
    id_materia = int(input("ID de la Materia que estara en ese curso: "))
    vuelta.append(id_curso)
    vuelta.append(id_materia)
    #print(vuelta)
    return vuelta #vuelta[0] = id_curso(curso) y vuelta[1] = id_materia(materia)

def agregar_curso_materia(id_curso, id_materia):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO curso_materia (id_curso, id_materia) VALUES (?, ?)",
        (id_curso, id_materia)
        )
    conn.commit()
    conn.close()

def listar_cursos_materias():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso_materia")
    #traer.fetchall()
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta   

def listar_cursos_from_materia(id_materia):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    traer = cursor.execute("SELECT * FROM curso_materia WHERE id_materia = (?)",(id_materia,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_materias_from_curso(id_curso):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    traer = cursor.execute("SELECT * FROM curso_materia WHERE id_curso = (?)",(id_curso,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_lefjoin_curso(id_curso):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    traer = cursor.execute("SELECT * FROM curso AS c LEFT JOIN curso_materia AS cm ON c.id_curso = cm.id_curso LEFT JOIN materia AS m ON cm.id_materia = m.id_materia WHERE c.id_curso = (?)",(id_curso,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_lefjoin_curso_nombre(id_curso):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    traer = cursor.execute("SELECT c.nombre, m.nombre FROM curso AS c LEFT JOIN curso_materia AS cm ON c.id_curso = cm.id_curso LEFT JOIN materia AS m ON cm.id_materia = m.id_materia WHERE c.id_curso = (?)",(id_curso,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta