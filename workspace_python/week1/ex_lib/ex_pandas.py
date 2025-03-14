#pip install pandas
#pip install openpyxl
#pip install finance-datareader
#pip install matplotlib
import matplotlib.pyplot as plt
import  pandas as pd
import  FinanceDataReader as fdr
#한국거래소
df_krx = fdr.StockListing("KRX")
print(df_krx.head())
df_krx.to_excel('krx.xlsx', index=False, engine='openpyxl')
#나스닥
df_nasdaq = fdr.StockListing("NASDAQ")
print(df_nasdaq.head())
df_nasdaq.to_excel('nasdaq.xlsx', index=False, engine='openpyxl')
#S&Q500
df_snp =  fdr.StockListing("S&P500")
df_snp.to_excel('s&p.xlsx', index=False,engine='openpyxl')
print(df_snp.head())






#AAPL = fdr.DataReader("AAPL")  #애플 주식 가져옴
#AAPL ['Close'].plot()
#plt.show()
