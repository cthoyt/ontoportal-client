# -*- coding: utf-8 -*-

"""Test a client."""

import unittest
from typing import ClassVar, Type

from ontoportal_client import OntoPortalClient

__all__ = ["TestOntoPortalClient"]


class TestOntoPortalClient(unittest.TestCase):
    """Test a client."""

    client_cls: ClassVar[Type[OntoPortalClient]]
    client: ClassVar[OntoPortalClient]
    test_acronym: ClassVar[str]

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the class with an OntoPortal client."""
        cls.client = cls.client_cls()

    def test_get_ontologies(self):
        """Test getting the ontologies."""
        res = self.client.get_ontologies()
        self.assertLessEqual(0, len(res))
        acronyms = {entry["acronym"] for entry in res}
        self.assertIn(self.test_acronym, acronyms)
