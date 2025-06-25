import logging
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Abstract base class for feature engineering strategies
class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Defines the interface for feature transformation.

        Parameters:
        df (pd.DataFrame): Input dataframe.

        Returns:
        pd.DataFrame: Transformed dataframe.
        """
        pass


# Strategy for log transformation of skewed features
class LogTransformation(FeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initialize with features to apply log transformation.

        Parameters:
        features (list): List of target features.
        """
        self.features = features

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply log1p transformation to specified features.

        Parameters:
        df (pd.DataFrame): Input dataframe.

        Returns:
        pd.DataFrame: Dataframe with log-transformed features.
        """
        logging.info(f"Applying log transformation to features: {self.features}")
        df_transformed = df.copy()
        for feature in self.features:
            df_transformed[feature] = np.log1p(df[feature])  # log1p safely handles log(0)
        logging.info("Log transformation completed.")
        return df_transformed


# Strategy for standard scaling (mean=0, std=1)
class StandardScaling(FeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initialize with features to standardize.

        Parameters:
        features (list): List of target features.
        """
        self.features = features
        self.scaler = StandardScaler()

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply standard scaling to specified features.

        Parameters:
        df (pd.DataFrame): Input dataframe.

        Returns:
        pd.DataFrame: Dataframe with standardized features.
        """
        logging.info(f"Applying standard scaling to features: {self.features}")
        df_transformed = df.copy()
        df_transformed[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Standard scaling completed.")
        return df_transformed


# Strategy for Min-Max scaling to a specified range
class MinMaxScaling(FeatureEngineeringStrategy):
    def __init__(self, features, feature_range=(0, 1)):
        """
        Initialize with features and target scaling range.

        Parameters:
        features (list): List of target features.
        feature_range (tuple): Target scaling range.
        """
        self.features = features
        self.scaler = MinMaxScaler(feature_range=feature_range)

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply Min-Max scaling to specified features.

        Parameters:
        df (pd.DataFrame): Input dataframe.

        Returns:
        pd.DataFrame: Dataframe with scaled features.
        """
        logging.info(
            f"Applying Min-Max scaling to features: {self.features} with range {self.scaler.feature_range}"
        )
        df_transformed = df.copy()
        df_transformed[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Min-Max scaling completed.")
        return df_transformed


# Strategy for one-hot encoding categorical features
class OneHotEncoding(FeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initialize with categorical features to encode.

        Parameters:
        features (list): List of target categorical features.
        """
        self.features = features
        self.encoder = OneHotEncoder(sparse=False, drop="first")

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply one-hot encoding to specified categorical features.

        Parameters:
        df (pd.DataFrame): Input dataframe.

        Returns:
        pd.DataFrame: Dataframe with one-hot encoded features.
        """
        logging.info(f"Applying one-hot encoding to features: {self.features}")
        df_transformed = df.copy()
        encoded_df = pd.DataFrame(
            self.encoder.fit_transform(df[self.features]),
            columns=self.encoder.get_feature_names_out(self.features),
        )
        df_transformed = df_transformed.drop(columns=self.features).reset_index(drop=True)
        df_transformed = pd.concat([df_transformed, encoded_df], axis=1)
        logging.info("One-hot encoding completed.")
        return df_transformed


# Context class for applying feature engineering strategies
class FeatureEngineer:
    def __init__(self, strategy: FeatureEngineeringStrategy):
        """
        Initialize with a feature engineering strategy.

        Parameters:
        strategy (FeatureEngineeringStrategy): Feature transformation strategy.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: FeatureEngineeringStrategy):
        """
        Update the current feature engineering strategy.

        Parameters:
        strategy (FeatureEngineeringStrategy): New strategy to apply.
        """
        logging.info("Switching feature engineering strategy.")
        self._strategy = strategy

    def apply_feature_engineering(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply the current strategy to the dataframe.

        Parameters:
        df (pd.DataFrame): Input dataframe.

        Returns:
        pd.DataFrame: Transformed dataframe.
        """
        logging.info("Applying feature engineering strategy.")
        return self._strategy.apply_transformation(df)


# Example usage
if __name__ == "__main__":
    # Example dataframe
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Log Transformation Example
    # log_transformer = FeatureEngineer(LogTransformation(features=['SalePrice', 'Gr Liv Area']))
    # df_log_transformed = log_transformer.apply_feature_engineering(df)

    # Standard Scaling Example
    # standard_scaler = FeatureEngineer(StandardScaling(features=['SalePrice', 'Gr Liv Area']))
    # df_standard_scaled = standard_scaler.apply_feature_engineering(df)

    # Min-Max Scaling Example
    # minmax_scaler = FeatureEngineer(MinMaxScaling(features=['SalePrice', 'Gr Liv Area'], feature_range=(0, 1)))
    # df_minmax_scaled = minmax_scaler.apply_feature_engineering(df)

    # One-Hot Encoding Example
    # onehot_encoder = FeatureEngineer(OneHotEncoding(features=['Neighborhood']))
    # df_onehot_encoded = onehot_encoder.apply_feature_engineering(df)

    pass
