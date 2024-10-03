from decouple import config
from django.core.mail import send_mail
from config.celery import app

# TODO: add html page for email verification.

@app.task
def send_verification_link(email: str, code: str) -> None:
    full_link = f"http://{config('SERVER_IP')}/verification/{code}/"
    send_mail(
        subject="Account verification",
        message=f"Follow the link to activate your account: {full_link}",
        from_email=config("EMAIL_HOST"),
        recipient_list=[email],
        )

# TODO: write resend and account recovery task.