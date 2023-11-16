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

# Assuming you have a primary key or unique constraint to identify records for updating
update_condition = "WHERE {} = {}"

sqlEquipe = "UPDATE EQUIPE SET primeiroNome=%s, ultimoNome=%s, numCelular=%s, email=%s, idGerente=%s " + update_condition.format("idEquipe", random.choice(idRecepcionista_lista))
sqlHospede = "UPDATE HOSPEDE SET primeiroNome=%s, ultimoNome=%s, numCelular=%s, email=%s " + update_condition.format("idHospede", random.choice(idHospede_lista))
sqlQuarto = "UPDATE QUARTO SET qtdCamas=%s, valDiariaPes=%s, tipoQuarto=%s, idReserva=%s " + update_condition.format("1", "1")
sqlReserva = "UPDATE RESERVA SET idHospede=%s, idRecepcionista=%s, dataCheckIn=%s, dataCheckOut=%s, numAdultos=%s, numCriancas=%s " + update_condition.format("1", "1")

valsEquipe = []
valsHospede = []
valsQuarto = []
valsReserva = []


def atualizarEquipe(valsEquipe, cursor):
    primeiroNome = random.choice(primeiroNomeLista)
    ultimoNome = random.choice(ultimoNomeLista)
    numCelular = str.format("+{} {}", random.randint(10, 99), random.randint(100000000000, 999999999999))
    equipeEmail = "".join(random.choice(letters) for _ in range(random.randint(4, 10))) + "@gmail.com"
    idGerente = random.choice(idRecepcionista_lista)

    valsEquipe.append((primeiroNome, ultimoNome, numCelular, equipeEmail, idGerente))
    cursor.execute(sqlEquipe, valsEquipe[-1])


def atualizarHospede(valsHospede, cursor):
    primeiroNome = random.choice(primeiroNomeLista)
    ultimoNome = random.choice(ultimoNomeLista)
    numCelular = str.format("+{} {}", random.randint(10, 99), random.randint(100000000000, 999999999999))
    hospedeEmail = "".join(random.choice(letters) for _ in range(random.randint(4, 10))) + "@gmail.com"

    valsHospede.append((primeiroNome, ultimoNome, numCelular, hospedeEmail))
    cursor.execute(sqlHospede, valsHospede[-1])


def atualizarQuarto(valsQuarto, cursor):
    qtdCamas = random.randint(0, 4)
    tipoQuarto = random.choice(tiposQuarto)
    valDirPessoa = random.randint(100, 1000)
    idReserva = random.choice(idReserva_lista)

    valsQuarto.append((qtdCamas, valDirPessoa, tipoQuarto, idReserva))
    cursor.execute(sqlQuarto, valsQuarto[-1])


def atualizarReserva(valsReserva, cursor):
    idHospede = random.choice(idHospede_lista)
    idRecepcionista = random.choice(idRecepcionista_lista)
    dataCheckIn = datetime.datetime.now()
    dataCheckOut = datetime.datetime.now()
    numAdultos = random.randint(0, 4)
    numCriancas = random.randint(0, 4)

    valsReserva.append(
        (idHospede, idRecepcionista, dataCheckIn, dataCheckOut, numAdultos, numCriancas))
    cursor.execute(sqlReserva, valsReserva[-1])


atualizarEquipe(valsEquipe, cursor)
atualizarHospede(valsHospede, cursor)
atualizarReserva(valsReserva, cursor)
atualizarQuarto(valsQuarto, cursor)

mydb.commit()
