from sklearn.pipeline import Pipeline
import sys
sys.path.append("./classification_model")
import pandas as pd
from classification_model import __version__ as _version
from classification_model.config.core import config, DATASET_DIR, TRAINED_MODEL_DIR
from classification_model.processing.data_manager import data_inputting, save_pipelines, load_pipeline, remove_old_pipelines


class Testing_Data_Manager:

    "Testing for Data Manager"

    def test_data_inputting(self) -> pd.DataFrame:
        """Checking Data imputing outputs -> DataFrame"""

        DATA_STORE = DATASET_DIR
        result = data_inputting(filename=config.app_config.test_data_file)
        assert type(config.app_config.test_data_file) == str
        assert type(result) == type(pd.DataFrame())

    def test_load_pipelines(self, tmpdir) -> None:
        """ Checking Return :  Pipeline format"""
        pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
        result = load_pipeline(file_name=pipeline_file_name)
        assert type(result) == Pipeline
