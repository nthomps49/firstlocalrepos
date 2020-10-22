from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from logging import DEBUG
from datetime import datetime

app = Flask(__name__)
#hardcoding key is okay in dev but in prod need to store it in a protected file and input it to flask app
app.secret_key = b'w\xbeR>\xf0\x8epN'

app.logger.setLevel(DEBUG)

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

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

if __name__ == '__main__':
        app.run(debug=True) #debug=True allows changes without manual recycle


