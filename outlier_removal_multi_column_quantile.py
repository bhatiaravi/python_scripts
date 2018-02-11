import pandas as pd

def remove_two_tail_outliers(df, col, two_tail_remove_fraction=0.05):
    """
    Useful to remove two tail quantile based outlier removal on multiple columns.
    Important Catch: Applying quantiles for multi column outlier removal one-by-one could 
    lead to a significant loss of data points which might not really be outliers. In a lot of 
    scenarios outlier in one column is also an outlier in another column. This method does not 
    blindly remove outliers on each column, but calculates each variable range beforehand and 
    does the filtering post the range calculation, effectively reducing the number of outliers
    and conserving useful data points.
    
    Inputs
    df: a pandas DataFrame
    col: a string if single column or an array of columns in DataFrame eg: ['A','B','C']
    two_tail_remove_fraction: two tail removal fraction eg: for 5% two tail, provide 0.05
    """
    if isinstance(col, str):
        lower_val, upper_val = df[col].quantile(two_tail_remove_fraction), df[col].quantile(1.0 - two_tail_remove_fraction)
        df = df[(df[col] >= lower_val) & (df[col] <= upper_val)]
    else:   # Multiple col filter case, col is an array
        filters = {}
        for c in col:
            # Calculate quantile ranges of all variables first
            filters[c] = df[c].quantile(two_tail_remove_fraction), df[c].quantile(1.0 - two_tail_remove_fraction)
        for filt in filters.keys():
            col = filt
            lower_val = filters[filt][0]
            upper_val = filters[filt][1]
            # Apply filter on previously calculated variable quantiles
            df = df[(df[col] >= lower_val) & (df[col] <= upper_val)]
    return df
