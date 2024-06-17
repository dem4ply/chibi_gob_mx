import datetime
import dateparser
from chibi_requests import Chibi_url
from chibi.atlas import Chibi_atlas
from chibi_requests_site import Site
from chibi_gob_mx.open_data.data_set_activity import Dataset_activity
import logging


logger = logging.getLogger( 'chibi_gob_mx.open_data.data_set' )


class Data_set( Site ):
    def parse_info( self ):
        result = Chibi_atlas()
        tags = self.soup.find_all( **{ 'class': 'tag' } )
        result.tags = [ t.text for t in tags ]
        result.resources = []
        drops = self.soup.find_all(
            **{ 'class': 'resource-item dataset-item row' } )
        for drop in drops:
            title = drop.find( 'a', **{ 'class': 'heading' } ).h4.text
            description = drop.find(
                'p', **{ 'class': 'description' } )
            if description:
                description = description.text.strip()
            if drop.img:
                kind = drop.img.attrs[ 'alt' ]
            else:
                kind = None
            download_link = drop.find(
                **{ 'class': 'dropdown-container' } ).a.attrs[ 'href' ]
            resource = Chibi_atlas(
                title=title, download_link=download_link,
                decription=description, kind=kind )
            result.resources.append( resource )
        return result

    def parse_metadata( self ):
        result = Chibi_atlas()
        rows = self.soup.table.tbody.find_all( 'tr' )
        for row in rows:
            value = row.td.text.strip()
            key = row.th.text.strip()
            key = "_".join( key.split( ' ' ) )
            key = key.lower()
            if key == 'email_del_publicador':
                key = 'email_publisher'
                value = value.lower()
            elif key == 'nombre_del_publicador':
                key = 'name_publisher'
                value = value.lower()
            elif key == 'idioma':
                key = 'language'
                value = value.lower()
            elif key == 'frecuencia':
                key = 'frequency'
                value = value.lower()
            elif key == 'modificado':
                key = 'modified'
                value = dateparser.parse( value )
            elif key == 'publicado':
                key = 'published'
                value = dateparser.parse( value )
            result[ key ] = value
        return result

    @property
    def activity( self ):
        try:
            return self._activity
        except AttributeError:
            tabs = self.soup.find( **{ 'class': 'nav nav-tabs' } )
            url = tabs.find_all( 'a' )[1].attrs[ 'href' ]
            self._activity = Dataset_activity( self.url + url, parent=self )
            return self._activity

    def response_is_ok( self, response ):
        is_ok = not response._response.url.endswith( '404.html' )
        if not is_ok:
            logger.warning( f'no se encontro "{self.url}"' )
            for i, request in enumerate( response._response.history ):
                logger.warning( f'history {i}: {request.url}' )
        return is_ok
