import typing
import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline
import joblib
from yaml import dump

File_ = Path(__file__).resolve().parent.parent
DATA_STORE = File_ / "datasets"
TRAINED_MODEL_DIR = File_ / "trained"


def data_inputting(*, filename: str) -> pd.DataFrame:  #ignore
    """ Load and check dataframe"""
    dataframe = pd.read_csv(Path(f"{DATA_STORE}/{filename}"))
    dataframe['Pclass'] = dataframe['Pclass'].astype('O')
    return dataframe


def save_pipelines(*, pipeline_to_save: Pipeline, pipeline_name: str,
                   version: str, remove_previous_version: bool) -> None:
    """ Save the current pipelines
    Save the version model"""

    # Set pipeline save file name
    save_file_name = f"{pipeline_name}{version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    if remove_previous_version:
        remove_old_pipelines(file_to_keep=[save_file_name])
        joblib.dump(pipeline_to_save, save_path)
    else:
        joblib.dump(pipeline_to_save, save_path)


def remove_old_pipelines(*, file_to_keep: typing.List[str]) -> None:
    """remove ol pipelines"""
    do_not_delete = file_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():  #Iterate through files
        if model_file not in do_not_delete:
            model_file.unlink()  #Delete or remove file


def load_pipeline(*, file_name: str) -> Pipeline:
    """ Load Pipelines"""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(file_path)
    return trained_model