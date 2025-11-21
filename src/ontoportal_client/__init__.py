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
    "AgroPortalClient",
    "BioPortalClient",
    "EcoPortalClient",
    "MatPortalClient",
    "MedPortalClient",
    "OntoPortalClient",
    "SIFRBioPortalClient",
]
