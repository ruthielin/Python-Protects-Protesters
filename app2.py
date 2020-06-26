from flask import Flask, render_template, request

import cities

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=["POST"])
def home_post():
    text = request.form["city"]
    return cities.findCities(text)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/protests')
def protests():
    return render_template('protests.html')


@app.route('/protests', methods=["POST", "GET"])
def protests_get():
    return "yay"
    # return render_template('protests.html')


@app.route('/risk')
def risk():
    return render_template('risk.html')


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)

