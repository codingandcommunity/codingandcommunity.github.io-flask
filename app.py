import os
from flask import Flask, render_template, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')

def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "content.json")
    data = json.load(open(json_url))
    return render_template('index.html', data=data["landing_page"])
