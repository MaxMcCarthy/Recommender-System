from flask import Flask, render_template

from Forms import forms

application = Flask(__name__)
application.secret_key = 'super secret string'  # Change this!
application.debug = True


@application.route('/', methods=['GET', 'POST'])
def home_page():
    sign_in_form = forms.SignInForm()
    if sign_in_form.validate_on_submit():
        return str(sign_in_form.data)
    return render_template('login.html', form=sign_in_form)


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = forms.SignUpForm()
    if sign_up_form.validate_on_submit():
        return str(sign_up_form.data)
    print(sign_up_form.errors)
    return render_template('signup.html', form=sign_up_form)


if __name__ == '__main__':
    application.run()

