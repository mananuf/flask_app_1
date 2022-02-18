from flask import Flask, render_template

app = Flask(__name__) #instance of Flask class

@app.route("/") #directs to home route
def home():
    # return "<h1> server is responding! </h1>"
    return render_template('index.html')


@app.route("/blog") #directs to blog route
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run(debug = True)