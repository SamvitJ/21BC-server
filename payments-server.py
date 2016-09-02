import time
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
    response.headers['Access-Control-Expose-Headers'] = 'Rate, Expiration, Scheme_id'
    return response

## Free access
@app.route('/')
def endpoint_free():
    print("REQUEST (FREE) HEADERS ----------")
    print(request.headers)
    return "Welcome to the free access endpoint\n"

## Payable endpoint - initial fee
@app.route('/payable', methods=['GET', 'PUT'])
@payment.required(100, Rate=10, Expiration=0.00069444)
def endpoint_payable():
    print("REQUEST (PAYABLE) HEADERS ----------")
    print(request.headers)
    return "Welcome to the payable endpoint\n"

## Payable endpoint - time-rated
@app.route('/payable/timerated', methods=['GET', 'PUT'])
@payment.required(10)
def endpoint_payable_timerated():
    print("REQUEST (PAYABLE, TIME-RATED) HEADERS ----------")
    print(request.headers)
    return 'Thanks for using the payable endpoint\n'

## Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
