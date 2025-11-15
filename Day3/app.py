import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Customers who never placed an order
    result = customers[~customers["id"].isin(orders["customerId"])]
    
    # Format result to match LeetCode output
    return result[["name"]].rename(columns={"name": "Customers"})


# --------------------------
# Local testing
# --------------------------
if __name__ == "__main__":
    # Example input
    customers = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "name": ["Joe", "Henry", "Sam", "Max"]
    })

    orders = pd.DataFrame({
        "id": [1, 2],
        "customerId": [3, 1]
    })

    # Run test
    output = find_customers(customers, orders)

    # Print result
    print(output)
