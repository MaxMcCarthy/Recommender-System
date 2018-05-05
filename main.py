from flask import Flask, render_template, redirect, url_for

from Forms import forms
from config.config import db

application = Flask(__name__)
application.secret_key = 'super secret string'  # Change this!
application.debug = True


@application.route('/', methods=['GET', 'POST'])
def home_page():
    sign_in_form = forms.SignInForm()
    if sign_in_form.validate_on_submit():
        cur = db.cursor()
        user = cur.execute('''SELECT * FROM user WHERE email=?''', (sign_in_form.data['email'],))
        user = user.fetchone()
        if user:
            if str(user['password']) == sign_in_form.data['password']:
                result = cur.execute('''SELECT * FROM user''')
                result = result.fetchall()
                return 'success! you\'re logged in! \n' + str(result)
        sign_in_form.email.errors.append(u'Invalid Credentials!')
    print(sign_in_form.errors)
    return render_template('login.html', form=sign_in_form)


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = forms.SignUpForm()
    if sign_up_form.validate_on_submit():
        cur = db.cursor()
        sql = '''INSERT INTO user (email, password) VALUES (?, ?)'''
        cur.execute(sql, (sign_up_form.data['email'], str(sign_up_form.data['password'])))
        db.commit()
        return redirect(url_for('survey'))
    print(sign_up_form.errors)
    return render_template('signup.html', form=sign_up_form)


@application.route('/survey', methods=['GET', 'POST'])
def survey():
    form = forms.SurveyForm()
    return render_template('survey.html', form=form)


if __name__ == '__main__':
    application.run()

