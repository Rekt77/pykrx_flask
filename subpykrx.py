from pykrx import stock
import pandas as pd

class krxModule():
    tickerList = stock.get_market_ticker_list()
    nameList = map(lambda x : stock.get_market_ticker_name(x),tickerList)
    nameMap = dict(zip(nameList,tickerList))

    #key==index
    #value==dictionary{colums:value}
    def to_dict(self,df):
        return {df.iloc[i].name:df.iloc[i,:].to_dict() for i in range(len(df))}
    
    def getName_by_ticker(self,ticker):
        return self.nameMap[ticker]

    def getTop10(self,start,end):
        df = stock.get_market_price_change_by_ticker(start,end)
        return self.to_dict(df.sort_values("등락률",ascending=False).head(10))