from flask import Flask, jsonify, request, render_template
#Capital letter in 'Flask' indicates they are Class objects
#'Module' means any Python file with .py extensions.

#What is __name__ function do? https://www.freecodecamp.org/news/if-name-main-python-example/
app = Flask(__name__)

#json is essentially text/string - jsonify() takes dictionary and convert them into string
stores = [
    {
        'name': 'storename',
        'items': [
            {
            'name': 'itemname',
            'price': 15.99
            }
        ]
    }
]


@app.route("/")
def home():
    return render_template('index.html')

# POST - to insert/update data
# GET - to retreive data

#POST /store data: {name:}

#get_json() is an reverse of jsonify(), which is converting json to dictionary
#request package allows to use HTTP 'methods'
@app.route("/store", methods =["Post"])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string: name>
@app.route("/store/<string:name>") # 'http://127.0.0.1:5000/store/some_name' and some_name will be name variable
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

#GET /store
@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

#GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})


app.run(port=5000)
