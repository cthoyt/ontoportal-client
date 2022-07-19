# -*- coding: utf-8 -*-

"""Test OntoPortal clients."""

from ontoportal_client import (
    AgroPortalClient,
    BioPortalClient,
    EcoPortalClient,
    MatPortalClient,
    MedPortalClient,
    OntoPortalClient,
    SIFRBioPortalClient,
)
from tests import cases


class TestBioPortalClient(cases.TestOntoPortalClient):
    """Test the BioPortal client."""

    client_cls = BioPortalClient
    test_acronym = "GO"


class TestEcoPortalClient(cases.TestOntoPortalClient):
    """Test the EcoPortal client."""

    client_cls = EcoPortalClient
    test_acronym = "ENVO"


class TestAgroPortalClient(cases.TestOntoPortalClient):
    """Test the AgroPortal client."""

    client_cls = AgroPortalClient
    test_acronym = "AGROVOC"


class TestMatPortalClient(cases.TestOntoPortalClient):
    """Test the MatPortal client."""

    client_cls = MatPortalClient
    test_acronym = "DISO"


class SIFRBioPortalClient(cases.TestOntoPortalClient):
    """Test the SIFR BioPortal client."""

    client_cls = SIFRBioPortalClient
    test_acronym = "NABM"


class TestMedPortalClient(cases.TestOntoPortalClient):
    """Test the MedPortal client."""

    client_cls = MedPortalClient
    test_acronym = "DOID"


class TestClients(unittest_templates.MetaTestCase[OntoPortalClient]):
    """Test that the loss functions all have tests."""

    base_cls = OntoPortalClient
    base_test = cases.TestOntoPortalClient
