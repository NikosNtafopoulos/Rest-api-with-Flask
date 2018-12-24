from flask import Flask, jsonify

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
    pass

# get single store


@app.route('/store/<string:name>',)
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    # get all stores
     # jsonify -> convert the stores variable into json
    return jsonify({'stores': stores})

# create an item in the store


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
    pass

# get form store the item


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)
