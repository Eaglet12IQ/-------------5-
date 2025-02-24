from flask import Flask, jsonify, request, send_from_directory
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.json')

def load_data():
    if not os.path.exists(DB_FILE):
        default_data = {"products": []}
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)
        return default_data

    with open(DB_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"products": []}
    
@app.route('/')
def serve_admin():
    return send_from_directory('../client', 'index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    data = load_data()
    category = request.args.get('category')
    products = data['products']
    if category:
        products = [p for p in products if category in p['categories']]
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=8080)