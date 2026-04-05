from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()


def read_json(product_id=None):
    with open('products.json', 'r') as f:
        products = json.load(f)

    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return None, "Product not found"

    return products, None


def read_csv(product_id=None):
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return None, "Product not found"

    return products, None


def read_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id is not None:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")

        rows = cursor.fetchall()
        conn.close()

        if product_id is not None and not rows:
            return None, "Product not found"

        products = [dict(row) for row in rows]
        return products, None

    except sqlite3.Error as e:
        return None, f"Database error: {str(e)}"


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        data, error = read_json(product_id)
    elif source == 'csv':
        data, error = read_csv(product_id)
    elif source == 'sql':
        data, error = read_sql(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if error:
        return render_template('product_display.html', error=error)

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
