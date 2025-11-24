import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the tables on departmentId
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # For each department, find the maximum salary
    max_salary = merged.groupby('departmentId')['salary'].transform('max')
    
    # Filter rows where salary equals max salary for that department
    result = merged[merged['salary'] == max_salary]
    
    # Select and rename columns to match required output
    return result[['name_dept', 'name_emp', 'salary']].rename(
        columns={
            'name_dept': 'Department',
            'name_emp': 'Employee',
            'salary': 'Salary'
        }
    )
