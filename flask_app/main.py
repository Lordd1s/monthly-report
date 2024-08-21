import datetime
from db.db import get_db, close_db
from db.db import init_db_command, close_db

from flask import Flask, render_template, g, redirect, url_for, request

from utils.exceptions import NotExistsError

app = Flask(__name__, static_folder='./static', template_folder='./templates')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

init_app(app)


@app.route('/')
def home():
    return render_template('add_product.html')

# products_to_give table
@app.route('/list_of_given_products')
def list_of_given_products():
    db = get_db().get_given_products()
    products = [
        {
        'name': product[0],
        'color': product[1],
        'quantity': product[2],
        'unit_type': product[3],
        'date_time_given': product[4],
        'note': product[5]
        } for product in db
    ]
    # print('List of given products:', db.get_given_products())
    close_db()
    return render_template('list_of_given_products.html', products=products)


@app.route('/add_product_to_give/<str:product_name>', methods=['POST'])
def add_product_to_give(product_name):
    """
    Add a product to the 'products_to_give' table!
    """

    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = request.form.get('productName'),
    color = request.form.get('productColor'),
    quantity = request.form.get('productQuantity'),
    unit_type = request.form.get('productUnit')
    note = request.form.get('productNote')
    db = get_db()
    product_id = db.get_product_id(product_name)

    if not product_id:
        raise NotExistsError
    
    try:
        db.add_product_to_give(
            product_id=product_id,
            name=name, 
            color=color, 
            quantity=quantity, 
            unit_type=unit_type, 
            date_time_given=date_time,
            note=note
        )
        return redirect(url_for('home'))
    except Exception as e:
        return render_template('add_product.html', error='Ошибка при добавлении! Полное сообщение: ' + str(e))
    finally:
        close_db()


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product_to_give(product_id):
    """
    Delete a product from the 'products_to_give' table!
    """

    try:
        db = get_db()
        db.delete_product(product_id)
        return redirect(url_for('list_of_given_products'))
    except Exception as e:
        return render_template('delete_product.html', error='Ошибка при удалении! Полное сообщение: ' + str(e))
    finally:
        close_db()


@app.route('/update_product_to_give/<int:product_id>', methods=['POST'])
def update_products_to_give(product_id):
    """
    Update a product in the 'products_to_give' table!
    """

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
    finally:
        close_db()


# Products table
@app.route('/list_of_products')
def list_of_products():
    try:
        db = get_db().get_all_products()
        products = [
            {
            'id': product[0],
            'name': product[1],
            'contract_number': product[2],
            'color': product[3],
            'quantity': product[4],
            'unit_type': product[5],
            'product_weight': product[6],
            'date_time_arrived': product[7],
            'note': product[8]
            } for product in db
        ]
        return render_template('list_of_products.html', products=products)
    except Exception as e:
        return render_template('list_of_products.html', error='Ошибка при получении списка продуктов! Полное сообщение: ' + str(e))
    finally:
        close_db()


@app.route('/add_products_arrived', methods=['POST'])
def add_products_arrived():
    form = request.form

    name = form.get('productName')
    contract_number = form.get('contract_number')
    color = form.get('productColor')
    quantity = form.get('productQuantity')
    unit_type = form.get('productUnit')
    product_weight = form.get('productWeight')
    date_time_arrived = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = form.get('productNote')
    try:
        db = get_db()
        db.add_products(
            name=name,
            contract_number=contract_number,
            color=color,
            quantity=quantity,
            unit_type=unit_type,
            product_weight=product_weight,
            date_time_arrived=date_time_arrived,
            note=note
        )
        return redirect(url_for('list_of_products'))
    except Exception as e:
        return render_template('add_products_arrived.html', error='Ошибка при добавлении продукта! Полное сообщение: ' + str(e))
    finally:
        close_db()
        

if __name__ == '__main__':
    app.run(debug=True)
