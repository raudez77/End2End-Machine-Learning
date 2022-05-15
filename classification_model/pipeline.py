from feature_engine.encoding import OrdinalEncoder, OneHotEncoder
from feature_engine.imputation import MeanMedianImputer, CategoricalImputer
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from config.core import config
from processing import features as pp
from sklearn.ensemble import GradientBoostingClassifier

Titanic_pipe = Pipeline([
    # === Selecting Features ===
    ("selecting_features",
     pp.selected_featured(variables=config.model_config.features)),

    # === IMPUTATION ==
    # Imputing Categorical with string *Pclass *Sex *Embarked
    ("missing_values_categorical",
     CategoricalImputer(imputation_method='frequent',
                        variables=config.model_config.categorical_with_nan)),

    # == Imputing Numerical data * Age * Fare
    ("missing_numerical_values",
     MeanMedianImputer(imputation_method='mean',
                       variables=config.model_config.numerical_vars_with_na)),

    # === Transforming Onehot and dummy ===
    ("mapping_sex",
     pp.feature_mapper(variables=config.model_config.map_sex,
                       mappings=config.model_config.mapping_sex)),

    # === OnehotEncoding ===
    ("onehotEncoding",
     OneHotEncoder(variables=config.model_config.one_vars_with_nan,
                   ignore_format=True)),

    # == StandarScaler
    ("scaler", MinMaxScaler()),

    # == GradientBoost
    ("GradientBoosting",
     GradientBoostingClassifier(
         learning_rate=config.model_config.learning_rate,
         random_state=config.model_config.random_state))
])
