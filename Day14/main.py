import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Compute the minimum id for each email
    min_ids = person.groupby("email")["id"].transform("min")
    # Drop rows whose id is not the minimum for that email (modify in-place)
    person.drop(index=person[person["id"] != min_ids].index, inplace=True)
