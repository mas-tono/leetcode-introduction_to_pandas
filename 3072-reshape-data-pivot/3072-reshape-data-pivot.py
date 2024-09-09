import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # return pd.pivot_table(data=weather, 
    #                 index='month', 
    #                 columns='city', 
    #                 values='temperature',
    #                 aggfunc='max')
    
    return pd.pivot(weather, index='month', columns='city', values='temperature')