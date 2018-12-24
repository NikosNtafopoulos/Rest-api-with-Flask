from flask import Flask, jsonify, request

app = Flask(__name__)
# static data/save to a list
stores = [
    {
        'name': 'My store',
        'item': [
            {
                'name': 'Coffe',
                'price': 5.00
            }
        ]
    }
]


@app.route('/')
def home():
    return "HEEEYYY"

# create a store


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# get single store


@app.route('/store/<string:name>',)
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found'})

# get all stores


@app.route('/store')
def get_stores():
     # jsonify -> convert the stores variable into json
    return jsonify({'stores': stores})

# create an item in the store [item -> name and price]


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['item'].append(new_item)
            return jsonify(new_item)
        return jsonify({'message': 'item not created'})

# get from store the item


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': store['item']})
        return jsonify({'message': 'item not found'})


app.run(port=5000)
