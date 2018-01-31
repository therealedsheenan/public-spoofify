from flask import Flask, render_template, jsonify
from mac_random import randomize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', random_mac_address=randomize())


@app.route('/random-mac')
def random_mac():
    return jsonify(random_mac_address=randomize())
