import hashlib
import re

# Hash du mdp


def hashingpassword(password):

    return hashlib.sha256(password.encode()).hexdigest()


def checkname(name):

    regex = r"^[a-zA-Z'-\.\sàâäéèêëîïôöùûüÿ]{1,50}$"
    return re.match(regex, name)


def checkemailadress(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    return re.match(regex, email)


def checkpassword(password):
    lettresmin = 'abcdefghijklmnopqrstuvwxyz'
    lettremaj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chiffres = '0123456789'

    if 12 >= len(password) >= 50:
        print("pb longueur mp")
        return False

    Minus = 0
    Majus = 0
    Chiffres = 0
    Speciaux = 0

    for car in password:
        if car in lettresmin:
            Minus += 1
        if car in lettremaj:
            Majus += 1
        if car in chiffres:
            Chiffres += 1
        else:
            Speciaux += 1

    return all([Minus, Majus, Chiffres, Speciaux])

# Vérifie les entrées de float


def convertingfloat(nb_float):

    try:
        floatrate = float(nb_float.replace(',', '.'))
        return floatrate

    except Exception:
        return None
