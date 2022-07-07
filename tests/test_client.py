# -*- coding: utf-8 -*-

"""Test a client."""

import unittest
from typing import ClassVar

from ontoportal_client import BioPortalClient, OntoPortalClient


class TestBioPortalClient(unittest.TestCase):
    """Test a client."""

    client: ClassVar[OntoPortalClient]

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the class with a BioPortal client."""
        cls.client = BioPortalClient()

    def test_get_ontologies(self):
        """Test getting the ontologies."""
        res = self.client.get_ontologies()
        acronyms = {entry["acronym"] for entry in res}
        self.assertIn("GO", acronyms)
