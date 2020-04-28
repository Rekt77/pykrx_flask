from pykrx import stock
import pandas as pd
import itertools

nameList = list()

#tickers = stock.get_market_ticker_list()
#for each in map(lambda x : stock.get_market_ticker_name(x),tickers):
#    nameList.append(each)

# 랭킹 매길때
df = stock.get_market_price_change_by_ticker("20200428", "20200428")
#print(df.sort_values('등락률',ascending=False))
df = {df.iloc[i].name:df.iloc[i,:].to_dict() for i in range(len(df))}
for i in itertools.islice(df.items(),2):
    print(i)
#print({df.iloc[i].name:df.iloc[i,:].to_dict() for i in range(3)})


#종목별 그래프 그릴 때
df = stock.get_market_ohlcv_by_date("20200401", "20200402", "950140", "d")
#print(df.head(3))