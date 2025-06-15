import sqlite3
import CursoFun
import Validar

DB_FILE = "escueladb.db"

def existe_alumno_id(id_alumno): #valida si existe alumno con ese id
    intentos = 3
    while True:
        if Validar.existe_en_tabla("alumno","id_alumno",id_alumno) != False:
            #print(listar_alumno_id(id_alumno))
            return listar_alumno_id(id_alumno)
        else:
            print("No existe alumno con ese ID")
            intentos -=1
            print(f"quedan {intentos+1} intento/s")
            id_alumno = Validar.input_ent("Ingrese un ID de alumno válido: ")
            if intentos == 0:
                return False
            continue

def cargar_alumno(): #Permite la carga manual de los datos para un nuevo alumno, tambien los valida con import Validar
    vuelta = []
    nombre = Validar.input_nombre()
    apellido = Validar.input_apellido()
    dni = Validar.input_dni()
    print(CursoFun.listar_cursos())
    while True:
        entrada_curso = Validar.input_ent("seleccione el ID del curso al que ingresa el alumno: ")
        existe = Validar.existe_en_tabla("curso","id_curso",entrada_curso)
        if existe == False:
            continue
        else:
            break
    vuelta.append(nombre)
    vuelta.append(apellido)
    vuelta.append(dni)
    vuelta.append(entrada_curso)
    print(vuelta)
    return vuelta

def agregar_alumno(nombre, apellido, dni, id_curso): #Agrega alumno a tabla alumno, requiere los parametros correctos
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO alumno (nombre, apellido, dni, id_curso) VALUES (?, ?, ?, ?)",
        (nombre, apellido, dni, id_curso)
    )
    conn.commit()
    conn.close()

def listar_alumnos(): #lista todos los alumnos
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno")
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_alumnos_curso(id_curso): #lista todos los alumnos de un curso con su ID(1)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno WHERE id_curso = (?)",(id_curso,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_alumno_id(id_alumno): #Trae una tupla del unico alumno con el ID(1)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno WHERE id_alumno = (?)",(id_alumno,))
    vuelta = traer.fetchone()
    conn.commit()
    conn.close()
    return vuelta

def listar_alumno_idall(id_alumno): #lista a un solo alumno con el ID, trae una lista de una sola tupla con datos registro
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno WHERE id_alumno = (?)",(id_alumno,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_alumnos_apellido(apellido): #lista todos los alumnos con el apellido(1)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno WHERE apellido = (?)",(apellido,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_alumnos_nombre(nombre): #lista todos los alumnos con el nombre(1)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno WHERE nombre = (?)",(nombre,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_alumnos_dni(dni): #lista todos los alumnos con el dni(1)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM alumno WHERE dni = (?)",(dni,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def borrar_alumno(id_alumno): #borra alumno con su ID(1) y todos sus registros relacionados con FK
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM alumno WHERE id_alumno = (?)", (id_alumno,))
    alumno = cur.fetchone()
    cur.execute("SELECT nombre FROM curso WHERE id_curso = (?)", (alumno[4],))
    curso = cur.fetchone()
    if not alumno:
        print("Error, el alumno no existe")
    else: 
        print("¿Seguro que quiere eliminar al alumno: ")
        print(f"{alumno[1]} {alumno[2]} DNI: {alumno[3]} del curso: {curso[0]}")
        print("y todos sus registros?")
        check = Validar.input_opcion("Ingrese: \n1) para Confirmar  \n2) para cancelar",2)
        if check == 1:
            cur.execute("DELETE FROM alumno WHERE id_alumno = (?)", (id_alumno,))
            conn.commit()
            print("Alumno eliminado")
        else:
            print("Eliminación cancelada")
    conn.close()

def input_opcion(prompt, cantidad_opciones): #valida que el input de eleccion sea un numero entre las opciones(2) posibles
    while True:
        entrada = input(f"{prompt} \n(1 a {cantidad_opciones}): ")
        try:
            opcion = int(entrada)
            if 1 <= opcion <= cantidad_opciones:
                return opcion
            else:
                print(f"Por favor, ingrese un número entre 1 y {cantidad_opciones}.")
        except ValueError:
            print("Por favor, ingresar un número entero válido.")

def buscar_alumno(): #menu de busqueda de alumnos con cualquier dato
    print("¿Sabe el ID del alumno? Ingrese: ")
    sabe_id = Validar.input_opcion("1) Para SI \n2) Para NO \n3) Para SALIR",3)
    if sabe_id == 1:
        while True:
            id_alumno = Validar.input_ent("ingrese el ID del alumno: ")
            if Validar.existe_en_tabla("alumno","id_alumno",id_alumno) != False:
                #print(listar_alumno_idall(id_alumno))
                return listar_alumno_idall(id_alumno)
            else:
                print("No existe alumno con ese ID")
                continue
    elif sabe_id == 2:
        buscar_al = Validar.input_opcion("Como quiere buscar al alumno:\n1)Listado completo de alumnos\n2)Por Nombre del alumno\n3)Por Apellido del alumno\n4)Por DNI del alumno \n5)Para SALIR.",5)
        if buscar_al == 1:
            print(listar_alumnos())
            return listar_alumnos()
        elif buscar_al == 2:
            while True:
                nombre = Validar.input_nombre("ingrese el nombre del alumno: ")
                if Validar.existe_en_tabla("alumno","nombre",nombre) != False:
                    print(listar_alumnos_nombre(nombre))
                    return listar_alumnos_nombre(nombre)
                else:
                    print("No existe alumno con ese nombre")
                    continue
        elif buscar_al == 3:
            while True:
                apellido = Validar.input_apellido("ingrese el apellido del alumno: ")
                if Validar.existe_en_tabla("alumno","apellido",apellido) != False:
                    print(listar_alumnos_apellido(apellido))
                    return listar_alumnos_apellido(apellido)
                else:
                    print("No existe alumno con ese apellido")
                    continue
        elif buscar_al == 4:
            while True:
                dni = Validar.input_dni("ingrese el DNI del alumno: ")
                if Validar.existe_en_tabla("alumno","dni",dni) != False:
                    print(listar_alumnos_dni(dni))
                    return listar_alumnos_dni(dni)
                else:
                    print("No existe alumno con ese DNI")
                    continue
    else:
        salir = True
        print("Salir")
        return salir
