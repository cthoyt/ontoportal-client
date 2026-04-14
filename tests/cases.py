"""Test a client."""

from typing import ClassVar

import pystow.config_api
import unittest_templates

from ontoportal_client import OntoPortalClient

__all__ = ["TestOntoPortalClient"]


class TestOntoPortalClient(unittest_templates.GenericTestCase[OntoPortalClient]):
    """Test a client."""

    test_acronym: ClassVar[str]

    def setUp(self) -> None:
        """Set up the test."""
        try:
            super().setUp()
        except pystow.config_api.ConfigError:
            self.skipTest("no configuration available")

    def test_get_ontologies(self) -> None:
        """Test getting the ontologies."""
        res = self.instance.get_ontologies()
        self.assertLessEqual(0, len(res))
        acronyms = {entry["acronym"] for entry in res}
        self.assertIn(self.test_acronym, acronyms)
