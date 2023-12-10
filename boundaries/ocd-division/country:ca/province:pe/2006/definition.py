from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.clean_attr('Descriptio')(f)
    if n.lower().startswith('tracadie'):
        return 'Tracadie—Hillsborough Park'
    elif n.lower().startswith('oleary'):
        return "O'Leary—Inverness"
    return n


boundaries.register('Prince Edward Island electoral districts (2006)',
    singular='Prince Edward Island electoral district',
    domain='Prince Edward Island',
    last_updated=date(2013, 7, 16),  # historical
    name_func=namer,
    id_func=boundaries.attr('Name'),
    authority='Her Majesty the Queen in Right of Prince Edward Island',
    source_url='http://www.electionspei.ca/provincial/districts',
    data_url='http://www.electionspei.ca/provincial/details/gis/kml/pei-provincial-districts-all.kml',
    licence_url='http://www.electionspei.ca/apilicense',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:pe'},
)

# The shapefile from gov.pe.ca has 222 features instead of 27:
# source_url='http://www.gov.pe.ca/gis/index.php3?number=77868&lang=E',
# data_url='http://www.gov.pe.ca/photos/original/prov_elect_dist.SHP.zip',
# licence_url='http://www.gov.pe.ca/gis/license_agreement.php3',
