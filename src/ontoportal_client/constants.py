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
MATPORTAL_BASE_URL = "http://rest.matportal.org"
SIFR_BIOPORTAL_BASE_URL = "http://data.bioportal.lirmm.fr"
MEDPORTAL_BASE_URL = "http://data.medportal.bmicc.cn"

NAMES = Literal["bioportal", "ecoportal", "agroportal", "matportal", "sifr_bioportal", "medportal"]

URLS: Mapping[NAMES, str] = {
    "bioportal": BIOPORTAL_BASE_URL,
    "ecoportal": ECOPORTAL_BASE_URL,
    "agroportal": AGROPORTAL_BASE_URL,
    "matportal": MATPORTAL_BASE_URL,
    "sifr_bioportal": SIFR_BIOPORTAL_BASE_URL,
    "medportal": MEDPORTAL_BASE_URL,
}
