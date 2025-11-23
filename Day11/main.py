import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get distinct salaries
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # If we have at least 2 distinct salaries
    if len(distinct_salaries) >= 2:
        sec_high = distinct_salaries.iloc[1]
    else:
        sec_high = None  
    
    return pd.DataFrame({'SecondHighestSalary': [sec_high]})
