from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/success', methods=['POST'])
def success():
    data = request.form
    name = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comment = request.form['comment']
    print("got post info")
    print("\n\n","*"*50, "\n\nName:", name)
    print("\n\n","*"*50, "\n\nLocation:", loc)
    print("\n\n","*"*50, "\n\nLanguage:", lang)
    print("\n\n","*"*50, "\n\nComment:", comment)
    print('\n\n',"*"*50)
    return render_template('success.html', name = name, location = loc, language = lang, comment = comment)
if __name__=="__main__":
    app.run(debug=True)