from flask import Flask, request, render_template




app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('main_form.html')





@app.route('/validate-form', methods=["POST"])
def display_time_form():
    password = request.form['password']
    vpassword = request.form['vpassword']

    password_error = ''
    

    if password!=vpassword:
        password_error = 'Passwords do not match'
        password=""
        vpassword=""
        return render_template('main_form.html',password_error=password_error,
            password=password,
            vpassword=vpassword)
        
    else:
        username = request.form['user_name']
        return '<h1>Hello, ' + username + '</h1>'







app.run()