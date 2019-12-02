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
    book=''
    email=request.form['email']
    user_name=request.form['username']
    home=''
    print (user_name)
    
    if len(password)<4 and password!=vpassword and '@' not in email or '.' not in email and email>'':
        passworderror='Not a valid password'

        password_error = 'Passwords do not match'
        password=""
        vpassword=""
        email_error="That's not a valid email"
    
        
        return render_template('main_form.html',home=user_name,book=email,email_error=email_error,password_error=password_error, passworderror=passworderror)
    if len(password)<4 :
        passworderror='Not a valid password'
        password_error =''
        password=""
        vpassword=""
        
        return render_template('main_form.html',home=user_name,book=email,password_error=password_error, passworderror=passworderror)
    if password!=vpassword:
        passworderror=''

        password_error = 'Passwords do not match'
        password=""
        vpassword=""
        return render_template('main_form.html',home=user_name,book=email,password_error=password_error, passworderror=passworderror)
    if email>'':
        if '@' not in email or '.' not in email:
            email_error="That's not a valid email"
            return render_template('main_form.html',home=user_name,book=email,email_error=email_error)
        else:
        
            return '<h1>Hello, Mia'  '</h1>'
    else:
        
        return '<h1>Hello, Mia'  '</h1>'







app.run()