import pandas as pd
import numpy as np

def time_series_anomaly_remover(df, cols, window_size=20, std_factor=2.0):
    """ 
    Pass the dataframe and an array of column names in the DF on which anomaly removal should be applied

    Parameters:
    df: a pandas dataframe
    cols: type array, column names of dataframe eg: ['A','B','C']
    window_size: sliding window size
    std_factor: Determines acceptable value of variation to consider a point valid. Eg: 2.0 considers 2*sigma as acceptable
    
    NaN values treatment:

    """
    df['accept'] = np.nan
    """ 
    Compute rolling Std deviation (Sigma) of all columns.
    For each column of Std deviations, take a quantile value to determine allowable sigma for the column
    """
    STD_QUANTILE = 0.90 # 90% quantile of STD values
    std_cols = df[cols].rolling(window=window_size).std().quantile([STD_QUANTILE])
    for col in cols:
        sigma = std_cols[col].values[0]
        mov_avg = df[col].rolling(window=window_size).mean()
        # Left window moving average (Mov Avg of points to the left)
        left_mov_avg = mov_avg.shift(1)
        # Right window moving average (Mov Avg of points to the right)
        right_mov_avg = mov_avg.shift(-1*window_size)
        # Set True if its in reasonable proximity of either left or right window moving average
        df['accept'] = (abs(left_mov_avg - df[col]) <= std_factor * sigma) \
                                     | (abs(right_mov_avg - df[col]) <= std_factor * sigma)
        print "Points removed with column", col, df[~df['accept']][col].shape[0]
        # Filter the points not satisfying acceptable criteria
        df = df.drop(df[~df['accept']].index)
    del df['accept']
    return df
