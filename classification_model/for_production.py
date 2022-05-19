import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from processing.data_manager import data_inputting, DATA_STORE
from processing.validation import validate_inputs, drop_na_input
from config.core import config

# Inputing / Requestin Data
data_ = data_inputting(filename=config.app_config.test_data_file)

# Validating data
validated_data, errors = validate_inputs(input_data=data_, features_= config.model_config.features)
print(validated_data)
