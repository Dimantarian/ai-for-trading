import project_tests

def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date
    
    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get
    
    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    top_performers = prices.loc[date].nlargest(top_n)
    
    # Here we are taking the top performers from the index of tha pandas series, and using that to subset 
    # on the index of the sectors series
    top_industries = set(sector.loc[top_performers.index])
    return top_industries


project_tests.test_date_top_industries(date_top_industries)