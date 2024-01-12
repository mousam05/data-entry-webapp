import mysql.connector
class DatabaseManager:
    # obtener desde fichero .env
    MYSQL_SERVER_HOST = "193.84.177.213"
    MYSQL_SERVER_PORT = 3306
    MYSQL_USER = "s241054_dev"
    MYSQL_PASSWORD = "P4ss3v3ntr4pp3r"
    MYSQL_DB_NAME = "s241054_development_eventiverse"


    def get_db(self):
        try:
            db = mysql.connector.connect(
                host=self.MYSQL_SERVER_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DB_NAME,
                port=self.MYSQL_SERVER_PORT,
                charset='utf8',
                use_unicode=True
            )
            return db
        except mysql.connector.Error as err:
            raise Exception("Error trying connect to database") from err