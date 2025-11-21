"""Test OntoPortal clients."""

from collections.abc import Collection
from itertools import islice
from typing import ClassVar

import unittest_templates

from ontoportal_client.api import (
    AgroPortalClient,
    IndustryPortalClient,
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

    cls: ClassVar[type[OntoPortalClient]] = BioPortalClient
    test_acronym: ClassVar[str] = "GO"

    def test_search(self) -> None:
        """Test searching an ontology."""
        records = islice(
            self.instance.search("tentacle pocket"), 100
        )  # only grab first two pages or so
        ids = {record["@id"] for record in records}
        self.assertIn("http://purl.obolibrary.org/obo/CEPH_0000259", ids)

    def test_search_pagination(self) -> None:
        """Test searching an ontology and verify that all results are accessible."""
        actual_count = 0
        expected_counts = []
        for page in self.instance.search_paginated("tentacle pocket"):
            actual_count += len(page["collection"])
            expected_counts.append(page["totalCount"])
        self.assertEqual(
            1, len(set(expected_counts)), msg="total count was inconsistent throughout pages"
        )
        self.assertEqual(expected_counts[0], actual_count)

    def test_annotate(self) -> None:
        """Test annotating a term."""
        res = self.instance.annotate("hippocampal neuron from human")
        self.assertTrue(
            any(
                record["annotatedClass"]["@id"] == "http://purl.obolibrary.org/obo/NCBITaxon_9606"
                for record in res
            )
        )

    def test_ancestors(self) -> None:
        """Test searching an ontology."""
        res = self.instance.get_ancestors(
            ontology="GO", uri="http://purl.obolibrary.org/obo/GO_0005773"
        )
        ids = {record["@id"] for record in res}
        self.assertIn("http://purl.obolibrary.org/obo/GO_0005575", ids)  # cellular_component
        self.assertIn("http://purl.obolibrary.org/obo/GO_0005737", ids)  # cytoplasm


class TestEcoPortalClient(cases.TestOntoPortalClient):
    """Test the EcoPortal client."""

    cls: ClassVar[type[OntoPortalClient]] = EcoPortalClient
    test_acronym: ClassVar[str] = "AGROVOC"


class TestAgroPortalClient(cases.TestOntoPortalClient):
    """Test the AgroPortal client."""

    cls: ClassVar[type[OntoPortalClient]] = AgroPortalClient
    test_acronym: ClassVar[str] = "AGROVOC"


class TestMatPortalClient(cases.TestOntoPortalClient):
    """Test the MatPortal client."""

    cls: ClassVar[type[OntoPortalClient]] = MatPortalClient
    test_acronym: ClassVar[str] = "DRMO"


class TestSIFRBioPortalClient(cases.TestOntoPortalClient):
    """Test the SIFR BioPortal client."""

    cls: ClassVar[type[OntoPortalClient]] = SIFRBioPortalClient
    test_acronym: ClassVar[str] = "NABM"


class TestMedPortalClient(cases.TestOntoPortalClient):
    """Test the MedPortal client."""

    cls: ClassVar[type[OntoPortalClient]] = MedPortalClient
    test_acronym: ClassVar[str] = "DOID"


class TestIndustryPortalClient(cases.TestOntoPortalClient):
    """Test the IndustryPortal client."""

    cls: ClassVar[type[OntoPortalClient]] = IndustryPortalClient
    test_acronym: ClassVar[str] = "EMMO"


class TestClients(unittest_templates.MetaTestCase[OntoPortalClient]):
    """Test that the loss functions all have tests."""

    base_cls: ClassVar[type[OntoPortalClient]] = OntoPortalClient
    base_test: ClassVar[type[unittest_templates.GenericTestCase[OntoPortalClient]]] = (
        cases.TestOntoPortalClient
    )
    skip_cls: ClassVar[Collection[type[OntoPortalClient]]] = {
        PreconfiguredOntoPortalClient,
    }
