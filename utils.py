import hashlib

# Hash du mdp


def hashingpassword(password):

    return hashlib.sha256(password.encode()).hexdigest()
