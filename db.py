import sqlite3

def create_db():
    with sqlite3.connect('inventory.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS products_to_give (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                color VARCHAR(10) NULL DEFAULT NULL,
                quantity REAL NOT NULL,
                unit_type VARCHAR(5) NOT NULL,
                date_time_given VARCHAR(25),
                note TEXT NULL DEFAULT NULL
            )
            '''
        )
        # cursor.execute(
        #     '''
        #     CREATE TABLE IF NOT EXISTS products_arrival (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         name TEXT NOT NULL,
        #         color VARCHAR(10) NULL DEFAULT NULL,
        #         quantity REAL NOT NULL,
        #         unit_type VARCHAR(5) NOT NULL,
        #         recording_time VARCHAR(25),
        #         note TEXT NULL DEFAULT NULL,
        #         article_number INTEGER NULL DEFAULT NULL,
        #         weight REAL NULL DEFAULT NULL,
        #         composition TEXT NULL DEFAULT NULL,
        #         where_from TEXT NULL DEFAULT NULL
        #         product_code INTEGER NULL DEFAULT NULL
        #     )
        #     '''
        # )  # TODO: Uncomment this block if you want to create a products_arrival table.
        conn.commit()


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
    create_db()
    # print('Database created successfully.')
    # db = DBInventory()
    # db.add_product('Product 1', 'Red', 10, 'm', '2024-07-10')
    # db.update_product(id=1, color='Blue', quantity=20, unit_type='kg', date_time_given='2024-07-10')