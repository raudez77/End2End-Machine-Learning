import numpy as np
import sys
sys.path.append(".")
import pandas as pd
from sklearn.model_selection import train_test_split
from processing.data_manager import data_inputting, save_pipelines
from config.core import config
from pipeline import Titanic_pipe
from classification_model import __version__ as _ver

# Reading data file
data = data_inputting(filename=config.app_config.training_data_file)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data[config.model_config.features],
    data[config.model_config.target],
    test_size=config.model_config.test_size,
    random_state=config.model_config.random_state)

Titanic_pipe.fit(X_train, y_train)

# Saving
(save_pipelines(pipeline_to_save=Titanic_pipe,
                pipeline_name=config.app_config.pipeline_save_file,
                version=_ver,
                remove_previous_version=True))