from flask import Flask,render_template,Blueprint,jsonify
from pykrx import stock
from subpykrx import krxModule
from CustomJSONencoder import CustomJSONEncoder
from functools import wraps
import time
app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
module = krxModule()

@app.route("/stock/<ticker>")
def ticker2name(ticker):
    return module.getName_by_ticker(ticker)

@app.route("/all")
def printNameMap():
    return jsonify(module.nameMap)

@app.route("/new")
def printstock():
    df = stock.get_market_price_change_by_ticker("20200427", "20200427")
    return jsonify({df.iloc[i].name:df.iloc[i,:].to_dict() for i in range(len(df))})

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)