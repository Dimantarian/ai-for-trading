import project_tests
print(prices)

def generate_positions(prices):
    """
    Generate the following signals:
     - Long 30 share of stock when the price is above 50 dollars
     - Short 10 shares when it's below 20 dollars
    
    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    
    Returns
    -------
    final_positions : DataFrame
        Final positions for each ticker and date
    """
    # TODO: Implement Function
    signal_gt_50 = (prices > 50).astype(np.int)
    signal_lt_20 = (prices < 20).astype(np.int)
    pos_gt_50 = 30 * signal_gt_50
    pos_lt_20 = -10 * signal_lt_20
    final_positions = pos_gt_50 + pos_lt_20
    return final_positions


project_tests.test_generate_positions(generate_positions)