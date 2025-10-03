from fastapi import FastAPI, UploadFile
from portfolio import optimize_portfolio
import pandas as pd

app = FastAPI(title="Portfolio Manager MVP")

@app.post("/portfolio/optimize")
async def optimize(file: UploadFile):
    """
    Input: CSV file with historical prices
    Output: Optimized portfolio weights as JSON
    """
    # Read CSV into pandas DataFrame
    df = pd.read_csv(file.file)
    
    # Process data and calculate optimized weights
    optimized_weights = optimize_portfolio(df)
    
    # Return JSON
    return {"optimized_portfolio": optimized_weights}
