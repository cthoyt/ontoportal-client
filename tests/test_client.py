# -*- coding: utf-8 -*-

"""Test OntoPortal clients."""

from itertools import islice

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

    def test_search(self):
        """Test searching an ontology."""
        records = islice(
            self.instance.search("tentacle pocket"), 100
        )  # only grab first two pages or so
        ids = {record["@id"] for record in records}
        self.assertIn("http://purl.obolibrary.org/obo/CEPH_0000259", ids)

    def test_search_pagination(self):
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

    def test_annotate(self):
        """Test annotating a term."""
        res = self.instance.annotate("hippocampal neuron from human")
        self.assertTrue(
            any(
                record["annotatedClass"]["@id"] == "http://purl.obolibrary.org/obo/NCBITaxon_9606"
                for record in res
            )
        )

    def test_ancestors(self):
        """Test searching an ontology."""
        res = self.instance.get_ancestors(
            ontology="GO", uri="http://purl.obolibrary.org/obo/GO_0005773"
        )
        ids = {record["@id"] for record in res}
        self.assertIn("http://purl.obolibrary.org/obo/GO_0005575", ids)  # cellular_component
        self.assertIn("http://purl.obolibrary.org/obo/GO_0005737", ids)  # cytoplasm


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
