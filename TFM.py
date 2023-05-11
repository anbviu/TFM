class Experimento:
    def __init__(self, operador, instrumento, fechacomp, fecha, idexperimento):
        self.operador = operador
        self.instrumento = instrumento
        self.fecha = fecha
        self.fechacomp = fechacomp
        self.idexperimento = idexperimento

class Medida:
    def __init__(self, parametro, intensidad, longitud, idmedida, idexperimento):
        self.parametro = parametro
        self.intensidad = intensidad
        self.longitud = longitud
        self.idmedida = idmedida
        self.idexperimento = idexperimento

#Q1-Consulta 1: de las medidas hechas para los experimentos hechos por un operador
def extraerConsulta1(operador):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_operador_instrumento_fecha WHERE experimento_operador = ?")
    resultados = []
    filas = session.execute(select, [operador, ])
    for fila in filas:
        e = Experimento(operador, fila.experimento_instrumento, fila.experimento_fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta1():
    operador = input("Introducir operador de las medidas a consultar")
    resultados = extraerConsulta1(operador)
    for resultado in resultados:
        print("Operador: ", operador)
        print("Instrumento: ", resultado.instrumento)
        print("Fecha: ", resultado.fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)

# Q2-Consulta 2: de las medidas hechas para los experimentos hechos con un instrumento.
def extraerConsulta2(instrumento):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_instrumento_fecha WHERE experimento_instrumento = ?")
    resultados = []
    filas = session.execute(select, [instrumento, ])
    for fila in filas:
        e = Experimento(fila.experimento_operador, instrumento, fila.experimento_fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta2():
    instrumento = input("Introducir instrumento de las medidas a consultar")
    resultados = extraerConsulta2(instrumento)
    for resultado in resultados:
        print("Operador: ", resultado.operador)
        print("Instrumento: ", instrumento)
        print("Fecha: ", resultado.fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)

# Q3-Consulta 3: de las medidas hechas en una fecha.
def extraerConsulta3(fecha):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_fecha WHERE experimento_fecha = ?")
    resultados = []
    filas = session.execute(select, [fecha, ])
    for fila in filas:
        e = Experimento(fila.experimento_operador, fila.experimento_instrumento, fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta3():
    fecha = input("Introducir fecha de las medidas a consultar")
    resultados = extraerConsulta3(fecha)
    for resultado in resultados:
        print("Operador: ", resultado.operador)
        print("Instrumento: ", resultado.instrumento)
        print("Fecha: ", fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)

# Q4-Consulta 4: de las medidas hechas para los experimentos hechos por un operador y con un instrumento.
def extraerConsulta4(operador, instrumento):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_operador_instrumento_fecha WHERE experimento_operador = ? AND experimento_instrumento = ?")
    resultados = []
    filas = session.execute(select, [operador,instrumento, ])
    for fila in filas:
        e = Experimento(operador, instrumento, fila.experimento_fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta4():
    operador = input("Introducir operador de las medidas a consultar")
    instrumento = input("Introducir instrumento de las medidas a consultar")
    resultados = extraerConsulta4(operador,instrumento)
    for resultado in resultados:
        print("Operador: ", operador)
        print("Instrumento: ", instrumento)
        print("Fecha: ", resultado.fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)

#Q5-Consulta 5: de las medidas hechas para los experimentos hechos por un operador en una fecha.
def extraerConsulta5(operador, fecha):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_fecha WHERE experimento_operador = ? AND experimento_fecha = ?")
    resultados = []
    filas = session.execute(select, [operador,fecha, ])
    for fila in filas:
        e = Experimento(operador, fila.experimento_instrumento, fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta5():
    operador = input("Introducir operador de las medidas a consultar")
    fecha = input("Introducir fecha de las medidas a consultar")
    resultados = extraerConsulta5(operador,fecha)
    for resultado in resultados:
        print("Operador: ", operador)
        print("Instrumento: ", resultado.instrumento)
        print("Fecha: ", fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)

# Q6-Consulta 6: de las medidas hechas para los experimentos hechos con un instrumento en una fecha.
def extraerConsulta6(instrumento, fecha):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_instrumento_fecha WHERE experimento_instrumento = ? AND experimento_fecha = ?")
    resultados = []
    filas = session.execute(select, [instrumento,fecha, ])
    for fila in filas:
        e = Experimento(fila.experimento_operador, instrumento, fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta6():
    instrumento = input("Introducir instrumento de las medidas a consultar")
    fecha = input("Introducir fecha de las medidas a consultar")
    resultados = extraerConsulta6(instrumento,fecha)
    for resultado in resultados:
        print("Operador: ", resultado.operador)
        print("Instrumento: ", instrumento)
        print("Fecha: ", fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)

#Q7-Consulta 7: de las medidas hechas para los experimentos hechos por un operador, con un instrumento y en una fecha.
def extraerConsulta7(operador, instrumento, fecha):
    select = session.prepare("SELECT experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_intensidad, medida_parametro, medida_longitud FROM medidas_por_operador_instrumento_fecha WHERE experimento_operador= ? AND experimento_instrumento = ? AND experimento_fecha = ?")
    resultados = []
    filas = session.execute(select, [operador,instrumento,fecha, ])
    for fila in filas:
        e = Experimento(operador, instrumento, fecha, fila.experimento_fecha_comp)
        m = Medida(fila.medida_parametro, fila.medida_intensidad, fila.medida_longitud)
        resultados.append((e,m))
    return resultados
    pass

def consulta7():
    operador = input("Introducir operador de las medidas a consultar")
    instrumento = input("Introducir instrumento de las medidas a consultar")
    fecha = input("Introducir fecha de las medidas a consultar")
    resultados = extraerConsulta7(operador,instrumento,fecha)
    for resultado in resultados:
        print("Operador: ", operador)
        print("Instrumento: ", instrumento)
        print("Fecha: ", fecha)
        print("Fecha Completa: ", resultado.fechacomp)
        print("Parametro: ", resultado.parametro)
        print("Intensidad: ", resultado.intensidad)
        print("Longitud de onda: ", resultado.longitud)




from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('sistemasopticos')

numero = -1
while (numero != 0):
    print("Introduzca un número para ejecutar una de las siguientes operaciones:")
    print("1. Consulta por operador")
    print ("2. Consulta por instrumento")
    print ("3. Consulta por fecha")
    print ("4. Consulta por operador e instrumento")
    print ("5. Consulta por operador y fecha")
    print ("6. Consulta por instrumento y fecha")
    print ("7. Consulta por operador, instrumento y fecha")
    print("0. Para salir")

    numero = int(input())
    if (numero == 1):
        consulta1()
    elif (numero == 2):
        consulta2()
    elif (numero == 3):
        consulta3()
    elif (numero == 4):
        consulta4()
    elif (numero == 5):
       consulta5()
    elif (numero == 6):
        consulta6()
    elif (numero == 7):
        consulta7()
    elif (numero == 0):
        print("Hasta pronto")
    else:
        print("No es válido")

cluster.shutdown()  # cerramos conexion