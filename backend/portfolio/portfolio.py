from pypfopt import EfficientFrontier, risk_models, expected_returns

def optimize_portfolio(df):
    """
    Input: df -> pandas DataFrame of historical prices (columns = tickers)
    Output: dictionary of optimized weights
    """
    # Calculate expected returns
    mu = expected_returns.mean_historical_return(df)

    # Calculate covariance matrix
    S = risk_models.sample_cov(df)

    # Efficient Frontier
    ef = EfficientFrontier(mu, S)

    # Maximize Sharpe ratio
    ef.max_sharpe()

    # Clean weights
    cleaned_weights = ef.clean_weights()

    return cleaned_weights
