from pykrx import stock
import pandas as pd
import numpy as np

class krxModule():
    tickerList = stock.get_market_ticker_list()
    nameList = map(lambda x : stock.get_market_ticker_name(x),tickerList)
    nameMap = dict(zip(nameList,tickerList))

    #key==index
    #value==dictionary{colums:value}
    def to_dict(self,df):
        return {df.iloc[i].name:df.iloc[i,:].to_dict() for i in range(len(df))}
    
    def chartJSON(self,dic):
        tmp_dic = {ticker["종목명"]:ticker["등락률"] for _,ticker in dic.items()}
        labels = list(tmp_dic.keys())
        datas = list(tmp_dic.values())
        rand = [[np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)] for _ in range(len(labels))]
        backgroundColors = ['rgba(%d,%d,%d,0.2)'%(rand[i][0],rand[i][1],rand[i][2]) for i in range(len(labels))]
        borderColors = ['rgba(%d,%d,%d,1)'%(rand[i][0],rand[i][1],rand[i][2]) for i in range(len(labels))]
        json_ = {
            'type': 'bar',
            'data': {
                'labels': labels,
                'datasets': [{
                    'label': '등락률',
                    'data': datas,
                    'backgroundColor': backgroundColors,
                    'borderColor': borderColors,
                    'borderWidth': '1'
                }]
            },
            'options': {
                'responsive': False,
                'scales': {
                    'yAxes': [{
                        'ticks': {
                            'beginAtZero': True
                        }
                    }]
                },
            }
        }
        return json_
    
    def getName_by_ticker(self,ticker):
        return self.nameMap[ticker]

    def getTop10(self,start,end):
        df = stock.get_market_price_change_by_ticker(start,end)
        return self.to_dict(df.sort_values("등락률",ascending=False).head(10))
