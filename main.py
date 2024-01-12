from flask import Flask
from flask_bootstrap import Bootstrap

from src.Event.Infrastructure.routes import event_blueprint
from src.Login.Infrastructure.routes import login_blueprint


app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(event_blueprint, url_prefix='/')
app.register_blueprint(login_blueprint, url_prefix='/login') # hacer una para el / que si no peta y no guarda el registro


def timestampformat(value, format='%Y-%m-%d %H:%M:%S'):
    from datetime import datetime
    return datetime.fromtimestamp(value).strftime(format)
# Agregar el filtro de formateo de fechas
app.jinja_env.filters['timestampformat'] = timestampformat



if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key = 'super secret key'
    app.debug = True

    app.run(host='127.0.0.1', port=5000, debug=True)
