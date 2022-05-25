from typing import List
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline


class selected_featured(BaseEstimator, TransformerMixin):
    """ Feature Selected by the Developer after OSEM """
    def __init__(self, variables: List[str]):
        if not isinstance(variables, list):
            raise ValueError("feature must be a list")
        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> pd.DataFrame:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X = X.loc[:, self.variables]
        return X


class feature_mapper(BaseEstimator, TransformerMixin):
    """Categorical Features Mapper"""
    def __init__(self, variables: List[str], mappings: dict):
        if not isinstance(variables, list):
            raise ValueError("Variable must be a list")

        self.variables = variables
        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> pd.DataFrame:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        # Creating Copy
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)

        return X


class OnehotTransform(BaseEstimator, TransformerMixin):
    """ Transform into Onehot Encoding and Return dataframe"""
    def __init__(self, variables: List[str]):
        if not isinstance(variables, list):
            raise ValueError("variable must be a lsit")
        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> pd.DataFrame:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:

        X = X.copy()
        OHC = OneHotEncoder(sparse=False)  #return a matrix
        result = OHC.fit_transform(X[self.variables])
        frame_enc = pd.DataFrame(data=OHC.fit_transform(X[self.variables]),
                                 columns=OHC.get_feature_names_out())
        result = pd.concat([X, frame_enc], axis=1)
        result.drop(self.variables, axis=1, inplace=True)

        return result
