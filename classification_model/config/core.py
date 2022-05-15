from pathlib import Path
from typing import List, Sequence, Dict
from pydantic import BaseModel
from strictyaml import load , YAML
# --> typing is the pytest version for text
# This file will run at calling

# == Project Directory =
PACKAGE_ROOT = Path(__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = ROOT / "config.yml"
DATASET_DIR = ROOT / "datasets"
TRAINED_MODEL_DIR = ROOT / "train_models"


class AppConfig(BaseModel):
    """
    Application to check each file extension
    """

    package_name:str
    training_data_file:str
    test_data_file:str
    pipeline_save_file:str
    


class ModelConfig(BaseModel):
    """
    All configuration relevant to model training
    including feature engieering columns
    """

    target:str 
    features:List[str] 
    test_size :float  
    learning_rate:float
    random_state:int
    one_vars_with_nan : List[str]  
    numerical_vars_with_na :List[str] 
    onehot_vars:List[str]
    categorical_with_nan: List[str]
    columns_to_drop:List[str] 
    map_sex: List[str]
    mapping_sex: Dict[str, int]  #*


class Config(BaseModel):
    """ Master config object """
    app_config : AppConfig
    model_config : ModelConfig

def find_config_file() -> Path:
    """ Locate the config.file """
    if CONFIG_FILE_PATH.is_file(): #check if it is file
        return CONFIG_FILE_PATH
        # the "!r" at the end add the windowsPath(directory) format
    raise Exception(f"config not found at {CONFIG_FILE_PATH!r}") 

def fetch_config_from_ymal (cfg_path: Path = None) -> YAML:  # type: ignore
    """Parse YAML containing the Package configuration"""

    if not cfg_path:  #If is not true
        cfg_path = find_config_file()
    
    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config =load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file path: {cfg_path}")

def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run Validation on config Values."""

    if parsed_config is None:
        parsed_config = fetch_config_from_ymal()

    # Specify the data attribute from the strictymal YAML type.
    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )

    return _config

config = create_and_validate_config()