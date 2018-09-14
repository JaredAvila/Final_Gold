from flask import Flask, render_template, redirect, request, session, flash
import re
app = Flask(__name__)
app.secret_key = "whatever"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
@app.route('/validate', methods=['POST'])
def validate():
    session['fName'] = request.form['fName']
    session['lName'] = request.form['lName']
    session['email'] = request.form['email']
    password = request.form['password']
    conf_password = request.form['conf_password']
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


    #name check

    if request.form['fName'] == '' or request.form['lName'] == '':
        print('name is blank')
        flash('Name cannot be blank', 'name')
    elif request.form['fName'].isalpha() == False or request.form['lName'].isalpha() == False:
        print('name contains numbers')
        flash('Name can only contain alphabetic characters', 'name')
    else:
        print('name is valid')

    #email check

    if len(request.form['email']) < 1:
        print('email is blank')
        flash('Email cannot be blank', 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        print('not a valid email')
        flash('Email is not valid', 'email')
    else:
        print('email is valid.')

    
    #password check

    if len(password) < 1 or len(conf_password) < 1:
        print('password blank')
        flash('Password cannot be left blank', 'password')
    elif len(password) < 8:
        print('too short, aint gettin it')
        flash('Password too short')
    elif password != conf_password:
        print('passwords no matchy ')
        flash('Passwords do not match', 'password')
    elif password.isalpha() == True:
        print("password has no numbers")
        flash('Password must contain at least one letter and one number', 'password')
    else:
        print('valid password')
    
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        flash('Congratulations! You are now registered.')
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
    
    
    
    
    # if int(len(request.form['password'])) < 1 or int(len(request.form['conf_password'] < 1)):
    #     print('password is blank')
    #     flash('Password cannot be left blank')
    # elif len(request.form['password']) < 8:
    #     print('password is too short')
    #     flash('Password is too short')
    # elif request.form['password'] != request.form['conf_passord']:
    #     print('passwords dont match')
    #     flash('Passwords do not match')
    # else:
    #     print('password is valid')