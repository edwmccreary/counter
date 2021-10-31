from flask import Flask, render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = 'beetlejuice! beetlejuice! beetlejuice!'

@app.route('/')
def index():
        
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    
    if not 'increment' in session:
        session['increment'] = 1

    if 'counter' in session:
        session['counter'] += session['increment']
    else:
        session['counter'] = 1

    return render_template("index.html",counter = session['counter'],visits = session['visits'],increment = session['increment'])

@app.route('/add', methods=['POST'])
def add_to_counter():
    print(request.form)
    session['increment'] = int(request.form['add_amount'])
    return redirect("/")

@app.route('/reset_count')
def reset_count():
    session.pop('counter')
    session['visits'] -= 1 #prevent visits from increasing and only reset the counter
    return redirect("/")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)