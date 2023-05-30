from db_operations import DatabaseOperations
from excel_application import ExcelApplication
from notifier import EmailNotifier
from extract import Extractor

import logging

from selenium.common.exceptions import NoSuchElementException


extractor = Extractor()
email_notifier = EmailNotifier()
excel_app = ExcelApplication()
db_op =DatabaseOperations()


class Robot:
    def __init__(self, name):
        """
        Initializes a Robot object.

        Args:
            name (str): The name of the robot.
        """
        self.name = name
        self.scientist_info = []
        self.validate_status = True

    def introduce(self):
        """
        Introduces the robot and its purpose.
        """
        print(f"Hello, my name is {self.name}. I will navigate to the Wikipedia page of scientists and retrieve information. The retreived information will be saved in a destinated database and an excel workbook with the name you inputted.")
        print("")

    def exit_success(self):
        """
        Displays a farewell message and instructions on finding the location of the exported Excel workbook.
        """
        logging.info("Process completed successfully.")
        print(f"Thank you for using Quandrinaut. The scientists information has been successfully saved to the database and an excel workbook named {excel_app.filename}.xlsx. You can find {excel_app.filename}.xlsx located at your Desktop")
    
    def exit_failure(self, err_msg):
        """
        Displays a farewell message and instructions if the robot is not initiated successfully.

        Args:
            err_msg (str): The error message to display.
        """
        print(err_msg)

    def get_scientist_info(self, scientists):
        """
        Retrieves information about scientists from their Wikipedia pages.

        Args:
            scientists (list): A list of scientist names.
        """
        for scientist in scientists:
            # Navigate to scientist's Wikipedia page
            extractor.open_webpage(f"https://en.wikipedia.org/wiki/{scientist.replace(' ', '_')}")

            try:
                extractor.extract_scientist_info(scientist, self.scientist_info)

            except NoSuchElementException:
                # Handle exceptions that occur when there is no birth date and/or death date and/or first paragraph
                self.handle_exceptions_with_notify_email(f"Could not find the birth date and/or death date and/or description for {scientist}.")

                # shut down the application
                self.validate_status = False

            except Exception as e:
                # Handle any exceptions that occur during extracting the information from wikipedia
                self.handle_exceptions_with_notify_email(f"Something went wrong when getting the information from wikipedia:{str(e)}. Please double check the names in the scientist list or contact the administrator.")

                # shut down the application
                self.validate_status = False

        
    def write_to_excel(self):
        """
        Writes scientist information to an Excel workbook.
        """
        try:

            # If no error of getting the data, start writing the info to the workbook
            if self.validate_status:
                excel_app.write_to_cells(self.scientist_info)
            else:
                # If getting the information failed, return without further action
                return
        except Exception as e:
            # Handle any exceptions that occur during writing to the excel workbook
            self.handle_exceptions_with_notify_email(f"An error occurred while writing to the excel workbook: {str(e)}. No data will be saved in the excel workbook. Please contact the administrator.")

            # shut down the application
            return
    
    def write_to_database(self):
        """
        Writes scientist information to a database.
        """
        if self.validate_status:
            try:
                db_op.connect_to_database()
                db_op.update_database(self.scientist_info)

                # Exit with success status
                self.exit_success()
            except Exception as e:
                # Handle any exceptions that occur during database operations
                self.handle_exceptions_with_notify_email(f"An error occurred while writing to the database: {str(e)} . No data will be saved in the database. Please contact the administrator.")

                # shut down the application
                return

    def notify_gmail(self, err_msg):
        """
        Sends a notification email via Gmail if an error occurred.

        Args:
            err_msg (str): The error message to include in the email.
        """
        try:
            email_notifier.send_email_notification(err_msg)

        except Exception as e:
            # Handle any exceptions that occur during sending email notification
            logging.exception((f"An error occurred while writing to the database: {str(e)}. No email will be sent. Please contact the administrator."))
            self.exit_failure((f"An error occurred while sending email: {str(e)}. No Email will be sent. Please contact the administrator."))

            # shut down the application
            return
        
    def handle_exceptions_with_notify_email(self, err_msg):
        """
        Handles exceptions by logging and sending an email notification.

        Args:
            err_msg (str): The error message to include in the logging and email.
        """
        logging.exception(err_msg)
        self.notify_gmail(err_msg)
        self.exit_failure(err_msg)
