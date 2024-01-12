from src.Core.db.DatabaseManager import DatabaseManager


class User:
    _USER_TABLE = "user"

    def create_user(self, form):
        global db
        user_name = form.name.data
        password = form.password.data
        email = form.email.data
        role = form.role.data
        insert_query = 'insert into {0} (name, password, email, role) values ("{1}", "{2}", "{3}", "{4}")'.format(
            self._USER_TABLE, user_name, password, email, role
        )
        print(insert_query)
        try:
            data_base_manager_instance = DatabaseManager()
            db = data_base_manager_instance.get_db()
            cursor = db.cursor()
            cursor.execute(insert_query)
            db.commit()
        except mysql.connector.Error as e:
            print("Query:", insert_query)
            raise Exception("Error executing query") from e
        finally:
            if db:
                db.close()
