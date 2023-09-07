from .models import Dividend
import yfinance as yf
from datetime import datetime
from pandas import Series

class YahooFinance:
    @staticmethod
    def check_finance_data(symbol, date, value):
        if Dividend.objects.filter(symbol=symbol, date=date, value=value):
            return True
        return False


    @staticmethod
    def get_finance_data(symbol):
        try:
            dividends = yf.Ticker(symbol).dividends
        except Exception as err:
            return {"success": False, "text": f"An error occurred: {str(err)}"}
        else:
            if type(dividends) == Series:
                for date, value in dividends.items():
                    if not YahooFinance.check_finance_data(symbol, date, value):
                        dividend = Dividend(symbol=symbol, date=date, value=value)
                        dividend.save()
                return {"success": True, "text": "Database populated successfully!"}
            else:
                return {"success": False, "text": f"The symbol {symbol} not exists!"}

        
