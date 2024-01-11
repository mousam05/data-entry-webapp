### Running the project

Then run the following command in a terminal:
`python3 run.py --reload`

Next, open a browser, type `127.0.0.1:5000` in the address bar, and hit enter. You will see a webpage containing some forms and buttons. This is the main (and only) webpage of the project. Your computer must be connected to the internet to communicate with the MySQL server. That's it!


rm -r venv 

python3 -m venv venv              
 source venv/bin/activate  
pip install -r requirements.txt

deactivate

pip3 freeze > requirements.txt
pip3 install -r requirements.txt 

python3 run.py --reload

http://127.0.0.1:5000/admin/

lsof -i :5000
kill -9 UID
