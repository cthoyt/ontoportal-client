# -*- coding: utf-8 -*-

"""Test OntoPortal clients."""

import unittest_templates

from ontoportal_client.api import (
    AgroPortalClient,
    BioPortalClient,
    EcoPortalClient,
    MatPortalClient,
    MedPortalClient,
    OntoPortalClient,
    PreconfiguredOntoPortalClient,
    SIFRBioPortalClient,
)
from tests import cases


class TestBioPortalClient(cases.TestOntoPortalClient):
    """Test the BioPortal client."""

    cls = BioPortalClient
    test_acronym = "GO"


class TestEcoPortalClient(cases.TestOntoPortalClient):
    """Test the EcoPortal client."""

    cls = EcoPortalClient
    test_acronym = "AGROVOC"


class TestAgroPortalClient(cases.TestOntoPortalClient):
    """Test the AgroPortal client."""

    cls = AgroPortalClient
    test_acronym = "AGROVOC"


class TestMatPortalClient(cases.TestOntoPortalClient):
    """Test the MatPortal client."""

    cls = MatPortalClient
    test_acronym = "DISO"


class TestSIFRBioPortalClient(cases.TestOntoPortalClient):
    """Test the SIFR BioPortal client."""

    cls = SIFRBioPortalClient
    test_acronym = "NABM"


class TestMedPortalClient(cases.TestOntoPortalClient):
    """Test the MedPortal client."""

    cls = MedPortalClient
    test_acronym = "DOID"


class TestClients(unittest_templates.MetaTestCase[OntoPortalClient]):
    """Test that the loss functions all have tests."""

    base_cls = OntoPortalClient
    base_test = cases.TestOntoPortalClient
    skip_cls = {
        PreconfiguredOntoPortalClient,
    }
