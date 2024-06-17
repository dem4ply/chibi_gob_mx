import copy

from chibi.atlas import Atlas
from chibi.chain import Chibi_chain
from chibi.metaphors import Book
from chibi.metaphors.book import End_book
from chibi_requests import Response

from .serializers import (
    Catalog as Catalog_serializer,
    Disaster as Disaster_serializer
)


class Catalog( Response ):
    serializer = Catalog_serializer

    @property
    def native( self ):
        try:
            return self._native
        except AttributeError:
            from chibi_gob_mx.chibi_gob_mx import catalog
            native = self.parse_content_type()
            results = Atlas( native.results )
            page = copy.copy( self.pagination )
            try:
                page.next()
                catalog = catalog + page
                chain_params = dict(
                    next_obj=catalog,
                    retrieve_next=lambda x: catalog.get().native
                )
            except End_book:
                chain_params = dict( next_obj=None, retrieve_next=None )
            self._native = Chibi_chain( results, **chain_params )
            return self._native

    @property
    def pagination( self ):
        try:
            return self._pagination
        except AttributeError:
            native = self.parse_content_type()
            page = native.pagination
            page = Book(
                total_elements=page.total, page_size=page.pageSize,
                page=page.page, offset_dict={
                    'page': 'page', 'page_size': 'pageSize' } )

            self._pagination = page
            return self._pagination


class Disaster( Response ):
    serializer = Disaster_serializer

    @property
    def native( self ):
        try:
            return self._native
        except AttributeError:
            from chibi_gob_mx.chibi_gob_mx import disaster
            native = self.parse_content_type()
            results = Atlas( native )
            page = copy.copy( self.pagination )
            try:
                page.next()
                catalog = disaster + page
                chain_params = dict(
                    next_obj=catalog,
                    retrieve_next=lambda x: catalog.get().native
                )
            except End_book:
                chain_params = dict( next_obj=None, retrieve_next=None )
            self._native = Chibi_chain( results, **chain_params )
            return self._native

    @property
    def pagination( self ):
        try:
            return self._pagination
        except AttributeError:
            native = self.parse_content_type()
            page = native.pagination
            page = Book(
                total_elements=page.total, page_size=page.pageSize,
                page=page.page, offset_dict={
                    'page': 'page', 'page_size': 'pageSize' } )

            self._pagination = page
            return self._pagination

    @property
    def native_is_many( self ):
        return True


"""
class Open_data( Response ):
    def parse_native( self ):
        native = super().parse_native()
        items = native.find_all(
            **{ 'class': "dataset-item row dataset-item" } )
        results = [
            Site( self.url + i.h3.a.attrs[ 'href' ] )
            for i in items ]
        page = copy.copy( self.pagination )
        try:
            page.next()
            next_page = self.url + page
            chain_params = dict(
                next_obj=next_page,
                retrieve_next=lambda x: next_page.get().native
            )
        except End_book:
            chain_params = dict( next_obj=None, retrieve_next=None )
        return Chibi_chain( results, **chain_params )

    @property
    def pagination( self ):
        try:
            return self._pagination
        except AttributeError:
            native = self.parse_content_type()
            current_page = self.url.params.get( 'page', 1 )
            pages = native.find( **{ 'class': "pagination" } ).find_all( 'a' )
            pages = list( filter( lambda x: x.text.isnumeric(), pages ) )
            page = Book(
                total_elements=int( pages[-1].text ), page_size=1,
                page=current_page, offset_dict={ 'page': 'page' } )

            self._pagination = page
            return self._pagination
"""
