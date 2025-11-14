import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filter products that are both low fat and recyclable
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    
    # Return only the product_id column
    return result[['product_id']]

# Test the function locally
def test_find_products():
    # Create test data matching the example
    data = {
        'product_id': [0, 1, 2, 3, 4],
        'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
        'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
    }
    
    products_df = pd.DataFrame(data)
    print("Input Products table:")
    print(products_df)
    print("\n" + "="*50 + "\n")
    
    # Call the function
    result = find_products(products_df)
    
    print("Output (products that are both low fat and recyclable):")
    print(result)
    print("\nExpected: product_id 1 and 3")
    
    # Verify the result
    expected_ids = [1, 3]
    actual_ids = result['product_id'].tolist()
    
    print(f"\nTest Result: {'PASS' if actual_ids == expected_ids else 'FAIL'}")
    print(f"Expected: {expected_ids}")
    print(f"Actual: {actual_ids}")

# Additional test cases
def additional_tests():
    print("\n" + "="*60)
    print("ADDITIONAL TEST CASES")
    print("="*60)
    
    # Test case 1: All products meet criteria
    print("\nTest Case 1 - All products are low fat and recyclable:")
    data1 = {
        'product_id': [10, 11, 12],
        'low_fats': ['Y', 'Y', 'Y'],
        'recyclable': ['Y', 'Y', 'Y']
    }
    df1 = pd.DataFrame(data1)
    result1 = find_products(df1)
    print(f"Input: {data1}")
    print(f"Output: {result1['product_id'].tolist()}")
    
    # Test case 2: No products meet criteria
    print("\nTest Case 2 - No products are both low fat and recyclable:")
    data2 = {
        'product_id': [20, 21, 22],
        'low_fats': ['Y', 'N', 'Y'],
        'recyclable': ['N', 'Y', 'N']
    }
    df2 = pd.DataFrame(data2)
    result2 = find_products(df2)
    print(f"Input: {data2}")
    print(f"Output: {result2['product_id'].tolist()}")
    
    # Test case 3: Empty dataframe
    print("\nTest Case 3 - Empty dataframe:")
    data3 = {
        'product_id': [],
        'low_fats': [],
        'recyclable': []
    }
    df3 = pd.DataFrame(data3)
    result3 = find_products(df3)
    print(f"Input: Empty dataframe")
    print(f"Output: {result3['product_id'].tolist()}")
"""
# Alternative implementations for comparison
def find_products_alternative1(products: pd.DataFrame) -> pd.DataFrame:
    
    return products.query("low_fats == 'Y' and recyclable == 'Y'")[['product_id']]

def find_products_alternative2(products: pd.DataFrame) -> pd.DataFrame:
    #Alternative using loc with multiple conditions
    return products.loc[products['low_fats'].eq('Y') & products['recyclable'].eq('Y'), ['product_id']]

# Compare different methods
def compare_methods():
    print("\n" + "="*60)
    print("COMPARING DIFFERENT METHODS")
    print("="*60)
    
    # Test data
    data = {
        'product_id': [0, 1, 2, 3, 4],
        'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
        'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
    }
    df = pd.DataFrame(data)
    
    print("Input data:")
    print(df)
    print("\nResults from different methods:")
    
    # Method 1 - Original
    result1 = find_products(df.copy())
    print(f"Method 1 (boolean indexing): {result1['product_id'].tolist()}")
    
    # Method 2 - Query
    result2 = find_products_alternative1(df.copy())
    print(f"Method 2 (query): {result2['product_id'].tolist()}")
    
    # Method 3 - Loc with conditions
    result3 = find_products_alternative2(df.copy())
    print(f"Method 3 (loc with conditions): {result3['product_id'].tolist()}")

if __name__ == "__main__":
    # Run main test
    test_find_products()
    
    # Run additional tests
    additional_tests()
    
    # Compare methods
    compare_methods()"""