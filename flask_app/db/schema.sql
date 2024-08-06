CREATE TABLE IF NOT EXISTS products_to_give (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    color VARCHAR(10) NULL DEFAULT NULL,
    quantity REAL NOT NULL,
    unit_type VARCHAR(5) NOT NULL,
    date_time_given VARCHAR(25),
    note TEXT NULL DEFAULT NULL
)

CREATE TABLE IF NOT EXISTS products_arrival (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    color VARCHAR(10) NULL DEFAULT NULL,
    quantity REAL NOT NULL,
    unit_type VARCHAR(5) NOT NULL,
    recording_time VARCHAR(25),
    note TEXT NULL DEFAULT NULL,
)

PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS size (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    products_arrival_id INTEGER NOT NULL
    FOREIGN KEY (products_arrival_id) REFERENCES products_arrival(id)
    size_name TEXT NOT NULL,
    size_number INTEGER NULL DEFAULT NULL
)