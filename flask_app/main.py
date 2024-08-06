import datetime
from db.db import get_db

from flask import Flask, render_template, g, redirect, url_for, request

app = Flask(__name__, static_folder='./static', template_folder='./templates')



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


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    db = get_db()
    db.delete_product(product_id)
    return redirect(url_for('list_of_given_products'))


@app.route('/update_product/<int:product_id>', methods=['POST'])
def update_product(product_id):
    name = request.form.get('productName'),
    color = request.form.get('productColor'),
    quantity = request.form.get('productQuantity'),
    unit_type = request.form.get('productUnit'),
    note = request.form.get('productNote')
    db = get_db()
    try:
        db.update_product(
            id=product_id,
            name=name,
            color=color,
            quantity=quantity,
            unit_type=unit_type,
            note=note
        )
        return redirect(url_for('list_of_given_products'))
    except Exception as e:
        return render_template('update_product.html', error=str(e), product_id=product_id)
    
    
if __name__ == '__main__':
    app.run(debug=True)
