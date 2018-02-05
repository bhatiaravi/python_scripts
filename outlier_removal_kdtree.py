import pandas as pd
from scipy import spatial
from sklearn import preprocessing

"""
- To remove outliers where range of individual variables filtered on quantile 
basis is not enough, as some data points do not form part of the overall data cluster.
- The method variation to basic kdtree is its ability to remove a specified number of points (quantile parameter)
without any knowledge of distance metric apriori.
Usage - outlier_removal_kdtree(df, ['ColA','ColB'])
Limitation: Cannot remove outliers forming small cluster of points which is more than num num_neighbors
"""
def outlier_removal_kdtree(df, on_cols, quantile=0.99, num_neighbors=4):
    # Normalize variables first so that distance measurements are meaningful
    scaled_vars = pd.DataFrame(preprocessing.StandardScaler().fit_transform(df[on_cols]), columns=on_cols)
    # cKDTree significantly speeds up process compared to kdtree
    kd_tree = spatial.cKDTree(scaled_vars[on_cols], leafsize=df.shape[0]/100)
    # Compute distances with nearest neighbors (nearest points)
    dist, nearest_pt = kd_tree.query(scaled_vars[on_cols], k=num_neighbors)
    # Take all distances in a dist array, used further to determine outlier removal criteria
    dist_array = pd.Series(dist.ravel())
    # Take quantile of all distances to determine max distance criteria
    max_allowable_dist = dist_array.quantile(quantile)
    """
    Filter points not satisfying max distance criteria (Considering the farthest among nearest points.
    Eg: If num_neighbors=4, take the 4th nearest point for criteria check
    """
    indices = [1 if x[num_neighbors-1] < max_allowable_dist else 0 for x in dist]
    df['filter_criteria'] = indices
    df = df[df['filter_criteria'] == 1]
    del df['filter_criteria']
    return df
