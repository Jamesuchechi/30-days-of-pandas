import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author viewed their own article
    self_views = views[views["author_id"] == views["viewer_id"]]
    
    # Extract unique author IDs and sort
    result = (self_views["author_id"]
              .drop_duplicates()
              .sort_values()
              .rename("id"))
    
    return result.to_frame()
