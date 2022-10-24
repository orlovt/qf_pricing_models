import pandas_datareader.data as pdr
import pandas as pd 


class options_data():
    def full_ticker(ticker):
        ticker = pdr.YahooOptions(ticker)  
        ticker.headers = {'User-Agent': 'Firefox'}
        all_opt = ticker.get_all_data()
        all_opt.reset_index(inplace = True)
        return  all_opt

    def get_ticker_date(ticker, date):
        all_opt = options_data.full_ticker(ticker)
        try: 
            exp_date = all_opt[all_opt.Expiry == date]
        except: 
            exp_date = all_opt[all_opt.Expiry == all_opt.Expiry[1]] 
        
        calls = exp_date[exp_date.Type=='call']
        calls['C'] = (calls.Bid+calls.Ask)/2
        puts = exp_date[exp_date.Type=='put']
        puts['P'] = (puts.Bid+puts.Ask)/2
        df = pd.merge(calls, puts, how='inner', on ='Strike')
        
        return df 


if __name__ == '__main__':
    print(options_data.full_ticker("TSLA"))
    print(options_data.get_ticker_date("SPY", "2022-12-16"))

