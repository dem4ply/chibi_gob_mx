from dateutil import parser
from dateutil.parser import parse

from chibi_requests import Chibi_url
from chibi.atlas import Chibi_atlas
from chibi_requests_site import Site
import dateparser


class Dataset_activity( Site ):
    def parse_info( self ):
        result = []
        li = self.soup.find_all( 'li', **{ 'class': 'item changed-package' } )
        for l in li:
            r = Chibi_atlas()
            r.user = {}
            user = l.span.a
            r.user.url = self.url + user.attrs[ 'href' ]
            r.user.name = user.text.strip()
            r.action = l.span.next_sibling.strip()
            date = l.find( 'span', **{ 'class': 'date' } ).attrs[ 'title' ]
            date = dateparser.parse( date )
            r.date = date
            result.append( r )
        return result
