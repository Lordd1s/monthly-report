import datetime
from db import DBInventory

from flask import Flask, render_template, g, redirect, url_for, request

app = Flask(__name__, static_folder='./static', template_folder='./templates')


def get_db():
    if 'db' not in g:
        g.db = DBInventory()
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.conn.close()


@app.route('/')
def home():
    return render_template('add_product.html')


@app.route('/list_of_given_products')
def list_of_given_products():
    db = get_db().get_products()
    products = [
        {
        'id': product[0],
        'name': product[1],
        'color': product[2],
        'quantity': product[3],
        'unit_type': product[4],
        'date_time_given': product[5],
        'note': product[6]
        } for product in db
    ]
    # print('List of given products:', db.get_products())
    return render_template('list_of_given_products.html', products=products)


@app.route('/add_product', methods=['POST'])
def add_product():
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = request.form.get('productName'),
    color = request.form.get('productColor'),
    quantity = request.form.get('productQuantity'),
    unit_type = request.form.get('productUnit')
    note = request.form.get('productNote')
    db = get_db()
    try:
        db.add_product(
            name=name, 
            color=color, 
            quantity=quantity, 
            unit_type=unit_type, 
            date_time_given=date_time,
            note=note
        )
        return redirect(url_for('home'))
    except Exception as e:
        return render_template('add_product.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
