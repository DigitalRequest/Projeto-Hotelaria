import mysql.connector
import datetime
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
tiposQuarto = ["Executivo", "Luxo", "Superluxo"]

primeiroNomeLista = ['Mia', 'Logan', 'Ella', 'Liam', 'Avery', 'Oliver', 'Emma', 'Noah', 'Ava', 'Sophia', 'Jackson', 'Isabella', 'Lucas', 'Amelia', 'Benjamin', 'Mila', 'Elijah', 'Harper', 'Aiden', 'Abigail', 'Olivia', 'Aria', 'Ethan', 'Scarlett', 'Grace', 'Chloe', 'Lily', 'Zoe', 'Alexander', 'Emily', 'Luna', 'Carter', 'Charlotte', 'Michael', 'Sofia', 'Mason', 'Liam', 'Aiden', 'Zoe', 'Ella', 'Harper', 'Avery', 'Sophia', 'Grace', 'Lily', 'Amelia', 'Olivia', 'Chloe']
ultimoNomeLista = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Perez', 'Turner', 'Gomez', 'Phillips', 'Evans', 'Collins', 'Morgan']


# Mude suas credenciais aqui por favor
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="G21f12f04@##",
    database="hotelaria"
)

cursor = mydb.cursor()

cursor.execute("SELECT idReserva FROM RESERVA")
idReserva_lista = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT idHospede FROM HOSPEDE")
idHospede_lista = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT idEquipe FROM EQUIPE")
idRecepcionista_lista = [row[0] for row in cursor.fetchall()]

sqlEquipe = "INSERT INTO EQUIPE VALUES(%s, %s, %s, %s, %s, %s)"
sqlHospede = "INSERT INTO HOSPEDE VALUES(%s, %s, %s, %s, %s)"
sqlQuarto = "INSERT INTO QUARTO VALUES(%s, %s, %s, %s, %s)"
sqlReserva = "INSERT INTO RESERVA VALUES(%s, %s, %s, %s, %s, %s, %s)"

valsEquipe = []
valsHospede = []
valsQuarto = []
valsReserva = []


def inserirEquipe(valsEquipe, cursor):
    equipeId = random.randint(0, 100000000)
    primeiroNome = random.choice(primeiroNomeLista)
    ultimoNome = random.choice(ultimoNomeLista)
    numCelular = str.format("+{} {}", random.randint(10, 99), random.randint(100000000000, 999999999999))
    equipeEmail = "".join(random.choice(letters) for _ in range(random.randint(4, 10))) + "@gmail.com"
    if len(idRecepcionista_lista) > 0:
        idGerente = random.choice(idRecepcionista_lista)
    else:
        idGerente = equipeId

    valsEquipe.append((equipeId, primeiroNome, ultimoNome, numCelular, equipeEmail, idGerente))
    cursor.executemany(sqlEquipe, [valsEquipe[-1]])

    return equipeId

def inserirHospede(valsHospede, cursor):
    hospedeId = random.randint(0, 100000000)
    primeiroNome = random.choice(primeiroNomeLista)
    ultimoNome = random.choice(ultimoNomeLista)
    numCelular = str.format("+{} {}", random.randint(10, 99), random.randint(100000000000, 999999999999))
    hospedeEmail = "".join(random.choice(letters) for _ in range(random.randint(4, 10))) + "@gmail.com"

    valsHospede.append((hospedeId, primeiroNome, ultimoNome, numCelular, hospedeEmail))
    cursor.executemany(sqlHospede, [valsHospede[-1]])
    return hospedeId


def inserirReserva(valsReserva, cursor, idHospede_lista, idRecepcionista_lista):
    idReserva = random.randint(0, 100000000)
    idHospede = 0
    if len(idHospede_lista) > 0:
        idHospede = random.choice(idHospede_lista)
    else:
        idHospede = inserirHospede(valsHospede, cursor)
    if len(idRecepcionista_lista) > 0:
        idRecepcionista = random.choice(idRecepcionista_lista)
    else:
        idRecepcionista = inserirEquipe(valsEquipe, cursor)
    dataCheckIn = datetime.datetime.now()
    dataCheckOut = datetime.datetime.now()
    numAdultos = random.randint(0, 4)
    numCriancas = random.randint(0, 4)

    valsReserva.append(
        (idReserva, idHospede, idRecepcionista, dataCheckIn, dataCheckOut, numAdultos, numCriancas))
    cursor.executemany(sqlReserva, [valsReserva[-1]])


def inserirQuarto(valsQuarto, cursor):
    cursor.execute("SELECT idReserva FROM RESERVA")
    idReserva = [row[0] for row in cursor.fetchall()]
    idReserva = idReserva[0]
    
    cursor.fetchall()
    
    quartoNumero = random.randint(0, 99)
    qtdCamas = random.randint(0, 4)
    tipoQuarto = random.choice(tiposQuarto)
    cursor.execute("SELECT numAdultos FROM RESERVA WHERE idReserva = {}".format(idReserva))
    numAdultos = [row[0] for row in cursor.fetchall()]
    numAdultos = numAdultos[0]
    valDirPessoa = numAdultos
    if tipoQuarto == "Executivo":
        valDirPessoa *= 300
    elif tipoQuarto == "Luxo":
        valDirPessoa *= 500
    else:
        valDirPessoa *= 700
    
    valsQuarto.append((quartoNumero, qtdCamas, valDirPessoa, tipoQuarto, idReserva))
    cursor.executemany(sqlQuarto, [valsQuarto[-1]])


# INSERIR EQUIPE
inserirEquipe(valsEquipe, cursor)
# INSERIR HOSPEDE
idHospede = inserirHospede(valsHospede, cursor)
# INSERIR RESERVA
inserirReserva(valsReserva, cursor, idHospede_lista, idRecepcionista_lista)
# INSERIR QUARTO
inserirQuarto(valsQuarto, cursor)

result = cursor.fetchall()

mydb.commit()