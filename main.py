from db import DBInventory

from flask import Flask
from flask.templating import render_template

app = Flask(__name__, static_folder='./static', template_folder='./templates')

DB = DBInventory()


@app.route('/')
def home():

    return render_template('index.html', )




if __name__ == '__main__':
    app.run(debug=True)
