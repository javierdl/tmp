import sqlite3

DB_FILE = "escueladb.db"

def input_ent(prompt): #valida que sea un entero el input
    while True:
        entrada = input(prompt)
        try:
            int_entrada = int(entrada)
            return int_entrada
        except ValueError:
            print("Por favor, ingrese un número válido")

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

def input_largo(prompt, largomin, largomax): #valida el largo de un input entre parametros min(2) y maximos(3)
    while True:
        entrada = input(prompt)
        print(f"(debe tener entre {largomin} y {largomax} caracteres): ")
        if largomin <= len(entrada.strip()) <= largomax:
            return entrada
        elif len(entrada.strip()) < largomin:
            print(f"Cantidad de caracteres errónea: Demasiado corto. Mínimo:{largomin}")
        else:
            print(f"Cantidad de caracteres errónea: Demasiado largo. Máximo:{largomax}")

def input_dni(prompt="Ingrese DNI (sin puntos ni espacios): "): #valida que un dni sea aceptable
    while True:
        entrada = input(prompt)
        if not entrada.isdigit():
            print("El DNI debe contener solo números.")
            continue
        if len(entrada) != 8:
            print("El DNI debe tener exactamente 8 dígitos.")
            continue
        dni = int(entrada)
        return dni

def input_nombre(prompt="Ingrese su nombre (sin espacios): "): #valida que un nombre sea aceptable
    while True:
        entrada = input(prompt).strip()
        if not entrada.isalnum():
            print("El nombre NO debe contener caracteres especiales")
            continue            
        if any(letra.isdigit() for letra in entrada):
            print("El nombre NO debe contener números")
            continue
        if not (1 <= len(entrada.strip()) <= 20):
            print("El Nombre debe tener entre 1 y 20 caracteres")
            continue
        nombre = entrada.capitalize()
        return nombre

def input_apellido(prompt="Ingrese su apellido: "): #valida que un apellido sea aceptable
    while True:
        entrada = input(prompt).strip()
        if any(letra.isdigit() for letra in entrada):
            print("El apellido NO debe contener números")
            continue
        if not (1 <= len(entrada.strip()) <= 20):
            print("El apellido debe tener entre 1 y 20 caracteres")
            continue
        if not entrada.isalnum():
            if any(letra == " " for letra in entrada.strip()):
                nombre = entrada.title()
                return nombre
            else:
                print("El apellido SOLO puede contener letras")
                continue 
        nombre = entrada.capitalize()
        return nombre

def existe_en_tabla(tabla, columna, valor): #Valida si en esa tabla(1) y columna(2) existe un registro con ese valor(3)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    consulta = f"SELECT * FROM {tabla} WHERE {columna} = ?"
    cur.execute(consulta, (valor,))
    resultado = cur.fetchone()
    conn.close()
    if resultado == None:
        return False
    else:
        return resultado
