from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Mock user data for login
users = {'testuser': 'password123'}

# Route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials. Please try again.'
    
    return render_template('login.html')

# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Implement registration logic here
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

# Route for consultation page
@app.route('/consultation')
def consultation():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('consultation.html')

# Route for logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
