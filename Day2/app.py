import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Returns product_id of products that are both low fat and recyclable.
    
    Args:
        products: DataFrame with columns ['product_id', 'low_fats', 'recyclable']
    
    Returns:
        DataFrame with single column ['product_id']
    """
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products.loc[mask, ['product_id']]



def test():
    data = {
        'product_id': [0, 1, 2, 3, 4],
        'low_fats':   ['Y', 'Y', 'N', 'Y', 'N'],
        'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
    }
    df = pd.DataFrame(data)
    result = find_products(df)
    expected = pd.DataFrame({'product_id': [1, 3]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
    print(df.to_markdown())

if __name__ == "__main__":
    test()