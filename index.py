from flask import Flask, render_template, jsonify
from mac_random import randomize
import pyperclip

app = Flask(__name__)

@app.route('/')
def index():
    random_mac_address=randomize()
    pyperclip.copy(random_mac_address)
    return render_template('index.html', random_mac_address=random_mac_address)


@app.route('/random-mac')
def random_mac():
    return jsonify(random_mac_address=randomize())
