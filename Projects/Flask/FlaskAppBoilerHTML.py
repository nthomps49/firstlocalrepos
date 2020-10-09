from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
        return render_template("index.html")

@app.route('/add')
def add():
        return render_template('add.html')

if __name__ == '__main__':
        app.run(debug=True) #debug=True allows changes without manual recycle


