## Flask App Routing


from flask import Flask

## create a simple flask application

app=Flask(__name__)

@app.route("/", methods=["GET"])

def welcome():
    return "<h2>Welcome to New World</h2>"

@app.route("/index", methods=["GET"])

def index():
    return "Welcome to  Index World"




if __name__=="__main__":
    app.run(debug=True)