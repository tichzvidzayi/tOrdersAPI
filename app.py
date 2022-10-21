from flask import Flask, jsonify,request, json

app = Flask(__name__)
#@app.route('/') 
#def home():
#    return "therefore "
inp = open('myfile.json')
stores = json.load(inp)

#API data

'''
stores = [    
 {
        'name':'MrPrice',
        'items': [
                   {  'name':'Shoes','price': 499 }
                 ]
},
 {
        'name':'Ackermans',
        'items': [
                   { 'name':'Shoe','price': 799 }
                 ]
}

] 
'''

def Update():
  out_file = open("myfile.json", "w")
  json.dump(stores, out_file, indent = 4) 
  out_file.close()


#POST/ store data
@app.route('/store',methods=['POST'] )
def create_store():
    req_data = request.get_json()
    new_data = {
        'name': req_data['name'],
        'items':[]
    }
    stores.append(new_data)
    Update()
    return jsonify(new_data)
   
#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for element in stores:
        if(element['name']== name):
            return jsonify(element)
        else:
            return jsonify({'message':"Store record does not exist"})

#GET store
@app.route('/store')
def get_stores():
    return jsonify(stores)

#POST store/<string:name>/item(name:,price)
@app.route('/store/<string:name>/item',methods=['POST'] )
def create_item_in_store(name):
    req_data= request.get_json()
    for element in stores:
        if (element['name']== name):
           
           new_data = {
           'name': req_data['name'],
           'price': req_data['price']
              }
           stores['items'].append(new_data)
           Update()
           return jsonify(new_data)
        else:
           return jsonify({'message':"Store record does not exist"})
#GET /store/<string:name>/item (name:, Price)
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for element in stores:
        if(element['name']== name):
            return jsonify(element['items'])
        else:
            return jsonify({'message':"Store record does not exist"})
app.run(port=5003)
