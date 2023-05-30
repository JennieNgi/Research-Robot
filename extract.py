from RPA.Browser.Selenium import Selenium

from datetime import datetime
from selenium.webdriver.common.by import By


class Extractor:
    def __init__(self):
        self.browser = Selenium()

    def open_webpage(self, webpage):
        """
        Opens a web page in an available browser.

        Args:
            webpage (str): The URL of the web page to open.
        """
        self.browser.open_available_browser(webpage)

    def extract_scientist_info(self, scientist, scientist_info):
        """
        Retrieves information about scientists from their Wikipedia pages.

        Args:
            scientist (str): The name of the scientist.
            scientist_info (list): A list to store the scientist information.
        """
        # Retrieve Death date
        death_date_element = self.browser.find_elements("//span[@style='display:none']")[1]
        death_date_value = death_date_element.get_attribute("innerHTML").replace("(", "").replace(")", "")

        # Retrieve Birth date
        birth_date_element = self.browser.find_elements("//span[@style='display:none']")[0].find_element(By.XPATH, ".//span[@class='bday']")
        birth_date_value = birth_date_element.get_attribute("innerHTML")

        # Convert birth and death dates to datetime objects
        birth_datetime = datetime.strptime(birth_date_value, "%Y-%m-%d")
        death_datetime = datetime.strptime(death_date_value, "%Y-%m-%d")

        # Calculate the age in years
        age = death_datetime.year - birth_datetime.year

        # Check if the death month and day are before the birth month and day
        if (death_datetime.month, death_datetime.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1

        # Retrieve First Paragraph
        first_paragraph_element = self.browser.find_elements("//p[not(@class='mw-empty-elt')]")[0]
        first_paragraph_value = first_paragraph_element.text.replace("'", "")

        # Display information in the terminal
        print("Scientist:", scientist)
        print("Birth Date:", birth_date_value)
        print("Death Date:", death_date_value)
        print("Age at death:", age)
        print("Description:", first_paragraph_value)
        print("")

        # Create a dictionary with scientist information
        scientist_info.append({
            'name': scientist,
            'death_date': death_date_value,
            'birth_date': birth_date_value,
            'age': age,
            'description': first_paragraph_value
        })

        self.browser.close_all_browsers()

