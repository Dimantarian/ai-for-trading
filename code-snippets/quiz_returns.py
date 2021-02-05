import quiz_tests


def calculate_returns(close):
    """
    Compute returns for each ticker and date in close.
    
    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date
    
    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """
    # TODO: Implement Function
    close_shifted = close.shift(1)
    
    close_returns = (close - close_shifted) / close_shifted
    return None


quiz_tests.test_calculate_returns(calculate_returns)