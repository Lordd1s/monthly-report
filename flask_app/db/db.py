import sqlite3
import click

from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = DBInventory()
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized database.')


class DBInventory:
    def __init__(self):
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()

    def get_products(self, params=None):
        # params = 'products_to_give' if params is None else 'products_arrival'  # If 'products_arrival' has to be implemented
        self.cursor.execute('SELECT * FROM products_to_give')
        rows = self.cursor.fetchall()
        return rows
    
    def add_product(self, **kwargs):
        kwargs = {k: v[0] if isinstance(v, tuple) else v for k, v in kwargs.items()}   
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?'] * len(kwargs))
        values = list(kwargs.values())
        query = f'INSERT INTO products_to_give ({columns}) VALUES ({placeholders})'
        self.cursor.execute(query, values)
        self.conn.commit()

    def update_product(self, **kwargs):
        columns = ', '.join([f"{key}=?" for key in kwargs if key != 'id'])
        values = [kwargs[key] for key in kwargs if key != 'id']
        values.append(kwargs['id'])
        sql = f"UPDATE products_to_give SET {columns} WHERE id=?"
        self.cursor.execute(sql, values)
        self.conn.commit()
        
    def delete_product(self, id):
        self.cursor.execute('DELETE FROM products_to_give WHERE id=?', (id,))
        self.conn.commit()


# if __name__ == '__main__':
    # db = DBInventory()
    # db.add_product('Product 1', 'Red', 10, 'm', '2024-07-10')
    # db.update_product(id=1, color='Blue', quantity=20, unit_type='kg', date_time_given='2024-07-10')