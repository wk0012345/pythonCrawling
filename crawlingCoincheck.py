import urllib3 as urllib
import json
import datetime
import time

class crawlingCoincheck:

    http = urllib.PoolManager()

    #defind of URL
    url = "https://coincheck.com/api/ticker.json?pair=btc_jpy"

    #defind of exchange
    exchange = "coincheck"

    #defind of Key
    apiPriceKey = 'last'

    def getPrice(self):

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
   
        urllib.disable_warnings()
        response = self.http.request('Get',self.url)

        #server check
        if response.status != 200:
            return False

        data = response.data.decode('utf-8')
        data = json.loads(data)

        priceData = data[self.apiPriceKey]

        #Api check
        if priceData is None:
            return False

        result = {"price": priceData, "exchange": self.exchange, "time": st}
        return result