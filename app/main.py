from data import db_session
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users.db")

    @app.route('/registration')
    def registration():
        return 'test'

    @app.route('/homepage')
    def homepage():
        return 'nothing'

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
