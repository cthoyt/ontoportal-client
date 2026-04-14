"""Constants for the OntoPortal Client."""

from typing import Literal

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
INDUSTRYPORTAL_BASE_URL = "https://data.industryportal.enit.fr"
ONTOPORTAL_ASTRO_BASE_URL = ""
BIODIVPORTAL_BASE_URL = "https://data.biodivportal.gfbio.org"
EARTHPORTAL_BASE_URL = ""
SOCIOPORTAL_BASE_URL = ""
TECHNOPORTAL_BASE_URL = ""
LOVPORTAL_BASE_URL = ""

NAMES = Literal[
    "bioportal",
    "ecoportal",
    "agroportal",
    "matportal",
    "sifr_bioportal",
    "medportal",
    "industryportal",
    "ontoportal-astro",
    "biodivportal",
    "earthportal",
    "socioportal",
    "technoportal",
    "lovportal",
]

URLS: dict[NAMES, str] = {
    "bioportal": BIOPORTAL_BASE_URL,
    "ecoportal": ECOPORTAL_BASE_URL,
    "agroportal": AGROPORTAL_BASE_URL,
    "matportal": MATPORTAL_BASE_URL,
    "sifr_bioportal": SIFR_BIOPORTAL_BASE_URL,
    "medportal": MEDPORTAL_BASE_URL,
    "industryportal": INDUSTRYPORTAL_BASE_URL,
    "ontoportal-astro": ONTOPORTAL_ASTRO_BASE_URL,
    "biodivportal": BIODIVPORTAL_BASE_URL,
    "earthportal": EARTHPORTAL_BASE_URL,
    "socioportal": SOCIOPORTAL_BASE_URL,
    "technoportal": TECHNOPORTAL_BASE_URL,
    "lovportal": LOVPORTAL_BASE_URL,
}
