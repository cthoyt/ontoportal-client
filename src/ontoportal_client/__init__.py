"""A client to BioPortal and other OntoPortal instances."""

from class_resolver import ClassResolver

from .api import (
    AgroPortalClient,
    AstroPortalClient,
    BioDivPortal,
    BioPortalClient,
    EarthPortal,
    EcoPortalClient,
    LovPortal,
    MatPortalClient,
    MedPortalClient,
    OntoPortalClient,
    PreconfiguredOntoPortalClient,
    SIFRBioPortalClient,
    SocioPortal,
    TechnoPortal,
)

__all__ = [
    "AgroPortalClient",
    "AstroPortalClient",
    "BioDivPortal",
    "BioPortalClient",
    "EarthPortal",
    "EcoPortalClient",
    "LovPortal",
    "MatPortalClient",
    "MedPortalClient",
    "OntoPortalClient",
    "PreconfiguredOntoPortalClient",
    "SIFRBioPortalClient",
    "SocioPortal",
    "TechnoPortal",
    "ontoportal_resolver",
]

ontoportal_resolver = ClassResolver.from_subclasses(
    OntoPortalClient,
    suffix="Client",
    skip={PreconfiguredOntoPortalClient},
)
