import typing as ty
import sys
sys.path.append(".")
import numpy as np
import pandas as pd
from config.core import config, TRAINED_MODEL_DIR
from classification_model import __version__ as _version
from processing.data_manager import load_pipeline, TRAINED_MODEL_DIR
from processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_titanic_pipeline = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: ty.Union[pd.DataFrame, dict]) -> dict:
    """Make prediction using trained model"""

    # check inputs columns type
    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(data,
                                             config.model_config.features)
    results = {"predictions": None, "Version": _version, "errors": errors}

    if not errors:
        predictions_ = _titanic_pipeline.predict_proba(
            X=validated_data[config.model_config.features])
        results = {
            "predictions": [pred for pred in predictions_],
            "Version": _version,
            "errors": errors
        }
    return results
