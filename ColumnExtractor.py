class ColumnExtractor(BaseEstimator, TransformerMixin):
    """Extracts a single column from DataFrame as a Series
    to preserve the methods.
    """
    def __init__(self, col):
        self.col = col
    
    def fit(self, X, y=None):
        """interface conforming for fit_transform"""
        return self
    
    def transform(self, X):
        """Expects a pd.DataFrame data type"""
        print('EXTRACTING SINGLE COLUMN ...')
        X_new = X[self.col]#.astype(str)
        return X_new
