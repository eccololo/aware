import os


class Sender:

    def __init__(self):
        self.email_app_pass = os.environ.get("EMAIL_APP_PASS")
