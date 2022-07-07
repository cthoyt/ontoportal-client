"""Constants for the OntoPortal Client."""

from typing import Mapping

from typing_extensions import Literal

__all__ = [
    "NAMES",
    "URLS",
]

BIOPORTAL_BASE_URL = "https://data.bioontology.org"
ECOPORTAL_BASE_URL = "http://ecoportal.lifewatch.eu:8080"
AGROPORTAL_BASE_URL = "http://data.agroportal.lirmm.fr"

NAMES = Literal["bioportal", "ecoportal", "agroportal"]

URLS: Mapping[NAMES, str] = {
    "bioportal": BIOPORTAL_BASE_URL,
    "ecoportal": ECOPORTAL_BASE_URL,
    "agroportal": AGROPORTAL_BASE_URL,
}
