from typing import Union
from enum import Enum, auto
from pathlib import Path
from dataclasses import dataclass
from namedivider.util import \
    get_kanji_csv_default_path, \
    get_family_name_txt_default_path, \
    get_gbdt_model_v1_default_path

KANJI_CSV_DEFAULT_PATH = get_kanji_csv_default_path()
FAMILY_NAME_TXT_DEFAULT_PATH = get_family_name_txt_default_path()
GBDT_MODEL_V1_DEFAULT_PATH = get_gbdt_model_v1_default_path()


class NameDividerVersions(Enum):
    BASIC_NAME_DIVIDER_V1 = auto()
    BASIC_NAME_DIVIDER_V2 = auto()
    BASIC_NAME_DIVIDER_LATEST = auto()
    GBDT_NAME_DIVIDER_V1 = auto()
    GBDT_NAME_DIVIDER_LATEST = auto()


@dataclass(frozen=True)
class NameDividerConfigBase:
    separator: str = " "
    normalize_name: bool = True
    algorithm_name: str = "unknown_algorithm"


@dataclass(frozen=True)
class BasicNameDividerConfig(NameDividerConfigBase):
    path_csv: Union[str, Path] = KANJI_CSV_DEFAULT_PATH
    only_order_score_when_4: bool = False
    algorithm_name: str = "kanji_feature"


@dataclass(frozen=True)
class GBDTNameDividerConfig(NameDividerConfigBase):
    path_csv: Union[str, Path] = KANJI_CSV_DEFAULT_PATH
    path_family_names: Union[str, Path] = FAMILY_NAME_TXT_DEFAULT_PATH
    path_model: Union[str, Path] = GBDT_MODEL_V1_DEFAULT_PATH
    algorithm_name: str = "gbdt"


def get_config_from_version(version: NameDividerVersions) -> NameDividerConfigBase:
    if version == NameDividerVersions.BASIC_NAME_DIVIDER_V1:
        return BasicNameDividerConfig(
            separator=" ",
            normalize_name=False,
            path_csv=KANJI_CSV_DEFAULT_PATH,
            only_order_score_when_4=True
        )
    elif version == NameDividerVersions.BASIC_NAME_DIVIDER_V2:
        return BasicNameDividerConfig(
            separator=" ",
            normalize_name=True,
            path_csv=KANJI_CSV_DEFAULT_PATH,
            only_order_score_when_4=False
        )
    elif version == NameDividerVersions.BASIC_NAME_DIVIDER_LATEST:
        return BasicNameDividerConfig()
    elif version == NameDividerVersions.GBDT_NAME_DIVIDER_V1:
        return GBDTNameDividerConfig(
            separator=" ",
            normalize_name=True,
            path_csv=KANJI_CSV_DEFAULT_PATH,
            path_family_names=FAMILY_NAME_TXT_DEFAULT_PATH,
            path_model=GBDT_MODEL_V1_DEFAULT_PATH
        )
    elif version == NameDividerVersions.GBDT_NAME_DIVIDER_LATEST:
        return GBDTNameDividerConfig()
    else:
        raise ValueError(f"Version {version} is not in NameDividerVersions.")
