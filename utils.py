import hashlib
import re
import filetype

# Hash du mot de passe


def hashingpassword(password):

    return hashlib.sha256(password.encode()).hexdigest()

# Vérifie la conformité des entrées texte


def checkname(name):

    regex = r"^[a-zA-Z'-\.\sàâäéèêëîïôöùûüÿ]{1,50}$"
    return re.match(regex, name)

# Vérifie la conformité des adresses mail


def checkemailadress(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    return re.match(regex, email)

# Vérifie les mots de passe


def checkpassword(password):
    lettresmin = 'abcdefghijklmnopqrstuvwxyz'
    lettremaj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chiffres = '0123456789'

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

# Vérifie la conformité des urls


def checkurl(url):
    regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$"
    return re.match(regex, url)

# Convertie les entrées en float


def convertingfloat(nb_float):

    try:
        floatrate = float(nb_float.replace(',', '.'))
        return floatrate

    except Exception:
        return None

# Vérifie le fichier entré est une image


def checkimg(file_img):
    # filename = "/path/to/file.jpg"

    print(file_img)
    if filetype.is_image(file_img.read()):
        file_img.seek(0)
        return True
    else:
        file_img.seek(0)
        return False
