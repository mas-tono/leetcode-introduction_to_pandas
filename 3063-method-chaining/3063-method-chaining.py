import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    
    # result = animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]
    # return result

    # or
    
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]

    