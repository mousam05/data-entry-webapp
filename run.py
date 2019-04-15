import MySQLdb

from flask import Flask, request, render_template, flash
from datetime import datetime

MYSQL_SERVER_HOST = "db-intern.ciupl0p5utwk.us-east-1.rds.amazonaws.com"
MYSQL_SERVER_PORT = 3306
MYSQL_USER = "dummyUser"
MYSQL_PASSWORD = "dummyUser01"
MYSQL_DB_NAME = "db_intern"
MYSQL_TABLE_NAME = "userData"

# database handling functions
#############################

# connect to the database
def get_db():
	db = MySQLdb.connect(MYSQL_SERVER_HOST, MYSQL_USER, MYSQL_PASSWORD,
		MYSQL_DB_NAME, port = MYSQL_SERVER_PORT, charset='utf8', use_unicode=True )

	return db

# get the record corresponding to an email id
def find_record_by_email(db, email):
	find_query = 'select * from {0} where emailId = "{1}"'.format(MYSQL_TABLE_NAME, email)
	cursor = db.cursor()
	cursor.execute(find_query)
	record = cursor.fetchall()

	if(len(record) == 0):
		return []
	else:
		return record[0]

# insert a record or update it if it exists
def insert_or_update_record(db, user_name, password, email, phone):

	current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	if find_record_by_email(db, email) == []:
		insert_query = 'insert into {0} values ("{1}", "{2}", "{3}", "{4}", "{5}")'.format(MYSQL_TABLE_NAME, 
			user_name, email, phone, password, current_timestamp)

	else:
		insert_query = 'update {0} set userName = "{1}", phoneNo = "{2}", password = "{3}", dateTime = "{4}" where emailId = "{5}"'.format(
			MYSQL_TABLE_NAME, user_name, phone, password, current_timestamp, email)

	cursor = db.cursor()
	cursor.execute(insert_query)
	db.commit()


# browser request handling code
###############################

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
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
			except MySQLdb.Error as e:
				message = "There was an error inserting the record."
				


		if 'submit_email_search' in request.form:
			email_search = request.form['email_search']

			try:
				db = get_db()
				record = find_record_by_email(db, email_search)
				db.close()
			except MySQLdb.Error as e:
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

	return render_template('main.html', message = message)

if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'filesystem'
	app.secret_key = 'super secret key'
	app.debug = True

	app.run(host='127.0.0.1', port=5000, debug = True)