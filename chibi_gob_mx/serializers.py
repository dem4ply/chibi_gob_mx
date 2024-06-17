from marshmallow import Schema, fields as f, pre_load, EXCLUDE


class Catalog( Schema ):
    id = f.String( data_key='_id', required=True )
    count = f.Integer( required=True )
    endpoint = f.String( required=True )
    origin_url = f.Url( data_key='url', required=True )
    fields = f.List(
        f.String, data_key='variables', required=False, missing=list )
    name = f.String( required=False )


    @pre_load( pass_many=True )
    def get_result( self, data, **kw ):
        self.many = True
        return data[ 'results' ]

    class Meta:
        unknown = EXCLUDE


class Disaster( Schema ):
    id = f.String( data_key='_id', required=True )
    id_state = f.String( data_key='cve_ent', required=True )
    state = f.String( data_key='nom_ent', required=True )
    municipality = f.String( data_key='nom_mun', required=True )
    id_municipality = f.String( data_key='cve_mun', required=True )
    description = f.String( data_key='descripcion', required=True )
    date = f.DateTime( data_key='fecha', required=False, allow_none=True )

    protected_natual_areas = f.Number(
        data_key='areas_naturales_protegidas', required=True )
    cartwright = f.Number(
        data_key='carretero', required=True )
    culture = f.Number(
        data_key='cultura', required=True )
    sport = f.Number(
        data_key='deportivo', required=True )
    educational = f.Number(
        data_key='educativo', required=True )
    forest_and_vivarium = f.Number(
        data_key='forestal_y_de_viveros', required=True )
    hydraulic = f.Number(
        data_key='hidraulico', required=True )
    indigenous_infrastructure = f.Number(
        data_key='infraestructura_indigena', required=True )
    military = f.Number(
        data_key='militar', required=True )
    archaeological_monuments = f.Number(
        data_key='monumentos_arqueologicos', required=True )
    naval = f.Number(
        data_key='naval', required=True )
    municipal_palaces = f.Number(
        data_key='palacios_municipales', required=True )
    fishing_and_aquaculture = f.Number(
        data_key='pesquero_y_acuicola', required=True )
    port = f.Number(
        data_key='portuario', required=True )
    solid_wasted = f.Number(
        data_key='residuos_solidos', required=True )
    health = f.Number(
        data_key='salud', required=True )
    tourism = f.Number(
        data_key='turistico', required=True )
    urban = f.Number(
        data_key='urbano', required=True )
    living_place = f.Number(
        data_key='vivienda', required=True )
    coast_zones = f.Number(
        data_key='zonas_costeras', required=True )


    @pre_load( pass_many=True )
    def get_result( self, data, **kw ):
        self.many = True
        for d in data[ 'results' ]:
            if d[ 'fecha' ] == 'NA':
                d[ 'fecha' ] = None
        return data[ 'results' ]

    class Meta:
        unknown = EXCLUDE
