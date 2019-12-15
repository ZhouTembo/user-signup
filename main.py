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
    usererror=''
    passworderror=''
    password_error=''
    email_error=''
    
    
    if len(password)<4 or len(password)>20 :
        passworderror='Not a valid password'

        
        password=""
        vpassword=""
    
    if  password!=vpassword:
        

        password_error = 'Passwords do not match'
        password=""
        vpassword=""
        
    
    if len(user_name)<4 or len(user_name)>20 :
        usererror='Not a valid username'
        password=""
        vpassword=""
        
         
    if email>'':
        if '@' not in email or '.' not in email:
            email_error="That's not a valid email"
        
        else:
            email=''

    if email_error=='' and usererror=='' and password_error=='' and passworderror=='':
        return render_template('welcome.html', home=user_name)
    else:
        return render_template('main_form.html',passworderror=passworderror,password_error=password_error,password=password,vpassword=vpassword, home=user_name,book=email,email_error=email_error, usererror=usererror)




app.run()