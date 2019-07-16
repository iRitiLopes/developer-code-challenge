from flask import Flask
from flask import render_template
import model

app = Flask(__name__)

@app.route('/')
def index():
    dps = model.atk_dps()
    print(dps)
    return render_template('index.html', columns=dps.columns.values, rows=dps.round(2).values.tolist())

