from Forms import app
from Forms.Model.model import db

app.secret_key = "|ZWszK=T:T;B|qW@"
app.config['MONGODB_SETTINGS'] = {
    'db': 'userdb',
    'host': 'localhost',
    'port': 27017
}

db.init_app(app)
if __name__ == '__main__':
    app.run(port=5000,debug=True)
