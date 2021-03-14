import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    ## Pivot the table
    prices_p = prices.pivot(index='date', columns='ticker', values='price')
    ## Calculate log returns
    prices_p["log_a"] = np.log(prices_p["A"])
    prices_p["log_b"] = np.log(prices_p["B"])
    
    prices_p["log_a_shift"] = prices_p["log_a"].shift(1)
    prices_p["log_b_shift"] = prices_p["log_b"].shift(1)
    
    prices_p['log_ret_a'] = prices_p["log_a"] - prices_p["log_a_shift"]
    prices_p['log_ret_b'] = prices_p["log_b"] - prices_p["log_b_shift"]
    
    if prices_p['log_ret_a'].std() > prices_p['log_ret_b'].std():
       return "A"
    else:
        return "B"
    pass


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
