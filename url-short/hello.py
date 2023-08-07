from flask import Flask, render_template, request

app = Flask(__name__) ## the name of the module currently holds

@app.route('/') ## The url for the homepage.
def home():
    return render_template("home.html", name="Nick")

@app.route('/your-url', methods=["GET","POSt"])
def your_url():
    if request.method == "POST":
        return render_template("url.html",code = request.form["code"])
    else:
        return "This is not valid."