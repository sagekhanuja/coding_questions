import numpy as np
def get_top_stocks(daily_stocks):
    stocks = list(daily_stocks[0].keys())
    stock_values = [0 for i in stocks]
    for day in daily_stocks:
        for i in range(len(stocks)):
            stock_values[i] += day[stocks[i]]
    print(stocks)
    print(stock_values)
    x = sorted([stocks[i] for i in np.argsort(stock_values)[-3:]])
    print(x)

get_top_stocks([
    {
        'ACT': 171.7,
        'BNDW': 180.45,
        'DEST': 149.32,
        'FTA': 131.81,
        'PYPL': 128.67
    },
    {
        'ACT': 187.79,
        'BNDW': 183.13,
        'DEST': 162.88,
        'FTA': 138.63,
        'PYPL': 181.72
    },
    {
        'ACT': 189.83,
        'BNDW': 191.21,
        'DEST': 168.39,
        'FTA': 113.35,
        'PYPL': 136.57
    },
    {
        'ACT': 198.84,
        'BNDW': 171.2,
        'DEST': 142.62,
        'FTA': 137.06,
        'PYPL': 184.32
    }
])