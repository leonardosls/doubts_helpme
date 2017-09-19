from owslib.csw import CatalogueServiceWeb
csw = CatalogueServiceWeb('http://www.metadados.geo.ibge.gov.br/geonetwork_ibge/srv/por/csw')
csw.identification.type
'CSW'
[op.name for op in csw.operations]
csw.getdomain('GetRecords.resultType')
csw.getrecords(keywords=[('bcim')], maxrecords=10000)
csw.results
for rec in csw.records:
    print csw.records[rec].title