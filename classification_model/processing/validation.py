from ast import Expression
import sys
sys.path.append("../config/")
from typing import List, Optional, Tuple
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError


def drop_na_input(input_data: pd.DataFrame, features_: List) -> pd.DataFrame:
    """ Check model input and return only feature selected"""
    validate_data = input_data.copy()
    validate_data = validate_data[features_]
    return validate_data


def validate_inputs(input_data: pd.DataFrame,
                    features_: List) -> Tuple[pd.DataFrame, Optional[dict]]:
    """ check model inputs"""
    relevant_data = input_data.copy()
    validated_data = drop_na_input(input_data=relevant_data,
                                   features_=features_)
    errors = None
    try:
        # Replace Nan Values
        TitanicDataInputs(inputs=validated_data.replace({
            np.nan: None
        }).to_dict(orient='records'))  #ignored
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class TitanicDataInputSchema(BaseModel):
    """ This class validate the data input format"""
    PassengerId: Optional[int]
    Pclass: Optional[int]
    Name: Optional[str]
    Sex: Optional[str]
    Age: Optional[float]
    SibSp: Optional[int]
    Parch: Optional[int]
    Ticket: Optional[str]
    Fare: Optional[float]
    Cabin: Optional[str]
    Embarked: Optional[str]


class TitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]
