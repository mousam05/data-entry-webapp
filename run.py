from flask import Flask, request, render_template, flash, redirect
import mysql.connector
from datetime import datetime

# from sqlalchemy.testing.pickleable import User

from src.login.Domain.login_form import login_form

MYSQL_SERVER_HOST = "193.84.177.213"
MYSQL_SERVER_PORT = 3306
MYSQL_USER = "s241054_dev"
MYSQL_PASSWORD = "P4ss3v3ntr4pp3r"
MYSQL_DB_NAME = "s241054_development_eventiverse"
EVENT_TABLE = "event"
USER_TABLE = "user"


def get_db():
    try:
        db = mysql.connector.connect(
            host=MYSQL_SERVER_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB_NAME,
            port=MYSQL_SERVER_PORT,
            charset='utf8',
            use_unicode=True
        )
        return db
    except mysql.connector.Error as err:
        raise Exception("Error al conectar a la base de datos") from err


def find_record_by_email(db, email):
    find_query = 'select * from {0} where emailId = "{1}"'.format(TABLE_EVENT, email)
    cursor = db.cursor()
    cursor.execute(find_query)
    record = cursor.fetchall()

    if (len(record) == 0):
        return []
    else:
        return record[0]


def insert_or_update_record(db, user_name, password, email, phone):
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if find_record_by_email(db, email) == []:
        insert_query = 'insert into {0} values ("{1}", "{2}", "{3}", "{4}", "{5}")'.format(TABLE_EVENT,
                                                                                           user_name, email, phone,
                                                                                           password, current_timestamp)

    else:
        insert_query = 'update {0} set userName = "{1}", phoneNo = "{2}", password = "{3}", dateTime = "{4}" where emailId = "{5}"'.format(
            TABLE_EVENT, user_name, phone, password, current_timestamp, email)

    cursor = db.cursor()
    cursor.execute(insert_query)
    db.commit()


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form(request.form)
    #form = login_form()
    if request.method == 'POST' and form.validate():
        create_user(form)
        return redirect('/success')
    return render_template('login.html', form=form)


def create_user(form):

        user_name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        role = request.form['role']
        insert_query = 'insert into {0} values ("{1}", "{2}", "{3}", "{4}", "{5}")'.format(USER_TABLE,
                                                                                           user_name, email, role,
                                                                                           password)
        message = "Record inserted successfully."
        flash('Olee te has registradoooo!')

        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(insert_query)
            db.commit()
            db.close()
        except mysql.connector.Error as e:
            message = "There was an error inserting the record."

@app.route('/', methods=['GET', 'POST'])
def main():
    message = ""

    if request.method == 'POST':
        if 'submit_credentials' in request.form:
            user_name = request.form['user_name']
            password = request.form['password']
            email = request.form['email']
            phone = request.form['phone_number']

            message = "Record inserted successfully."

            try:
                db = get_db()
                status = insert_or_update_record(db, user_name, password, email, phone)
                db.close()
            except mysql.connector.Error as e:
                message = "There was an error inserting the record."

        if 'submit_email_search' in request.form:
            email_search = request.form['email_search']

            try:
                db = get_db()
                record = find_record_by_email(db, email_search)
                db.close()
            except mysql.connector.Error as e:
                message = "There was an error fetching records."

            if record == []:
                message = "No matching record was found."
            else:
                record = list(record)
                # convert timestamp to proper format for display
                record[4] = record[4].strftime('%Y-%m-%d %H:%M:%S')
                record_show = \
                    "User name: " + record[0] + \
                    ", Email ID:" + record[1] + \
                    ", Phone no.: " + record[2] + \
                    ", Password: " + record[3] + \
                    ", Timestamp: " + record[4]
                message = "Record found: \n" + repr(record_show)

    return render_template('main.html', message=message)


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key = 'super secret key'
    app.debug = True

    app.run(host='127.0.0.1', port=5000, debug=True)
