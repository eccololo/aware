import sys
from birthday_wisher_sender import BirthdayWisherSender

email_from = sys.argv[1]
email_to = sys.argv[2]
if email_from and email_to:
    bw_sender = BirthdayWisherSender(email_from, email_to)
