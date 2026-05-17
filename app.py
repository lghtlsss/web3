from flask import Flask, render_template, url_for, redirect
from data.db_session import create_session, global_init
from jobs_request import get_jobs
from data.register_form import RegisterForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route('/')
@app.route('/index')
def index():
    session = create_session()
    context = {'title': '', 'works_list': get_jobs(session)}
    return render_template('index.html', **context)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    session = create_session()
    if form.validate_on_submit():
        if form.password.data == form.repeat_password.data:
            if 0 <= int(form.age.data) <= 120:
                user = User(
                    email=form.login.data,
                    surname=form.surname.data,
                    name=form.name.data,
                    age=form.age.data,
                    position=form.position.data,
                    speciality=form.speciality.data,
                    address=form.address.data
                )
                user.set_password(form.password.data)
                session.add(user)
                session.commit()
                return redirect('/index')
            return render_template('register.html', form=form, message='Такой возраст невозможен')
        return render_template('register.html', form=form, message='Пароли не совпадают')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    global_init('db/mars.sqlite')
    app.run(port=8080, host='127.0.0.1', debug=False)
