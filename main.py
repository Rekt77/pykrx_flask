from flask import Flask,Blueprint,jsonify,request
from pykrx import stock
from subpykrx import krxModule
from CustomJSONencoder import CustomJSONEncoder
from functools import wraps
import time
app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
module = krxModule()

#refactoring to restAPI
@app.route("/top10",methods=['POST'])
def top10():
    if request.json:
        top10_dict = module.getTop10(request.json['start'],request.json['end'])
        chartJSON = module.chartJSON(top10_dict)
        return jsonify(chartJSON)
    else:
        return jsonify({'msg':'no input vlaue'})

@app.route("/today")
def printstock():
    now = time.strftime('%Y%m%d')
    df = stock.get_market_price_change_by_ticker(now, now)
    return jsonify({df.iloc[i].name:df.iloc[i,:].to_dict() for i in range(len(df))})

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)