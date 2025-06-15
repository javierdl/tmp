import sqlite3

DB_FILE = "escueladb.db"

def crear_tablas():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    #"""administrativo"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS administrativo (
        id_admin INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        dni INTEGER,
        usuario TEXT,
        clave TEXT
    )
    """)

    #"""profesor"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profesor (
        id_profesor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        dni INTEGER,
        clave INT
    )
    """)

    #"""materia"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materia (
        id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        id_profesor INTEGER,
        FOREIGN KEY (id_profesor) REFERENCES profesor(id_profesor) ON DELETE SET NULL
    )
    """)

    #"""curso"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS curso (
        id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
    )
    """)

    #"""curso_materia"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS curso_materia (
        id_curso INTEGER,
        id_materia INTEGER,
        PRIMARY KEY (id_curso, id_materia),
        FOREIGN KEY (id_curso) REFERENCES curso(id_curso) ON DELETE CASCADE,
        FOREIGN KEY (id_materia) REFERENCES materia(id_materia) ON DELETE CASCADE
    )
    """)

    #"""alumno"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumno (
        id_alumno INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        dni INTEGER,
        id_curso INTEGER,
        FOREIGN KEY (id_curso) REFERENCES curso(id_curso) ON DELETE SET NULL
    )
    """)

    #"""alumno_materia"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumno_materia (
        id_alumno_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        id_alumno INTEGER,
        id_materia INTEGER,
        FOREIGN KEY (id_alumno) REFERENCES alumno(id_alumno) ON DELETE CASCADE, 
        FOREIGN KEY (id_materia) REFERENCES materia(id_materia) ON DELETE SET NULL,
        UNIQUE (id_alumno, id_materia)
    )
    """)

    #"""Notas"""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
        id_alumno_materia INTEGER,
        trimestre INTEGER,
        nota REAL,
        FOREIGN KEY (id_alumno_materia) REFERENCES alumno_Materia(id_alumno_materia) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
    print("Se crearon las Tablas")

crear_tablas()