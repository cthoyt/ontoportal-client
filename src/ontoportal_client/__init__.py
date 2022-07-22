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
    PreconfiguredOntoPortalClient,
)
from class_resolver import ClassResolver

__all__ = [
    # Resolver
    "ontoportal_resolver",
    # Base Classes
    "OntoPortalClient",
    "PreconfiguredOntoPortalClient",
    # Concrete Classes
    "AgroPortalClient",
    "EcoPortalClient",
    "BioPortalClient",
    "MatPortalClient",
    "SIFRBioPortalClient",
    "MedPortalClient",
]

ontoportal_resolver = ClassResolver.from_subclasses(
    OntoPortalClient,
    suffix="Client",
    skip={PreconfiguredOntoPortalClient},
)
