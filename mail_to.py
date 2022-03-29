from flask import flash, request
from flask_login import current_user


def send_mail(topic, message):

    client = Smtp2goClient(api_key='api-964C4C04A90311ECAD26F23C91BBF4A0')

    payload = {
        'sender': 'maylislb@hotmail.fr',
        'recipients': ['maylislb09@gmail.com'],
        'subject': f'Formulaire de support: {topic}',
        'html': f'<html><body><h1>Formulaire de support: {topic}</h1><br><h4>Site de provenance:</h4><br><p>{request.url}</p><br><h4>Demandeur:<br></h4><p>{current_user.email}</p><br><h4>Texte de la demande:</h4><br><p>{message}</p></body><html>'
    }

    try:
        response = client.send(**payload)
    except Exception:
        flash('Une erreur est survenue à l\'envoie du formulaire.')
        return False

    print(response.success)

    return True
