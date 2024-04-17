from data import db_session
from flask import *
from forms.user import *
from forms.base import *
from forms.signin import *
from forms.homepage import *
from data.users import User
import requests
from flask_login import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'danil_lozben'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


def main():
    db_session.global_init("db/users.db")

    @app.route('/', methods=['GET', 'POST'])
    def base():
        global lang
        ip_user = request.remote_addr
        lang = 'rus'  # временно
        # ip_info = requests.get(f'https://geo.ipify.org/api/v2/country?apiKey=at_YqASaGzc2VdPMbqg14tPKcZ4UXz0A&ipAddress={ip_user}')
        # if ip_info.json()['location']['country'] == 'RU':
        #   lang = 'rus'
        # else:
        #   lang = 'eng'
        form = HelloForm()
        if form.register.data:
            return redirect('/registration')
        if form.signin.data:
            return redirect('/signin')
        return render_template('base_' + lang + '.html', title='Добро пожаловать', form=form)

    @app.route('/signin', methods=['GET', 'POST'])
    def signin():
        form = SigninForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/homepage")
            return render_template('signin_' + lang + '.html', message="Неправильный логин или пароль", form=form,
                                   title='Вход')
        return render_template('signin_' + lang + '.html', form=form, title='Вход')

    @app.route('/registration', methods=['GET', 'POST'])
    def registration():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('registration_' + lang + '.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == form.email.data).first():
                return render_template('registration_' + lang + '.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")
            user = User(email=form.email.data)
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/homepage')
        return render_template('registration_' + lang + '.html', title='Регистрация', form=form)

    @app.route('/homepage', methods=['GET', 'POST'])
    def homepage():
        #проверка куки на регистрацию
        form = HomepageForm()
        if form.submit.data:
            return form.name_product.data
        return render_template('homepage_' + lang + '.html', title='Главная', form=form)

    app.run(port=8081, host='127.0.0.1')


if __name__ == '__main__':
    main()
