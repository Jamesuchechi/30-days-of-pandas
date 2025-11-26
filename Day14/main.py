import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Keep only rows where id is the smallest for each email
    person.drop_duplicates(subset=["email"], keep="first", inplace=True)
