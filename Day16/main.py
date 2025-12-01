import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define conditions
    conditions = [
        accounts["income"] < 20000,
        accounts["income"].between(20000, 50000),
        accounts["income"] > 50000
    ]
    
    categories = ["Low Salary", "Average Salary", "High Salary"]
    
    # Assign category to each account
    accounts["category"] = pd.cut(
        accounts["income"],
        bins=[-1, 19999, 50000, float("inf")],
        labels=categories
    )
    
    # Count accounts per category
    counts = accounts["category"].value_counts().reindex(categories, fill_value=0)
    
    # Return as DataFrame
    return pd.DataFrame({
        "category": categories,
        "accounts_count": counts.values
    })
