from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


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


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        data, error = read_json(product_id)
    elif source == 'csv':
        data, error = read_csv(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if error:
        return render_template('product_display.html', error=error)

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
