query_1 = """CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    password VARCHAR(60)
);"""
query_2 = """CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    message TEXT
);"""
query_3 = """CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    description TEXT,
    price DECIMAL(7, 2)
);"""
query_4 = """CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    description TEXT
);"""
query_5 = """CREATE TABLE ItemsOrders (
    id SERIAL PRIMARY KEY,
    item_id int REFERENCES items(id) ON DELETE CASCADE,
    order_id int REFERENCES orders(id) ON DELETE CASCADE
);"""
query_6 = "SELECT * from items WHERE price > 13.00;"
query_7 = "INSERT INTO orders(description) VALUES ('przykładowy opis');"
query_8 = "DELETE FROM users WHERE id = 7;"
query_9 = "SELECT users.name as User_name, users.id as User_id, messages.message as User_message FROM users JOIN messages
    ON users.id=messages.user_id;""
query_10 = "ALTER TABLE messages ADD date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"