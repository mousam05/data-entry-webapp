from src.Core.db.DatabaseManager import DatabaseManager

class Event:
    _EVENT_TABLE = "event"

    def event_list_collection(self):
        global db
        query = "select * from {0} order by id desc, startDate desc". format(self._EVENT_TABLE)

        try:
            data_base_manager_instance = DatabaseManager()
            db = data_base_manager_instance.get_db()
            cursor = db.cursor(dictionary=True)
            cursor.execute(query)
            events = cursor.fetchall()
            return events
        except mysql.connector.Error as e:
            print("Query:", query)
            raise Exception("Error executing query") from e
        finally:
            if db:
                db.close()