from flask import Blueprint, render_template, request
from flask_login import login_required
from utils.mail_to import send_mail

contact_api = Blueprint('contact_api', __name__)


@contact_api.route("/contact", methods=['GET', 'POST'])
@login_required
def contact():
    """ Renvoie le formulaire de contact (GET), Envoie le formulaire (POST)"""

    if request.method == 'POST':

        topic = request.form.get('topic')
        message = request.form.get('message')

        message = message.replace('\r\n', '<br>')

        send_mail(topic, message)

        return render_template("contact.html")
    else:
        return render_template("contact.html")
