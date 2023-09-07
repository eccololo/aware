import os


class Sender:

    def __init__(self, email_from, email_to):
        self.email_app_pass = os.environ.get("EMAIL_APP_PASS")
        self.email_from = email_from
        self.email_to = email_to
