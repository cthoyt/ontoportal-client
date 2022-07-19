# -*- coding: utf-8 -*-

"""Download the NCBO BioPortal registry.

Get an API key by logging up, signing in, and navigating to .
"""

from typing import Any, Dict, Optional

import pystow
import requests

from .constants import NAMES, URLS

__all__ = [
    # Base clients
    "OntoPortalClient",
    "PreconfiguredOntoPortalClient",
    # Concrete clients
    "AgroPortalClient",
    "EcoPortalClient",
    "BioPortalClient",
    "MatPortalClient",
    "SIFRBioPortalClient",
    "MedPortalClient",
]


class OntoPortalClient:
    """A client for an OntoPortal site, like BioPortal."""

    def __init__(self, api_key: str, base_url: str):
        """Instantiate the OntoPortal client.

        :param api_key: The API key for the OntoPortal instance
        :param base_url: The base URL for the OntoPortal instance, e.g.,
            ``https://data.bioontology.org`` for BioPortal.
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_json(self, path: str, params: Optional[Dict[str, Any]] = None, **kwargs):
        """Get the response JSON."""
        return self.get_response(path=path, params=params, **kwargs).json()

    def get_response(
        self, path: str, params: Optional[Dict[str, Any]] = None, **kwargs
    ) -> requests.Response:
        """Send a GET request the given endpoint on the OntoPortal site.

        :param path: The path to query following the base URL, e.g., ``/ontologies``
        :param params: Parameters to pass through to :func:`requests.get`
        :param kwargs: Keyword arguments to pass through to :func:`requests.get`
        :returns: The response from :func:`requests.get`

        The rate limit is 15 queries per second. See:
        https://www.bioontology.org/wiki/Annotator_Optimizing_and_Troublehooting
        """
        if not params:
            params = {}
        params.setdefault("apikey", self.api_key)
        return requests.get(self.base_url + "/" + path.lstrip("/"), params=params, **kwargs)

    def get_ontologies(self):
        """Get ontologies."""
        return self.get_json("ontologies")


class PreconfiguredOntoPortalClient(OntoPortalClient):
    """A client for an OntoPortal site, like BioPortal."""

    def __init__(self, name: NAMES, api_key: Optional[str] = None, value_key: str = "api_key"):
        """Instantiate the OntoPortal Client.

        :param name: The name of the instance. One of:
            1. ``bioportal``
            2. ``agroportal``
            3. ``ecoportal``
        :param api_key: The API key for the instance. If not given, use :mod:`pystow` to read
            the configuration in one of the following ways (assuming BioPortal)

            1. From `BIOPORTAL_API_KEY` in the environment
            2. From a configuration file at `~/.config/bioportal.ini`
               and set the `[bioportal]` section in it with the given key
        :param value_key: The name of the key to use. By default, uses ``api_key``
        """
        self.name = name
        base_url = URLS[name]
        if api_key is None:
            api_key = pystow.get_config(self.name, value_key, raise_on_missing=True)
        super().__init__(api_key=api_key, base_url=base_url)


class BioPortalClient(PreconfiguredOntoPortalClient):
    """A client for BioPortal.

    To get an API key, follow the sign-up process at https://bioportal.bioontology.org/account.
    """

    # docstr-coverage: inherited
    def __init__(self, **kwargs):  # noqa:D107
        super().__init__(name="bioportal", **kwargs)


class AgroPortalClient(PreconfiguredOntoPortalClient):
    """A client for AgroPortal."""

    # docstr-coverage: inherited
    def __init__(self, **kwargs):  # noqa:D107
        super().__init__(name="agroportal", **kwargs)


class EcoPortalClient(PreconfiguredOntoPortalClient):
    """A client for EcoPortal."""

    # docstr-coverage: inherited
    def __init__(self, **kwargs):  # noqa:D107
        super().__init__(name="ecoportal", **kwargs)


class MatPortalClient(PreconfiguredOntoPortalClient):
    """A client for materials science ontologies in `MatPortal <https://matportal.org>`_.

    Create an account and get an API key by starting at https://matportal.org/accounts/new.
    """

    # docstr-coverage: inherited
    def __init__(self, **kwargs):  # noqa:D107
        super().__init__(name="matportal", **kwargs)


class SIFRBioPortalClient(PreconfiguredOntoPortalClient):
    """A client for French biomedical ontologies in `SIFR BioPortal <http://bioportal.lirmm.fr>`_.

    Create an account and get an API key by starting at http://bioportal.lirmm.fr/accounts/new.
    """

    # docstr-coverage: inherited
    def __init__(self, **kwargs):  # noqa:D107
        super().__init__(name="sifr_bioportal", **kwargs)


class MedPortalClient(PreconfiguredOntoPortalClient):
    """A client for medical ontologies in `MedPortal <https://medportal.bmicc.cn>`_.

    Create an account and get an API key by starting at https://medportal.bmicc.cn/accounts/new.
    """

    # docstr-coverage: inherited
    def __init__(self, **kwargs):  # noqa:D107
        super().__init__(name="medportal", **kwargs)
