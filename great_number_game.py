from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'random' in session:
        print('random number already generated!')
        print(session['random'])
    else:
        print('random number generated!')
        session['random'] = random.randint(1,100)
        print(session['random'])
    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess():
    print('a guess was made!')
    print(request.form)
    session['is_too_low'] = False
    session['is_too_high'] = False
    session['is_equal'] = False

    # if too low
    if int(request.form['number_guess']) < session['random']:
        print('it\'s too low!!!')
        session['is_too_low'] = True

    # if too high
    if int(request.form['number_guess']) > session['random']:
        print('it\'s too high!!!')
        session['is_too_high'] = True

    # if equal
    if int(request.form['number_guess']) == session['random']:
        print('it\'s equal!!!')
        session['is_equal'] = True

    return redirect('/')





if __name__=="__main__":   
    app.run(debug=True)    