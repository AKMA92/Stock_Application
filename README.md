## Stock Price Trend (AAPL)

This project fetches stock market data from an external API and processes it using Python.  
The data is then visualized with pandas and matplotlib to display stock price trends.  
To reduce unnecessary API calls, the data is only fetched via GET if no JSON cache file exists or if the existing cache is older than 10 minutes.

<img src="img.png" alt="Stock Chart" width="600"/>

## Downloader

The Downloader class fetches stock market data from the Alpha Vantage API and caches it locally in a JSON file.  
It avoids unnecessary API calls by reusing cached data if it is less than 10 minutes old.

## Plotter

The Plotter class processes the fetched data, calculates key statistics (mean, min, max, standard deviation), and visualizes the last 10 days of closing prices using matplotlib.