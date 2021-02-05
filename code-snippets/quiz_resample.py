import quiz_tests


def days_to_weeks(open_prices, high_prices, low_prices, close_prices):
    """Converts daily OHLC prices to weekly OHLC prices.
    
    Parameters
    ----------
    open_prices : DataFrame
        Daily open prices for each ticker and date
    high_prices : DataFrame
        Daily high prices for each ticker and date
    low_prices : DataFrame
        Daily low prices for each ticker and date
    close_prices : DataFrame
        Daily close prices for each ticker and date

    Returns
    -------
    open_prices_weekly : DataFrame
        Weekly open prices for each ticker and date
    high_prices_weekly : DataFrame
        Weekly high prices for each ticker and date
    low_prices_weekly : DataFrame
        Weekly low prices for each ticker and date
    close_prices_weekly : DataFrame
        Weekly close prices for each ticker and date
    """
    open_prices_weekly = open_prices.resample('W').first()
    high_prices_weekly = high_prices.resample('W').max()
    low_prices_weekly = low_prices.resample('W').min()
    close_prices_weekly = close_prices.resample('W').last()
    # TODO: Implement Function
    
    return open_prices_weekly, high_prices_weekly, low_prices_weekly, close_prices_weekly


quiz_tests.test_days_to_weeks(days_to_weeks)