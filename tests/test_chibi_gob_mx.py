#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from chibi_gob_mx import catalog


class Test_catalog(unittest.TestCase):
    def test_catalog_should_have_200( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        self.assertIsInstance( response.native, list )

    def test_catalog_should_retrive_the_total_of_elements( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        total_elements = list( response.native )
        self.assertEqual(
            len( total_elements ), response.pagination.total_elements )

    def test_all_the_elements_should_be_dict( self ):
        response = catalog.get()
        self.assertEqual( response.status_code, 200  )
        keys = set()
        for n in response.native:
            self.assertIsInstance( n, dict )
            keys |= set( n.keys() )
