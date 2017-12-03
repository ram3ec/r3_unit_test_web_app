from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'secret_key'

#функция проверки что пользователь аутентифицировался
def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are not logged in.'

@app.route('/page1')
def page1() -> str:
    if not check_logged_in():
        return 'You are NOT logged in.'
    return 'This is page 1.'

@app.route('/page2')
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
def page3() -> str:
    return 'This is page 3.'

if __name__ == '__main__':
    app.run(debug=True)