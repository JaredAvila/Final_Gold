from flask import Flask, render_template, redirect, request, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "walla-walla"

@app.route('/')
def indext():
    try:
        if session['gil'] > 0:
            print(session['list'])
            return render_template('index.html', gil=session['gil'], activities = session['list'])
        else:
            session['gil'] = 0
            return render_template('index.html', gil=session['gil'], activities = session['list'])
    except:
        print("new game")
        session['gil'] = 0
        session['list'] = ["<p>Activity Log</p>"]
        return render_template('index.html', gil=session['gil'], activities = session['list'])

@app.route('/process', methods=['POST'])
def process():
    x = datetime.datetime.now()
    if request.form["postType"] != 'Gold Saucer':
        session['board'] = request.form['postType']
        if session['board'] == 'farm':
            session['tempGil'] = random.randrange(10, 21)
        elif session['board'] == 'cave':
            session['tempGil'] = random.randrange(5, 11)
        elif session['board'] == 'house':
            session['tempGil'] = random.randrange(2, 6)
        print(session['tempGil'])
        session['gil'] += session['tempGil']
        session['list'].append("<p id='plus'>Entered a "+session['board']+" and earned "+str(session['tempGil'])+" gil at: "+ x.strftime("%Y")+"/"+ x.strftime("%m")+"/"+ x.strftime("%d") + " "+ x.strftime("%I")+ ":"+ x.strftime('%M') + "  " +  x.strftime("%p").lower() +"</p>")
        return redirect('/')
    elif request.form['postType'] == 'Gold Saucer':
        session['tempGil'] = random.randrange(-50, 51)
        session['gil'] += session['tempGil']
        session['board'] = request.form['postType']
        if session['tempGil'] >= 0:
            session['list'].append("<p id='plus'>Entered the "+session['board']+" and earned "+str(session['tempGil'])+" gil at: "+ x.strftime("%Y")+"/"+ x.strftime("%m")+"/"+ x.strftime("%d") + "  "+ x.strftime("%I")+ ":"+ x.strftime('%M') + "  " +  x.strftime("%p").lower() +"</p>")
            return redirect('/')
        elif session['tempGil']<0:
            session['list'].append("<p id='minus'>Entered the "+session['board']+" and lost "+str(session['tempGil'])+" gil at: "+ x.strftime("%Y")+"/"+ x.strftime("%m")+"/"+ x.strftime("%d") + "  "+ x.strftime("%I")+ ":"+ x.strftime('%M') + "  " + x.strftime("%p").lower() +"</p>")
            return redirect('/')
@app.route('/reset', methods=["POST"])
def reseet():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
