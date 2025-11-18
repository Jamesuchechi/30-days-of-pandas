import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
 
    df = employees.copy()
    
    df["bonus"] = df.apply(
        lambda row: row["salary"] 
                    if row["employee_id"] % 2 == 1 and not row["name"].startswith("M")
                    else 0,
        axis=1
    )
    
    return df[["employee_id", "bonus"]].sort_values("employee_id")
