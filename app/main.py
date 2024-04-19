from data import db_session
from flask import *
from forms.user import *
from forms.base import *
from forms.signin import *
from forms.homepage import *
from data.users import User
from data.products import Product
import requests
from sqlite3 import *
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
            login_user(user, True)
            return redirect('/homepage')
        return render_template('registration_' + lang + '.html', title='Регистрация', form=form)

    @app.route('/homepage', methods=['GET', 'POST'])
    def homepage():
        if request.cookies.get('remember_token') == '':
            return redirect('/')
        bas = connect('db/users.db')
        cur = bas.cursor()
        id_of_user = cur.execute('''SELECT id FROM users WHERE email = ?''', (current_user.email,)).fetchall()
        products = cur.execute('''SELECT * FROM products WHERE user_id = ?''', (id_of_user[0][0], )).fetchall()
        form = HomepageForm()
        if form.add.data:
            added_product = form.name_added_product.data
            cur.execute('''INSERT INTO products(user_id, name) VALUES(?, ?)''', (id_of_user[0][0], added_product))
        if form.delete.data:
            deleted_product = form.name_deleted_product.data
            print(deleted_product)
            id_of_product = cur.execute('''SELECT id FROM products WHERE name = ?''', (deleted_product, )).fetchall()
            print(id_of_product)
            cur.execute('''DELETE FROM products WHERE id = ?''', (id_of_product[0][0], ))
        return render_template('homepage_' + lang + '.html', products=products, title='Главная', form=form)

    @app.route('/logout')
    def logout():
        res = redirect('/')
        res.set_cookie("remember_token", "", 0)
        return res

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
