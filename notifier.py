from RPA.Notifier import Notifier

from dotenv import dotenv_values


class EmailNotifier:
    def __init__(self):
        self.notifier = Notifier()
        self.env_vars = dotenv_values(".env")

    def send_email_notification(self, err_msg):
        """
        Sends an email notification with the provided error message.

        Args:
            err_msg (str): The error message to include in the email.
        """
        # Retrieve email configuration from environment variables
        email_address_receiver = self.env_vars["EMAIL_RECEIVER"]
        email_user = self.env_vars["EMAIL_USERNAME"]
        email_pw = self.env_vars["EMAIL_PW"]

        # Send a notification email
        self.notifier.notify_gmail(
            message=err_msg,
            to=email_address_receiver,
            username=email_user,
            password=email_pw
        )
