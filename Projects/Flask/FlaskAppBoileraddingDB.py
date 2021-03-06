from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from logging import DEBUG
from datetime import datetime
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#hardcoding key is okay in dev but in prod need to store it in a protected file and input it to flask app
app.secret_key = b'w\xbeR>\xf0\x8epN'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.logger.setLevel(DEBUG)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"

feedback= []

def store_feedback(url):
        feedback.append(dict(
                url=url,
                user='Loonycorn',
                date= datetime.utcnow()
        ))

@app.route('/')
@app.route('/index')
def home():
        return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add():
        if request.method == 'POST':
                url = request.form['url']
                store_feedback(url)
                app.logger.debug('stored feedback: ' + url)
                #call flash function 
                flash("Your Feedback : " + url)
                #redirect the user to the home page after submitting the feedback
                return redirect(url_for('home'))
                
        return render_template('add.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created!')
        return redirect(url_for('login'))
        
    if form.errors:
        flash('Validation Errors: ' + str(form.errors))
        app.logger.error('ValidationError:\n' + str(form.errors))
    return render_template('register.html', title= 'Register', form= form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@loonycorn.com' and form.password.data == 'loony':
            flash('Logged in!')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful')
    return render_template('login.html', title= 'Login', form = form)

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

if __name__ == '__main__':
        app.run(debug=True) #debug=True allows changes without manual recycle


