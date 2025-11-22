import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f'getNthHighestSalary({N})'
    
    if N <= 0:
        return pd.DataFrame({col: [None]})
    
    distinct = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    if N > len(distinct):
        return pd.DataFrame({col: [None]})
    
    return pd.DataFrame({col: [int(distinct.iloc[N-1])]})
