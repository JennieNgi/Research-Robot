from RPA.Database import Database

from dotenv import dotenv_values


class DatabaseOperations:
    def __init__(self):
        self.db = Database()
        self.env_vars = dotenv_values(".env")

    def connect_to_database(self):
        """
        Connects to the database.
        """
        # Retrieve database configuration from environment variables
        db_name = self.env_vars["DB_NAME"]
        db_host = self.env_vars["DB_HOST"]
        db_user = self.env_vars["DB_USER"]
        db_password = self.env_vars["DB_PASSWORD"]
        db_port = self.env_vars["DB_PORT"]

        # Connect to the database
        self.db.connect_to_database(
            "pymysql",
            db_name,
            db_user,
            db_password,
            db_host,
            int(db_port),
        )

    def update_database(self, scientist_info):
        """
        Updates the database with the scientist information.

        Args:
            scientist_info (list): A list containing dictionaries of scientist information.
        """
        # Iterate over the scientists and insert their information into the database
        for scientist in scientist_info:
            # Check if a scientist with the same name already exists in the database
            query = f"SELECT COUNT(*) FROM scientists WHERE name = '{scientist['name']}'"
            result = self.db.query(query)
            count = result[0][0]
            # if the name doesn't exist in the database, insert records to the database
            if count == 0:
                query = f"INSERT INTO scientists (name, death_date, birth_date, age, description) VALUES ('{scientist['name']}', '{scientist['death_date']}', '{scientist['birth_date']}', '{scientist['age']}', '{scientist['description']}')"
                # execute the sql query
                self.db.query(query)
            else:
                # If a record with the same name exists, update the scientist information in the database
                query = f"UPDATE scientists SET death_date = '{scientist['death_date']}', birth_date = '{scientist['birth_date']}', age = '{scientist['age']}', description = '{scientist['description']}' WHERE name = '{scientist['name']}'"
                # execute the sql query
                self.db.query(query)
