"""A client to BioPortal and other OntoPortal instances."""

from class_resolver import ClassResolver

from .api import (
    AgroPortalClient,
    BioPortalClient,
    EcoPortalClient,
    MatPortalClient,
    MedPortalClient,
    OntoPortalClient,
    PreconfiguredOntoPortalClient,
    SIFRBioPortalClient,
)

__all__ = [
    "AgroPortalClient",
    "BioPortalClient",
    "EcoPortalClient",
    "MatPortalClient",
    "MedPortalClient",
    "OntoPortalClient",
    "PreconfiguredOntoPortalClient",
    "SIFRBioPortalClient",
    "ontoportal_resolver",
]

ontoportal_resolver = ClassResolver.from_subclasses(
    OntoPortalClient,
    suffix="Client",
    skip={PreconfiguredOntoPortalClient},
)
