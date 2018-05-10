from flask import Flask, render_template, redirect, url_for

from Forms import forms
from Config.config import db
from Recommender.recommender import recommend

application = Flask(__name__)
application.secret_key = 'super secret string'  # Change this!
application.debug = True


@application.route('/', methods=['GET', 'POST'])
def home_page():
    sign_in_form = forms.SignInForm()
    if sign_in_form.validate_on_submit():

        # locate user email in database
        cur = db.cursor()
        user = cur.execute('''SELECT * FROM user WHERE email=?''', (sign_in_form.data['email'],))
        user = user.fetchone()

        # see if password in the database matches the given password
        if user:
            if str(user['password']) == str(sign_in_form.data['password']):
                return redirect(url_for('results', user_id=user['user_id']))
        sign_in_form.email.errors.append(u'Invalid Credentials!')

    # return login page
    return render_template('login.html', form=sign_in_form)


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = forms.SignUpForm()
    if sign_up_form.validate_on_submit():
        cur = db.cursor()

        # insert user
        sql = '''INSERT INTO user (email, password) VALUES (?, ?)'''
        cur.execute(sql, (sign_up_form.data['email'], str(sign_up_form.data['password'])))
        db.commit()

        # get new user id
        user_id = cur.execute('''SELECT user_id FROM user WHERE email=?''', (sign_up_form.data['email'],))
        user_id = user_id.fetchone()['user_id']

        # create interests
        sql = '''INSERT INTO interests (user_id) VALUES (?)'''
        cur.execute(sql, (user_id,))
        db.commit()
        cur.close()

        # redirect to survey
        return redirect(url_for('survey', user_id=user_id))
    print(sign_up_form.errors)
    return render_template('signup.html', form=sign_up_form)


def create_interests(data):
    interests = [0, 0, 0, 0, 0, 0]
    if 'seminars' in data:
        interests[0] = 1
    if 'workshops' in data:
        interests[1] = 1
    if 'job_networking' in data:
        interests[2] = 1
    if 'workouts' in data:
        interests[3] = 1
    if 'social_events' in data:
        interests[4] = 1
    if 'art' in data:
        interests[5] = 1
    return interests


@application.route('/<user_id>/survey', methods=['GET', 'POST'])
def survey(user_id):
    form = forms.SurveyForm()
    if form.validate_on_submit():
        cur = db.cursor()
        cur.execute('''UPDATE user SET college=?, secondary_college=?, degree_level=? WHERE user_id=?''',
                    (form.data['college'], form.data['college_secondary'], form.data['standing'], user_id))
        update = '''UPDATE interests 
                    SET seminars=?, workshops=?, job_networking=?, workouts=?, social_events=?, arts=? 
                    WHERE user_id=?'''
        params = tuple(create_interests(form.data['interests'])) + (user_id,)
        cur.execute(update, params)
        db.commit()
        return redirect(url_for('results', user_id=user_id))
    return render_template('survey.html', form=form)


@application.route('/<user_id>/results', methods=['GET'])
def results(user_id):
    cur = db.cursor()
    interests = cur.execute('''SELECT seminars, workshops, job_networking, workouts, social_events, arts FROM interests WHERE user_id=?''', (user_id,))
    interests = interests.fetchone()
    interest_list = []
    for key in interests.keys():
        if interests[key] == 1:
            interest_list.append(key)

    results = recommend(interest_list)

    return render_template('results.html', events=results)


if __name__ == '__main__':
    application.run()

