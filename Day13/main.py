import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Create rank using dense ranking (no gaps after ties)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)

    # Select required columns and sort by score desc
    return scores[['score', 'rank']].sort_values(by='score', ascending=False)
