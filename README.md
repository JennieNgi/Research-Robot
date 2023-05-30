### Robotic Researcher
The goal of this project is to develop a software robot that retrieves key information about important scientists from Wikipedia and displays it to the user.

## Project Description
The Robotic Researcher software robot performs the following steps:
- Introduce itself and explain the process it will follow.
- Navigate to the Wikipedia page of each scientist in the provided list.
- Retrieve the birth and death dates of each scientist and calculate their age.
- Retrieve the first paragraph of each scientist's Wikipedia page.
- Display all the collected information to the user in an easily understandable manner.
- Save the information to an excel workbook with the name that the user input.
- Save the information to a destinated database.
- If any error raised during the process, an email will be sent to the receiver by GMAIL.


## Project Setup
To set up the project, follow these steps:
- Ensure you have Python installed on your system (Python 3.6 or above is recommended).
- Install the required dependencies using pip:
```
pip install -r requirements.txt
```
- Set up a virtual environment (optional but recommended) to isolate the project's dependencies.
- Set up necessary variables in .env file: you need a mySQL database running and gmail
- For gmail settings, you will need to generate a password for use: go to your Gmail Accout > Security > 2-Step Verification > App passwords > Select App (Other) > GENERATE

## Project Execution in Local Environment
To execute the Robotic Researcher software robot, follow these steps:
- Activate the virtual environment (if set up).
- Run main.py