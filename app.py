from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
products = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

# GET all products
@app.route('/products', methods=['GET'])
def get_products():
    print("Hello users.. I am Aditya the developer")
    return jsonify(products)

# GET single product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else ('', 404)

# POST a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

# DELETE a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
