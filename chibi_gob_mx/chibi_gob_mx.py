# -*- coding: utf-8 -*-
from chibi_requests import Chibi_url
from chibi_gob_mx.response import Catalog, Disaster#, Open_data


catalog = Chibi_url(
    'https://api.datos.gob.mx/v1/api-catalog', response_class=Catalog )

disaster = Chibi_url(
    'https://api.datos.gob.mx/v2/fonden.desastres', response_class=Disaster )


"""
open_data = Chibi_url(
    'https://datos.gob.mx/busca/dataset', response_class=Open_data )
"""
