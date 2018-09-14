from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['number'] = random.randrange(0, 101)
    print(session['number'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    guess = int(guess)
    num = session['number']
    if guess == num:
        return render_template('justRight.html', number = num)
    elif guess > num:
        return render_template('tooHigh.html')
    elif guess < num:
        return render_template('tooLow.html')

@app.route('/replay', methods=['POST'])
def replay():
    print(session['number'])
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)