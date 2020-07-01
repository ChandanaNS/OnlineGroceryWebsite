from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jayabalaji'
app.config['MYSQL_DB'] = 'DBS'

mysql = MySQL(app)


# Python Flask API to fetch the data from MYSQL
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM MYUSERS")
    data = cur.fetchall()
    cur.close()
    return render_template('Home.html', data=data)


# Python Flask API to add the data to MYSQL
@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('Add.html')


# Python Flask Main Function
if __name__ == '__main__':
    app.run()
