from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
    <style>
        .error {{ color: purple; }}
    </style>
    <h1>Signup</h1>
        <form action="/validate-form" method="post">
            <label for="username">Username</label>
            <input id="username" type="text" name="user_name" />
            
            <br><label for="password">Password</label>
            <input id="password" type="password" name="password" />
            
           <br><label for="vpassword">Verify Password</label>
            <input id="vpassword" type="password" name="vpassword" />
            <span class="error">{password_error}</span>
           <br><label for="email">Email (optional)</label>
            <input id="email" type="email" name="email" />
           
            <br><input type="submit" />
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format(password_error='')





@app.route('/validate-form', methods=["POST"])
def display_time_form():
    password = request.form['password']
    vpassword = request.form['vpassword']

    password_error = ''
    

    if password!=vpassword:
        password_error = 'Passwords do not match'
        password=""
        vpassword=""
        return form.format(password_error=password_error,
            password=password,
            vpassword=vpassword)
        
    else:
        username = request.form['user_name']
        return '<h1>Hello, ' + username + '</h1>'







app.run()