from data import db_session
from flask import *
from forms.user import *
from forms.base import *
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'danil_lozben'


def main():
    db_session.global_init("db/users.db")

    @app.route('/', methods=['GET', 'POST'])
    def base():
        form = HelloForm()
        print(form.register.data)
        if form.register.data:
            return redirect('/registration')
        if form.signin.data:
            return redirect('/signin')
        return render_template('base_rus.html', title='govno', form=form)

    @app.route('/signin')
    def signin():
        form = HelloForm()
        if form.validate_on_submit():
            pass
        pass
        # проверка пользователя на наличи в базе данных


    @app.route('/registration', methods=['GET', 'POST'])
    def registration():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('registration_rus.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == form.email.data).first():
                return render_template('registration_rus.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")
            user = User(email=form.email.data)
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/homepage')
        return render_template('registration_rus.html', title='Регистрация', form=form)

    @app.route('/homepage')
    def homepage():
        return 'nothing'

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
