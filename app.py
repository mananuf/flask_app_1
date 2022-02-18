from flask import Flask, render_template

app = Flask(__name__) #instance of Flask class

@app.route("/") #directs to home route
def home():
    # return "<h1> server is responding! </h1>"
    return render_template('index.html')


@app.route("/blog") #directs to blog route
def blog():
    return "<h1>Welcome to my blog</h1>"


if __name__ == "__main__":
    app.run(debug = True)