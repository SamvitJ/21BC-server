from flask import Flask, request

## Import from the Bitcoin library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

## Create an app
app = Flask(__name__)

## Get the user's wallet 
wallet = Wallet()
payment = Payment(app, wallet)

@app.after_request
def enable_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    return response

## Default: free access
@app.route('/')
def endpoint1():
    print (request.headers)
    return "Welcome to the free access endpoint\n"
    # return json.dumps({"message": "Welcome to the free access endpoint\n"})

## Alternative: payable endpoint
@app.route('/payable')
@payment.required(1000)
def endpoint2():
    print (request.headers)
    return "Welcome to the payable endpoint\n"
    # return json.dumps({"message": "Welcome to the payable endpoint\n"})

## Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(host='10.8.235.166', port=80)
