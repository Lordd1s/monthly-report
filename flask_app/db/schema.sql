#############################################################

#                WORKS ON SQLite3 DATABASE

#############################################################




# Products for_counting
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_number INTEGER NOT NULL,
    name TEXT NOT NULL,
    color VARCHAR(10) NULL DEFAULT NULL,
    quantity REAL NOT NULL,
    unit_type VARCHAR(20) NOT NULL,
    product_weight VARCHAR(10) NULL DEFAULT NULL,
    date_time_added VARCHAR(25) NOT NULL,
    note TEXT NULL DEFAULT NULL
)

#  Products sizes (S, XL, etc...)
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_number INTEGER NOT NULL
    FOREIGN KEY (contract_number) REFERENCES products(id),
    clothes_name TEXT NOT NULL,
    color VARCHAR(10) NULL DEFAULT NULL,
    size_name TEXT NOT NULL,
    size_number INTEGER NULL DEFAULT NULL
)

#  Products to_give to_shop
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS products_to_give (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL
    FOREIGN KEY (product_id) REFERENCES products(id),
    name TEXT NOT NULL,
    color VARCHAR(10) NULL DEFAULT NULL,
    quantity REAL NOT NULL,
    unit_type VARCHAR(5) NOT NULL,
    date_time_given VARCHAR(25) NOT NULL,
    note TEXT NULL DEFAULT NULL
)

#  Products shipments
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS product_shipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL
    FOREIGN KEY (product_id) REFERENCES products(id),
    shipment_date VARCHAR(25) NOT NULL,
    note TEXT NULL DEFAULT NULL,
    quantity REAL NOT NULL
)

#  Records 
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    product_id INTEGER NULL DEFAULT NULL
    FOREIGN KEY (product_id) REFERENCES products(id),

    products_to_give INTEGER NULL DEFAULT NULL
    FOREIGN KEY (products_to_give) REFERENCES products_to_give(id),

    record_datetime VARCHAR(25) NOT NULL,
    operation TEXT NOT NULL
)