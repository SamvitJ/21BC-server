from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/AmIBehindProxy")
def areyouaproxy():
    if "X-Forward-For" in request.headers:
	    return "Yes, You are behind a proxy\n"
    else:
        return "I didn't see any evidence of a proxy\n"

if __name__ == "__main__":
    app.run()
