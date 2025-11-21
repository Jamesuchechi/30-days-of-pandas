import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients['conditions'].str.contains(r'\bDIAB1', regex=True, na=False)
    return patients[mask][['patient_id', 'patient_name', 'conditions']]
