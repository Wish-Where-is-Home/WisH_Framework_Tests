from django.db import models

class GeoBuildingsAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_buildings_a_free'


class GeoLanduseAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_landuse_a_free'


class GeoNaturalAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_natural_a_free'


class GeoNaturalFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_natural_free'


class GeoPlacesAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    population = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_places_a_free'


class GeoPlacesFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    population = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_places_free'


class GeoPofwAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_pofw_a_free'


class GeoPofwFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_pofw_free'


class GeoPoisAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_pois_a_free'


class GeoPoisFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_pois_free'


class GeoRailwaysFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    layer = models.FloatField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_railways_free'


class GeoRoadsFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.SmallIntegerField(blank=True, null=True)
    layer = models.FloatField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_roads_free'


class GeoTrafficAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_traffic_a_free'


class GeoTrafficFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_traffic_free'


class GeoTransportAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_transport_a_free'


class GeoTransportFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_transport_free'


class GeoWaterAFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_water_a_free'


class GeoWaterwaysFree(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_waterways_free'

class Portugal2011Bgri11Ac25(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objectid_12 = models.BigIntegerField(db_column='OBJECTID_12', blank=True, null=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dtmn11 = models.CharField(db_column='DTMN11', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fr11 = models.CharField(db_column='FR11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sec11 = models.CharField(db_column='SEC11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ss11 = models.CharField(db_column='SS11', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bgri11 = models.CharField(db_column='BGRI11', max_length=11, blank=True, null=True)  # Field name made lowercase.
    lug11 = models.CharField(db_column='LUG11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lug11desig = models.CharField(db_column='LUG11DESIG', max_length=90, blank=True, null=True)  # Field name made lowercase.
    n_aloj = models.IntegerField(db_column='N_ALOJ', blank=True, null=True)  # Field name made lowercase.
    objectid_1 = models.IntegerField(db_column='OBJECTID_1', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    geo_cod = models.CharField(db_column='GEO_COD', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    geo_cod_dsg = models.CharField(db_column='GEO_COD_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nivel_dsg = models.CharField(db_column='NIVEL_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_1ou2 = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_1OU2', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_isolados = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_ISOLADOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_gemin = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_GEMIN', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_embanda = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_EMBANDA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_3oumais = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_3OUMAIS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_outros = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_OUTROS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_exclusiv_resid = models.IntegerField(db_column='N_EDIFICIOS_EXCLUSIV_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_principal_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIPAL_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_princip_nao_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIP_NAO_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_1ou2_pisos = models.IntegerField(db_column='N_EDIFICIOS_1OU2_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_3ou4_pisos = models.IntegerField(db_column='N_EDIFICIOS_3OU4_PISOS', blank=True, null=True)  # Field name made lowercase.
    f_n_edificios_5ou_mais_pisos = models.IntegerField(db_column='F_N_EDIFICIOS_5OU_MAIS_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_antes_1919 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_ANTES_1919', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1919a1945 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1919A1945', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1946a1960 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1946A1960', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1961a1970 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1961A1970', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1971a1980 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1971A1980', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1981a1990 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1981A1990', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1991a1995 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1991A1995', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1996a2000 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1996A2000', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2001a2005 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2001A2005', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2006a2011 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2006A2011', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_betao = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_BETAO', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_com_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_COM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_sem_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_SEM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_adobe_pedra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_ADOBE_PEDRA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_outra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_OUTRA', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos = models.IntegerField(db_column='N_ALOJAMENTOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_familiares = models.IntegerField(db_column='N_ALOJAMENTOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_n_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_N_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_colectivos = models.IntegerField(db_column='N_ALOJAMENTOS_COLECTIVOS', blank=True, null=True)  # Field name made lowercase.
    n_classicos_res_habitual = models.IntegerField(db_column='N_CLASSICOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_res_habitual = models.IntegerField(db_column='N_ALOJAMENTOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_vagos = models.IntegerField(db_column='N_ALOJAMENTOS_VAGOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_agua = models.IntegerField(db_column='N_RES_HABITUAL_COM_AGUA', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_retrete = models.IntegerField(db_column='N_RES_HABITUAL_COM_RETRETE', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_esgotos = models.IntegerField(db_column='N_RES_HABITUAL_COM_ESGOTOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_banho = models.IntegerField(db_column='N_RES_HABITUAL_COM_BANHO', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50_100 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50_100', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_100_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_100_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_1_2_div = models.IntegerField(db_column='N_RES_HABITUAL_1_2_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_3_4_div = models.IntegerField(db_column='N_RES_HABITUAL_3_4_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_1 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_1', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_2 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_2', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_3 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_3', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_prop_ocup = models.IntegerField(db_column='N_RES_HABITUAL_PROP_OCUP', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_arrend = models.IntegerField(db_column='N_RES_HABITUAL_ARREND', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS', blank=True, null=True)  # Field name made lowercase.
    n_familias_institucionais = models.IntegerField(db_column='N_FAMILIAS_INSTITUCIONAIS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_1ou2_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_1OU2_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_3ou4_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_3OU4_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes65 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES65', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes14 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES14', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_sem_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_SEM_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_1desempreg = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_1DESEMPREG', blank=True, null=True)  # Field name made lowercase.
    n_familias_class_2mais_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASS_2MAIS_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_familiares = models.IntegerField(db_column='N_NUCLEOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_1filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_1FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_2filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_2FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_6anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_6ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_mais_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_MAIS_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_h = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_m = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_65', blank=True, null=True)  # Field name made lowercase.
    n_indiv_resident_n_ler_escrv = models.IntegerField(db_column='N_INDIV_RESIDENT_N_LER_ESCRV', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_1bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_2bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_3bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_possec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_POSSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sup = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_1bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_2bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_3bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_posec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_POSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sup = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_1emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_1EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empregados = models.IntegerField(db_column='N_IND_RESID_EMPREGADOS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_pens_reform = models.IntegerField(db_column='N_IND_RESID_PENS_REFORM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_sem_act_econ = models.IntegerField(db_column='N_IND_RESID_SEM_ACT_ECON', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_prim = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_PRIM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_seq = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_SEQ', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_terc = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_TERC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_estud_mun_resid = models.IntegerField(db_column='N_IND_RESID_ESTUD_MUN_RESID', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_trab_mun_resid = models.IntegerField(db_column='N_IND_RESID_TRAB_MUN_RESID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portugal2011 — BGRI11_AC25'


class Portugal2011Bgri11Ac26(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objectid_12 = models.BigIntegerField(db_column='OBJECTID_12', blank=True, null=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dtmn11 = models.CharField(db_column='DTMN11', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fr11 = models.CharField(db_column='FR11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sec11 = models.CharField(db_column='SEC11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ss11 = models.CharField(db_column='SS11', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bgri11 = models.CharField(db_column='BGRI11', max_length=11, blank=True, null=True)  # Field name made lowercase.
    lug11 = models.CharField(db_column='LUG11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lug11desig = models.CharField(db_column='LUG11DESIG', max_length=90, blank=True, null=True)  # Field name made lowercase.
    n_aloj = models.IntegerField(db_column='N_ALOJ', blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    len = models.FloatField(db_column='LEN', blank=True, null=True)  # Field name made lowercase.
    objectid_1 = models.IntegerField(db_column='OBJECTID_1', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    geo_cod = models.CharField(db_column='GEO_COD', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    geo_cod_dsg = models.CharField(db_column='GEO_COD_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nivel_dsg = models.CharField(db_column='NIVEL_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_1ou2 = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_1OU2', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_isolados = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_ISOLADOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_gemin = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_GEMIN', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_embanda = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_EMBANDA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_3oumais = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_3OUMAIS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_outros = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_OUTROS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_exclusiv_resid = models.IntegerField(db_column='N_EDIFICIOS_EXCLUSIV_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_principal_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIPAL_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_princip_nao_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIP_NAO_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_1ou2_pisos = models.IntegerField(db_column='N_EDIFICIOS_1OU2_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_3ou4_pisos = models.IntegerField(db_column='N_EDIFICIOS_3OU4_PISOS', blank=True, null=True)  # Field name made lowercase.
    f_n_edificios_5ou_mais_pisos = models.IntegerField(db_column='F_N_EDIFICIOS_5OU_MAIS_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_antes_1919 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_ANTES_1919', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1919a1945 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1919A1945', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1946a1960 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1946A1960', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1961a1970 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1961A1970', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1971a1980 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1971A1980', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1981a1990 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1981A1990', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1991a1995 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1991A1995', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1996a2000 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1996A2000', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2001a2005 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2001A2005', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2006a2011 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2006A2011', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_betao = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_BETAO', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_com_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_COM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_sem_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_SEM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_adobe_pedra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_ADOBE_PEDRA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_outra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_OUTRA', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos = models.IntegerField(db_column='N_ALOJAMENTOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_familiares = models.IntegerField(db_column='N_ALOJAMENTOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_n_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_N_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_colectivos = models.IntegerField(db_column='N_ALOJAMENTOS_COLECTIVOS', blank=True, null=True)  # Field name made lowercase.
    n_classicos_res_habitual = models.IntegerField(db_column='N_CLASSICOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_res_habitual = models.IntegerField(db_column='N_ALOJAMENTOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_vagos = models.IntegerField(db_column='N_ALOJAMENTOS_VAGOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_agua = models.IntegerField(db_column='N_RES_HABITUAL_COM_AGUA', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_retrete = models.IntegerField(db_column='N_RES_HABITUAL_COM_RETRETE', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_esgotos = models.IntegerField(db_column='N_RES_HABITUAL_COM_ESGOTOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_banho = models.IntegerField(db_column='N_RES_HABITUAL_COM_BANHO', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50_100 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50_100', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_100_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_100_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_1_2_div = models.IntegerField(db_column='N_RES_HABITUAL_1_2_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_3_4_div = models.IntegerField(db_column='N_RES_HABITUAL_3_4_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_1 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_1', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_2 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_2', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_3 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_3', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_prop_ocup = models.IntegerField(db_column='N_RES_HABITUAL_PROP_OCUP', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_arrend = models.IntegerField(db_column='N_RES_HABITUAL_ARREND', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS', blank=True, null=True)  # Field name made lowercase.
    n_familias_institucionais = models.IntegerField(db_column='N_FAMILIAS_INSTITUCIONAIS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_1ou2_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_1OU2_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_3ou4_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_3OU4_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes65 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES65', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes14 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES14', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_sem_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_SEM_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_1desempreg = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_1DESEMPREG', blank=True, null=True)  # Field name made lowercase.
    n_familias_class_2mais_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASS_2MAIS_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_familiares = models.IntegerField(db_column='N_NUCLEOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_1filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_1FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_2filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_2FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_6anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_6ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_mais_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_MAIS_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_h = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_m = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_65', blank=True, null=True)  # Field name made lowercase.
    n_indiv_resident_n_ler_escrv = models.IntegerField(db_column='N_INDIV_RESIDENT_N_LER_ESCRV', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_1bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_2bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_3bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_possec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_POSSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sup = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_1bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_2bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_3bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_posec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_POSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sup = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_1emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_1EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empregados = models.IntegerField(db_column='N_IND_RESID_EMPREGADOS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_pens_reform = models.IntegerField(db_column='N_IND_RESID_PENS_REFORM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_sem_act_econ = models.IntegerField(db_column='N_IND_RESID_SEM_ACT_ECON', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_prim = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_PRIM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_seq = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_SEQ', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_terc = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_TERC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_estud_mun_resid = models.IntegerField(db_column='N_IND_RESID_ESTUD_MUN_RESID', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_trab_mun_resid = models.IntegerField(db_column='N_IND_RESID_TRAB_MUN_RESID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portugal2011 — BGRI11_AC26'


class Portugal2011Bgri11Cont(models.Model):
    geom = models.MultiPolygonField(srid=3763, blank=True, null=True)
    objectid_1 = models.BigIntegerField(db_column='OBJECTID_1', blank=True, null=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dtmn11 = models.CharField(db_column='DTMN11', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fr11 = models.CharField(db_column='FR11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sec11 = models.CharField(db_column='SEC11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ss11 = models.CharField(db_column='SS11', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bgri11 = models.CharField(db_column='BGRI11', max_length=11, blank=True, null=True)  # Field name made lowercase.
    lug11 = models.CharField(db_column='LUG11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lug11desig = models.CharField(db_column='LUG11DESIG', max_length=90, blank=True, null=True)  # Field name made lowercase.
    objectid_12 = models.IntegerField(db_column='OBJECTID_12', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    geo_cod = models.CharField(db_column='GEO_COD', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    geo_cod_dsg = models.CharField(db_column='GEO_COD_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nivel_dsg = models.CharField(db_column='NIVEL_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_1ou2 = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_1OU2', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_isolados = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_ISOLADOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_gemin = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_GEMIN', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_embanda = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_EMBANDA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_3oumais = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_3OUMAIS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_outros = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_OUTROS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_exclusiv_resid = models.IntegerField(db_column='N_EDIFICIOS_EXCLUSIV_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_principal_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIPAL_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_princip_nao_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIP_NAO_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_1ou2_pisos = models.IntegerField(db_column='N_EDIFICIOS_1OU2_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_3ou4_pisos = models.IntegerField(db_column='N_EDIFICIOS_3OU4_PISOS', blank=True, null=True)  # Field name made lowercase.
    f_n_edificios_5ou_mais_pisos = models.IntegerField(db_column='F_N_EDIFICIOS_5OU_MAIS_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_antes_1919 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_ANTES_1919', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1919a1945 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1919A1945', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1946a1960 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1946A1960', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1961a1970 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1961A1970', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1971a1980 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1971A1980', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1981a1990 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1981A1990', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1991a1995 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1991A1995', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1996a2000 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1996A2000', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2001a2005 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2001A2005', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2006a2011 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2006A2011', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_betao = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_BETAO', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_com_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_COM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_sem_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_SEM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_adobe_pedra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_ADOBE_PEDRA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_outra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_OUTRA', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos = models.IntegerField(db_column='N_ALOJAMENTOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_familiares = models.IntegerField(db_column='N_ALOJAMENTOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_n_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_N_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_colectivos = models.IntegerField(db_column='N_ALOJAMENTOS_COLECTIVOS', blank=True, null=True)  # Field name made lowercase.
    n_classicos_res_habitual = models.IntegerField(db_column='N_CLASSICOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_res_habitual = models.IntegerField(db_column='N_ALOJAMENTOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_vagos = models.IntegerField(db_column='N_ALOJAMENTOS_VAGOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_agua = models.IntegerField(db_column='N_RES_HABITUAL_COM_AGUA', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_retrete = models.IntegerField(db_column='N_RES_HABITUAL_COM_RETRETE', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_esgotos = models.IntegerField(db_column='N_RES_HABITUAL_COM_ESGOTOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_banho = models.IntegerField(db_column='N_RES_HABITUAL_COM_BANHO', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50_100 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50_100', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_100_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_100_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_1_2_div = models.IntegerField(db_column='N_RES_HABITUAL_1_2_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_3_4_div = models.IntegerField(db_column='N_RES_HABITUAL_3_4_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_1 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_1', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_2 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_2', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_3 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_3', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_prop_ocup = models.IntegerField(db_column='N_RES_HABITUAL_PROP_OCUP', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_arrend = models.IntegerField(db_column='N_RES_HABITUAL_ARREND', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS', blank=True, null=True)  # Field name made lowercase.
    n_familias_institucionais = models.IntegerField(db_column='N_FAMILIAS_INSTITUCIONAIS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_1ou2_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_1OU2_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_3ou4_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_3OU4_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes65 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES65', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes14 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES14', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_sem_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_SEM_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_1desempreg = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_1DESEMPREG', blank=True, null=True)  # Field name made lowercase.
    n_familias_class_2mais_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASS_2MAIS_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_familiares = models.IntegerField(db_column='N_NUCLEOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_1filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_1FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_2filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_2FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_6anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_6ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_mais_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_MAIS_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_h = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_m = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_65', blank=True, null=True)  # Field name made lowercase.
    n_indiv_resident_n_ler_escrv = models.IntegerField(db_column='N_INDIV_RESIDENT_N_LER_ESCRV', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_1bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_2bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_3bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_possec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_POSSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sup = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_1bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_2bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_3bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_posec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_POSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sup = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_1emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_1EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empregados = models.IntegerField(db_column='N_IND_RESID_EMPREGADOS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_pens_reform = models.IntegerField(db_column='N_IND_RESID_PENS_REFORM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_sem_act_econ = models.IntegerField(db_column='N_IND_RESID_SEM_ACT_ECON', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_prim = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_PRIM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_seq = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_SEQ', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_terc = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_TERC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_estud_mun_resid = models.IntegerField(db_column='N_IND_RESID_ESTUD_MUN_RESID', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_trab_mun_resid = models.IntegerField(db_column='N_IND_RESID_TRAB_MUN_RESID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portugal2011 — BGRI11_CONT'


class Portugal2011Bgri11Mad(models.Model):
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)
    objectid_12 = models.BigIntegerField(db_column='OBJECTID_12', blank=True, null=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    dtmn11 = models.CharField(db_column='DTMN11', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fr11 = models.CharField(db_column='FR11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sec11 = models.CharField(db_column='SEC11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ss11 = models.CharField(db_column='SS11', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bgri11 = models.CharField(db_column='BGRI11', max_length=11, blank=True, null=True)  # Field name made lowercase.
    lug11 = models.CharField(db_column='LUG11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lug11desig = models.CharField(db_column='LUG11DESIG', max_length=90, blank=True, null=True)  # Field name made lowercase.
    objectid_1 = models.IntegerField(db_column='OBJECTID_1', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    geo_cod = models.CharField(db_column='GEO_COD', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    geo_cod_dsg = models.CharField(db_column='GEO_COD_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nivel_dsg = models.CharField(db_column='NIVEL_DSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_1ou2 = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_1OU2', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_isolados = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_ISOLADOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_gemin = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_GEMIN', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_embanda = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_EMBANDA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_3oumais = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_3OUMAIS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_classicos_outros = models.IntegerField(db_column='N_EDIFICIOS_CLASSICOS_OUTROS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_exclusiv_resid = models.IntegerField(db_column='N_EDIFICIOS_EXCLUSIV_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_principal_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIPAL_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_princip_nao_resid = models.IntegerField(db_column='N_EDIFICIOS_PRINCIP_NAO_RESID', blank=True, null=True)  # Field name made lowercase.
    n_edificios_1ou2_pisos = models.IntegerField(db_column='N_EDIFICIOS_1OU2_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_3ou4_pisos = models.IntegerField(db_column='N_EDIFICIOS_3OU4_PISOS', blank=True, null=True)  # Field name made lowercase.
    f_n_edificios_5ou_mais_pisos = models.IntegerField(db_column='F_N_EDIFICIOS_5OU_MAIS_PISOS', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_antes_1919 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_ANTES_1919', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1919a1945 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1919A1945', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1946a1960 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1946A1960', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1961a1970 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1961A1970', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1971a1980 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1971A1980', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1981a1990 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1981A1990', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1991a1995 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1991A1995', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_1996a2000 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_1996A2000', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2001a2005 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2001A2005', blank=True, null=True)  # Field name made lowercase.
    n_edificios_constr_2006a2011 = models.IntegerField(db_column='N_EDIFICIOS_CONSTR_2006A2011', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_betao = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_BETAO', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_com_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_COM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_sem_placa = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_SEM_PLACA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_adobe_pedra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_ADOBE_PEDRA', blank=True, null=True)  # Field name made lowercase.
    n_edificios_estrut_outra = models.IntegerField(db_column='N_EDIFICIOS_ESTRUT_OUTRA', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos = models.IntegerField(db_column='N_ALOJAMENTOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_familiares = models.IntegerField(db_column='N_ALOJAMENTOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_fam_n_classicos = models.IntegerField(db_column='N_ALOJAMENTOS_FAM_N_CLASSICOS', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_colectivos = models.IntegerField(db_column='N_ALOJAMENTOS_COLECTIVOS', blank=True, null=True)  # Field name made lowercase.
    n_classicos_res_habitual = models.IntegerField(db_column='N_CLASSICOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_res_habitual = models.IntegerField(db_column='N_ALOJAMENTOS_RES_HABITUAL', blank=True, null=True)  # Field name made lowercase.
    n_alojamentos_vagos = models.IntegerField(db_column='N_ALOJAMENTOS_VAGOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_agua = models.IntegerField(db_column='N_RES_HABITUAL_COM_AGUA', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_retrete = models.IntegerField(db_column='N_RES_HABITUAL_COM_RETRETE', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_esgotos = models.IntegerField(db_column='N_RES_HABITUAL_COM_ESGOTOS', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_com_banho = models.IntegerField(db_column='N_RES_HABITUAL_COM_BANHO', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_50_100 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_50_100', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_100_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_100_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_area_200 = models.IntegerField(db_column='N_RES_HABITUAL_AREA_200', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_1_2_div = models.IntegerField(db_column='N_RES_HABITUAL_1_2_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_3_4_div = models.IntegerField(db_column='N_RES_HABITUAL_3_4_DIV', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_1 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_1', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_2 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_2', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_estac_3 = models.IntegerField(db_column='N_RES_HABITUAL_ESTAC_3', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_prop_ocup = models.IntegerField(db_column='N_RES_HABITUAL_PROP_OCUP', blank=True, null=True)  # Field name made lowercase.
    n_res_habitual_arrend = models.IntegerField(db_column='N_RES_HABITUAL_ARREND', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS', blank=True, null=True)  # Field name made lowercase.
    n_familias_institucionais = models.IntegerField(db_column='N_FAMILIAS_INSTITUCIONAIS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_1ou2_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_1OU2_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_3ou4_pess = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_3OU4_PESS', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes65 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES65', blank=True, null=True)  # Field name made lowercase.
    n_familias_classicas_npes14 = models.IntegerField(db_column='N_FAMILIAS_CLASSICAS_NPES14', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_sem_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_SEM_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_familias_classic_1desempreg = models.IntegerField(db_column='N_FAMILIAS_CLASSIC_1DESEMPREG', blank=True, null=True)  # Field name made lowercase.
    n_familias_class_2mais_desemp = models.IntegerField(db_column='N_FAMILIAS_CLASS_2MAIS_DESEMP', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_familiares = models.IntegerField(db_column='N_NUCLEOS_FAMILIARES', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_1filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_1FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_2filh_nao_casado = models.IntegerField(db_column='N_NUCLEOS_2FILH_NAO_CASADO', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_6anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_6ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_inf_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_INF_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_nucleos_filh_mais_15anos = models.IntegerField(db_column='N_NUCLEOS_FILH_MAIS_15ANOS', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_h = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_present_m = models.IntegerField(db_column='N_INDIVIDUOS_PRESENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_h_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_H_65', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_0a4 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_0A4', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_5a9 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_5A9', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_10a13 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_10A13', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_14a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_14A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_15a19 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_15A19', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a24 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A24', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_20a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_20A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_25a64 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_25A64', blank=True, null=True)  # Field name made lowercase.
    n_individuos_resident_m_65 = models.IntegerField(db_column='N_INDIVIDUOS_RESIDENT_M_65', blank=True, null=True)  # Field name made lowercase.
    n_indiv_resident_n_ler_escrv = models.IntegerField(db_column='N_INDIV_RESIDENT_N_LER_ESCRV', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_1bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_2bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_3bas = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_possec = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_POSSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_fensino_sup = models.IntegerField(db_column='N_IND_RESIDENT_FENSINO_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_1bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_1BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_2bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_2BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_3bas = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_3BAS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_posec = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_POSEC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resident_ensincomp_sup = models.IntegerField(db_column='N_IND_RESIDENT_ENSINCOMP_SUP', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_1emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_1EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_desemp_proc_emprg = models.IntegerField(db_column='N_IND_RESID_DESEMP_PROC_EMPRG', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empregados = models.IntegerField(db_column='N_IND_RESID_EMPREGADOS', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_pens_reform = models.IntegerField(db_column='N_IND_RESID_PENS_REFORM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_sem_act_econ = models.IntegerField(db_column='N_IND_RESID_SEM_ACT_ECON', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_prim = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_PRIM', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_seq = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_SEQ', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_empreg_sect_terc = models.IntegerField(db_column='N_IND_RESID_EMPREG_SECT_TERC', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_estud_mun_resid = models.IntegerField(db_column='N_IND_RESID_ESTUD_MUN_RESID', blank=True, null=True)  # Field name made lowercase.
    n_ind_resid_trab_mun_resid = models.IntegerField(db_column='N_IND_RESID_TRAB_MUN_RESID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portugal2011 — BGRI11_MAD'

