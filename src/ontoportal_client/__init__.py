"""A client to BioPortal and other OntoPortal instances."""

from class_resolver import ClassResolver

from .api import (
    AgroPortalClient,
    BioDivPortal,
    BioPortalClient,
    EarthPortal,
    EcoPortalClient,
    LovPortal,
    MatPortalClient,
    MedPortalClient,
    OntoportalAstroClient,
    OntoPortalClient,
    PreconfiguredOntoPortalClient,
    SIFRBioPortalClient,
    SocioPortal,
    TechnoPortal,
)

__all__ = [
    "AgroPortalClient",
    "BioDivPortal",
    "BioPortalClient",
    "EarthPortal",
    "EcoPortalClient",
    "LovPortal",
    "MatPortalClient",
    "MedPortalClient",
    "OntoPortalClient",
    "OntoportalAstroClient",
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
