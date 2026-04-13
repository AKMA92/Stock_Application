import json

import requests


class Downloader:
    stock = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=compact&apikey=DEIN_KEY"
    #stock2 = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=compact&apikey=DEIN_KEY"
    #stock3 = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=compact&apikey=DEIN_KEY"

    def __init__(self):
        pass

    def get_data(self):

        try:
            response = requests.get(self.stock)
            json_data = json.loads(response.text)

        except Exception as e:
            print(e)

        return json_data



