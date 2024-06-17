from unittest import TestCase, skip
from chibi_gob_mx.open_data import Open_data
from chibi_gob_mx.open_data.data_set import Data_set
import itertools
from vcr_unittest import VCRTestCase


class Test_open_data( VCRTestCase ):
    def setUp( self ):
        self.site = Open_data()
        super().setUp()

    def tearDown( self ):
        del self.site
        super().tearDown

    def test_get_should_work( self ):
        response = self.site.get()
        self.assertEqual( response.status_code, 200  )

    def test_page_should_return_the_current_page( self ):
        self.assertEqual( self.site.current_page, 1 )

    def test_last_page_should_be_a_int( self ):
        self.assertIsInstance( self.site.last_page, int )

    def test_pages_should_return_a_list_of_sites( self ):
        for page in self.site.pages:
            self.assertIsInstance( page, Open_data )

    def test_iter_should_generate_dataset( self ):
        for dataset in itertools.islice( self.site, 30 ):
            self.assertIsInstance( dataset, Data_set )


class Test_data_set( VCRTestCase ):
    def setUp( self ):
        super().setUp()
        self.site = Open_data()
        a = itertools.islice( self.site, 10 )
        next( a )
        self.dataset = next( a )

    def tearDown( self ):
        del self.site
        super().tearDown

    def test_should_have_metadata( self ):
        self.assertTrue( self.dataset.metadata )
        self.assertIsInstance( self.dataset.metadata, dict )

    def test_should_have_info( self ):
        self.assertTrue( self.dataset.info )
        self.assertIsInstance( self.dataset.info, dict )

    def test_should_have_activity( self ):
        self.assertTrue( self.dataset.activity )
        self.assertTrue( self.dataset.activity.info )
