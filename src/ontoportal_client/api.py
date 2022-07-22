# -*- coding: utf-8 -*-

"""Download the NCBO BioPortal registry.

Get an API key by logging up, signing in, and navigating to .
"""

from typing import Any, ClassVar, Dict, Optional, Set, cast
from urllib.parse import quote

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

    def get_json(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        raise_for_status: bool = True,
        **kwargs,
    ):
        """Get the response JSON."""
        return self.get_response(
            path=path, params=params, raise_for_status=raise_for_status, **kwargs
        ).json()

    def get_response(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        raise_for_status: bool = True,
        **kwargs,
    ) -> requests.Response:
        """Send a GET request the given endpoint on the OntoPortal site.

        :param path: The path to query following the base URL, e.g., ``/ontologies``.
            If this starts with the base URL, it gets stripped.
        :param params: Parameters to pass through to :func:`requests.get`
        :param raise_for_status: If true and the status code isn't 200, raise an exception
        :param kwargs: Keyword arguments to pass through to :func:`requests.get`
        :returns: The response from :func:`requests.get`

        The rate limit is 15 queries per second. See:
        https://www.bioontology.org/wiki/Annotator_Optimizing_and_Troublehooting
        """
        if not params:
            params = {}
        params.setdefault("apikey", self.api_key)
        if path.startswith(self.base_url):
            path = path[len(self.base_url) :]
        res = requests.get(self.base_url + "/" + path.lstrip("/"), params=params, **kwargs)
        if raise_for_status:
            res.raise_for_status()
        return res

    def get_ontologies(self):
        """Get ontologies."""
        return self.get_json("ontologies")

    def get_ontology_versions(self, ontology: str) -> Set[str]:
        """Get all versions for the given ontology."""
        return {
            result["version"]
            for result in self.get_json(f"/ontologies/{ontology.upper()}/submissions")
        }

    def annotate(self, text: str, ontology: Optional[str] = None, require_exact_match: bool = True):
        """Annotate the given text."""
        # include =['prefLabel', 'synonym', 'definition', 'semanticType', 'cui']
        include = ["prefLabel", "semanticType", "cui"]
        params = {
            "include": ",".join(include),
            "require_exact_match": require_exact_match,
            "text": text,
        }
        if ontology:
            params["ontologies"] = ontology
        return self.get_json("/annotator", params=params)

    def search(self, text: str, ontology: Optional[str] = None):
        """Search the given text."""
        params = {"q": text, "include": ["prefLabel"]}
        if ontology:
            params["ontologies"] = ontology
        return self.get_json("/search", params)

    def get_ancestors(self, ontology: str, uri: str):
        """Get the ancestors of the given class."""
        quoted_uri = quote(uri, safe="")
        return self.get_json(
            f"/ontologies/{ontology}/classes/{quoted_uri}/ancestors",
            params={"display_context": "false"},
        )


class PreconfiguredOntoPortalClient(OntoPortalClient):
    """A client for an OntoPortal site, like BioPortal."""

    #: The name of the instance
    name: ClassVar[str]

    def __init__(self, api_key: Optional[str] = None, value_key: str = "api_key"):
        """Instantiate the OntoPortal Client.

        :param api_key:
            The API key for the instance. If not given, use :mod:`pystow` to read
            the configuration in one of the following ways. Using BioPortal as an example,
            where the subclass of :class:`PreconfiguredOntoPortalClient` sets the class
            variable ``name = "bioportal"``, the configuration can be set in the following
            ways:

            1. From `BIOPORTAL_API_KEY` in the environment, where the `name` is uppercased
               before `_API_KEY`
            2. From a configuration file at `~/.config/bioportal.ini`
               and set the `[bioportal]` section in it with the given key
        :param value_key:
            The name of the key to use. By default, uses ``api_key``
        """
        base_url = URLS[cast(NAMES, self.name)]
        if api_key is None:
            api_key = pystow.get_config(self.name, value_key, raise_on_missing=True)
        super().__init__(api_key=api_key, base_url=base_url)


class BioPortalClient(PreconfiguredOntoPortalClient):
    """A client for BioPortal.

    To get an API key, follow the sign-up process at https://bioportal.bioontology.org/account.
    """

    name = "bioportal"


class AgroPortalClient(PreconfiguredOntoPortalClient):
    """A client for AgroPortal."""

    name = "agroportal"


class EcoPortalClient(PreconfiguredOntoPortalClient):
    """A client for EcoPortal."""

    name = "ecoportal"


class MatPortalClient(PreconfiguredOntoPortalClient):
    """A client for materials science ontologies in `MatPortal <https://matportal.org>`_.

    Create an account and get an API key by starting at https://matportal.org/accounts/new.
    """

    name = "matportal"


class SIFRBioPortalClient(PreconfiguredOntoPortalClient):
    """A client for French biomedical ontologies in `SIFR BioPortal <http://bioportal.lirmm.fr>`_.

    Create an account and get an API key by starting at http://bioportal.lirmm.fr/accounts/new.
    """

    name = "sifr_bioportal"


class MedPortalClient(PreconfiguredOntoPortalClient):
    """A client for medical ontologies in `MedPortal <https://medportal.bmicc.cn>`_.

    Create an account and get an API key by starting at https://medportal.bmicc.cn/accounts/new.
    """

    name = "medportal"
