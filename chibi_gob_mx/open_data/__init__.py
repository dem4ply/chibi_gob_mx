from chibi.atlas import Chibi_atlas
from chibi_requests_site import Site_paginate_by_url
from .data_set import Data_set


class Open_data( Site_paginate_by_url ):
    url = 'https://datos.gob.mx/busca/dataset'

    @property
    def last_page( self ):
        pagination = self.soup.find( **{ 'class': "pagination" } )
        pages = pagination.find_all( 'a' )
        pages = list( filter( lambda x: x.text.isnumeric(), pages ) )
        return int( pages[-1].text )

    def __iter__( self ):
        for dataset in self.datasets:
            yield Data_set( url=dataset.url, parent=self )
        for page in self.pages:
            for dataset in page.datasets:
                yield Data_set( url=dataset.url, parent=self )

    @property
    def datasets( self ):
        for dataset in self.info.datasets:
            yield Data_set( url=dataset.url, parent=self )

    def parse_info( self ):
        result = Chibi_atlas()
        result.datasets = []
        datasets = self.soup.find_all(
            **{ 'class': "dataset-item row dataset-item" } )

        for dataset in datasets:
            d = Chibi_atlas()
            d.url = self.url + dataset.h3.a.attrs[ 'href' ]
            result.datasets.append( d )
        return result
