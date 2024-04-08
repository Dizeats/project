from data import db_session
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/users.db")


def main():
    app.run()


if __name__ == '__main__':
    main()
