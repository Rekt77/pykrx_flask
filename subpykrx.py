from pykrx import stock

class krxModule:
    tickerList = stock.get_market_ticker_list()
    nameList = map(lambda x : stock.get_market_ticker_name(x),tickerList)
    nameMap = dict(zip(nameList,tickerList))
    
    def getName_by_ticker(self,ticker):
        return self.nameMap[ticker]
