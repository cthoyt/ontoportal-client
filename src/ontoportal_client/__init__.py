# -*- coding: utf-8 -*-

"""A client to BioPortal and other OntoPortal instances."""

from .api import (
    AgroPortalClient,
    BioPortalClient,
    EcoPortalClient,
    MatPortalClient,
    MedPortalClient,
    OntoPortalClient,
    SIFRBioPortalClient,
)

__all__ = [
    "OntoPortalClient",
    "AgroPortalClient",
    "EcoPortalClient",
    "BioPortalClient",
    "MatPortalClient",
    "SIFRBioPortalClient",
    "MedPortalClient",
]
