# -*- coding: utf-8 -*-

"""Test a client."""

from typing import ClassVar

import unittest_templates

from ontoportal_client import OntoPortalClient

__all__ = ["TestOntoPortalClient"]


class TestOntoPortalClient(unittest_templates.GenericTestCase[OntoPortalClient]):
    """Test a client."""

    test_acronym: ClassVar[str]

    def test_get_ontologies(self):
        """Test getting the ontologies."""
        res = self.instance.get_ontologies()
        self.assertLessEqual(0, len(res))
        acronyms = {entry["acronym"] for entry in res}
        self.assertIn(self.test_acronym, acronyms)
