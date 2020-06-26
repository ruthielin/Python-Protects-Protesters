import io

from flask import Flask, render_template, request, Response, send_file
import numpy as np

import cities
import risk_test
import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as figurecanvas, FigureCanvasAgg

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=["POST"])
def home_post():
    text = request.form["city"]
    var = cities.findCities(text)
    return render_template("protests.html", var=var)


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/protests')
# def protests():
#     return render_template('protests.html')


@app.route('/protests', methods=["POST", "GET"])
def protests_get():
    return "yay"
    # return render_template('protests.html')


@app.route('/risk')
def risk():
    return render_template('risk.html')


@app.route('/risk', methods=["POST"])
def risk_post():
    code = request.form["location"]
    numcode = int(code)
    # var2 = "dog"
    var2 = risk_test.get_risk(numcode)
    return render_template("results.html", var2=var2)

    # text = request.form["city"]
    # var = cities.findCities(text)
    # return render_template("protests.html", var=var)


# def risk_post():
#     code = request.form["county"]
#     var2 = risk_test.get_risk(code)
#     plt.barh(var2[0], var2[1])
#     y_pos = np.arange(len(var2[1]))
#     plt.yticks(y_pos, var2[1])
#     plt.ylabel('FIPS is ' + str(var2[0][0]))
#     plt.xlabel('RISK Level (%)')
#     plt.title('Your approximate risk is ' + str(var2[1][0]) + "%")
#     axes = plt.gca()
#     axes.set_xlim([0, 100])
#     plt.show()
#     plt.savefig("/static/images/new_plot.jpg")
#     return render_template('results.html', name="new_plot", url="/static/images/new_plot.jpg")


@app.route('/results')
def results():
    return render_template('results.html')


# @app.route('/results', methods=["POST", "GET"])
# def results_get():
#     return "yay"
#     # return render_template('results.html')


@app.route('/tips')
def tips():
    return render_template('tips.html')


if __name__ == '__main__':
    app.run(debug=True)
