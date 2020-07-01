import os
from datetime import timedelta

from flask import Flask
from FlaskSource.API.Products import productApi
from FlaskSource.API.Login import loginApi

app = Flask(__name__, template_folder='WebApp',
            static_folder='WebApp/static')

app.register_blueprint(productApi)
app.register_blueprint(loginApi)

# Python Flask Main Function
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.permanent_session_lifetime = timedelta(minutes=20)
    app.run(debug=True, threaded=True, host='0.0.0.0', port=80)
