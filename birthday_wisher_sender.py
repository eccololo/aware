from sender import Sender


class BirthdayWisherSender(Sender):

    def __init__(self, email_from, email_to):
        super().__init__(email_from, email_to)
