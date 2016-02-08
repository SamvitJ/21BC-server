import json

from flask import Flask, request

# import from the 21 Bitcoin Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# sort method w/out delay simulates faster computation server
def fast_get_element(arr, prop, val):
    for elem in arr:
        if elem[prop] == val:
            return elem

def get_array_to_sort(request):
    return json.loads(request.form.getlist("array")[0])

@app.route('/fastfind', methods=['GET', 'POST'])
@payment.required(800)
def fast_get_elem():
    arr = get_array_to_sort(request)
    prop = request.form.getlist("property")[0]
    value = int(request.form.getlist("value")[0])
    res = fast_get_element( arr, prop, value )
    return json.dumps({"elem": str(res)})

# set up and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
