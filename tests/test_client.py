# -*- coding: utf-8 -*-

"""Test OntoPortal clients."""

from ontoportal_client import BioPortalClient, MatPortalClient, MedPortalClient, SIFRBioPortalClient
from tests import cases


class TestBioPortalClient(cases.TestOntoPortalClient):
    """Test the BioPortal client."""

    client_cls = BioPortalClient
    test_acronym = "GO"


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
