import typing as ty 
import sys
sys.path.append(".")
import numpy as np 
import pandas as pd 
from config.core import config, TRAINED_MODEL_DIR
from classification_model import __version__ as _version

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
print(pipeline_file_name)
def make_prediction()


