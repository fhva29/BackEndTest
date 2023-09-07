from .models import Dividend
from datetime import datetime

def serialize_dividend(symbol, year):
    dividends = Dividend.objects.filter(symbol=symbol)
    dividends_json = {}

    for dividend in dividends:
        year_db = datetime.strptime(str(dividend.date), "%Y-%m-%d %H:%M:%S%z").year
        if year_db == int(year):
            if year_db not in dividends_json:
                dividends_json.update({year_db: round(dividend.value, 5)})
            else:
                dividends_json[year_db] += round(dividend.value, 5)
    
    return dividends_json