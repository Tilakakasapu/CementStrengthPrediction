from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    unzip_dir: Path
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    STATUS_FILE: str
    unzip_Data_dir: Path
    all_schema: dict
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path 
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    train_data_path: Path
    test_data_path : Path
    model_name: str
    learning_rate: float
    max_depth: int
    min_samples_leaf: int
    min_samples_split: int
    n_estimators: int
    target_column : str