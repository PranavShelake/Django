from django.conf import settings
from django.core.mail import EmailMessage

def sent_mail(name, gmail, body, file):
    subject = "Message from Pranav Portfolio sent by " + gmail
    from_email = settings.EMAIL_HOST_USER
    to = ["pranavshelake99@gmail.com"]

    body = f"Name = {name}\nGmail = {gmail}\nMessage = {body}"
    mail = EmailMessage(subject, body, from_email, to)
    
    if file:
        mail.attach(file.name, file.read(), file.content_type)

    mail.send()
