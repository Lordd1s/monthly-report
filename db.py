import sqlite3

def create_db():
    with sqlite3.connect('inventory.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                color VARCHAR(10) NULL DEFAULT NULL,
                quantity REAL NOT NULL,
                unit_type VARCHAR(5) NOT NULL,
                date_time_given VARCHAR(15))
            '''
        )
        conn.commit()


class DBInventory:
    def __init__(self):
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()

    def get_products(self):
        self.cursor.execute('SELECT * FROM products ORDER BY date_time_given DESC')
        rows = self.cursor.fetchall()
        print(rows)
        return rows
    
    def add_product(self, *args):
        self.cursor.execute(
            'INSERT INTO products (name, color, quantity, unit_type, date_time_given) VALUES (?,?,?,?,?)',
            args
        )
        self.conn.commit()

    def update_product(self, **kwargs):
        columns = ', '.join([f"{key}=?" for key in kwargs if key != 'id'])
        values = [kwargs[key] for key in kwargs if key != 'id']
        values.append(kwargs['id'])
        sql = f"UPDATE products SET {columns} WHERE id=?"
        self.cursor.execute(sql, values)
        self.conn.commit()
        
    def delete_product(self, id):
        self.cursor.execute('DELETE FROM products WHERE id=?', (id,))
        self.conn.commit()


# if __name__ == '__main__':
    # create_db()
    # print('Database created successfully.')
    # db = DBInventory()
    # db.add_product('Product 1', 'Red', 10, 'm', '2024-07-10')
    # db.update_product(id=1, color='Blue', quantity=20, unit_type='kg', date_time_given='2024-07-10')