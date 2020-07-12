import os
from datetime import timedelta
from flask import Flask
from FlaskSource.API.Products import productApi
from FlaskSource.API.Login import loginApi
from FlaskSource.API.User import userApi
from FlaskSource.API.Admin import adminApi
from FlaskSource.API.Location import locationApi



app = Flask(__name__, template_folder='WebApp',
            static_folder='WebApp/static')

app.register_blueprint(productApi)
app.register_blueprint(loginApi)
app.register_blueprint(userApi)
app.register_blueprint(adminApi)
app.register_blueprint(locationApi)


# Python Flask Main Function
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.permanent_session_lifetime = timedelta(minutes=20)
    app.run(debug=True, threaded=True, host='0.0.0.0', port=80)
