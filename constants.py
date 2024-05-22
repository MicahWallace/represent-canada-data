import re

"""
Supplement the master open data catalog spreadsheet, so that the definitions
task performs the correct test for the license.
"""
more_licenses_with_templates = [
    # Open data licenses.
    'http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    'https://www.elections.bc.ca/docs/EBC-Open-Data-Licence.pdf',
    'http://www.electionspei.ca/apilicense',
    # Some rights reserved.
    'http://mli2.gov.mb.ca/app/register/app/index.php',  # no commercial redistribution
    'https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',  # per CIPPIC
    'https://www.geosask.ca/Portal/jsp/terms_popup.jsp',  # per CIPPIC
]

"""
"All rights reserved" licenses.
"""
all_rights_reserved_licenses = [
    'http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',  # open data license pending
    'http://www.elections.on.ca/en/voting-in-ontario/electoral-districts/electoral-districts--maps--shapefiles-and-street-index-guide/limited-use-data-product-licence-agreement.html',  # per CIPPIC
]

"""
The template for "All rights reserved" licenses.
"""
all_rights_reserved_terms_re = re.compile(r'\ADistributed with permission from .+?.  Please direct licensing inquiries and requests to:\n\n(.+)', re.MULTILINE | re.DOTALL)

"""
The exact templates for other licenses.
"""
terms = {
    # Text provided by license ("Open Government Licence" with jurisdiction name).
    'https://open.alberta.ca/licence':                                                                                   'I. Terms of Use. Contains information licensed under the Open Government Licence – Alberta (%s).',  # noqa: E241
    'https://www.barrie.ca/Online%20Services/PublishingImages/OpenData_Images/COB_DataLicense.pdf':                      'I. Terms of Use. Contains information licensed under the Open Government Licence – Barrie (%s).',  # noqa: E241
    'http://data-brantford.opendata.arcgis.com/pages/licence':                                                           'I. Terms of Use. Contains information licensed under the Open Government Licence – Brantford (%s).',  # noqa: E241
    'https://open.canada.ca/en/open-government-licence-canada':                                                          'I. Terms of Use. Contains information licensed under the Open Government Licence – Canada (%s).',  # noqa: E241
    'http://opendata.haldimandcounty.on.ca/':                                                                            'I. Terms of Use. Contains information licensed under the Open Government Licence – Haldimand County (%s).',  # noqa: E241
    'https://www2.gnb.ca/content/dam/gnb/Departments/gs-sg/pdf/OpenDataPolicy.pdf':                                      'I. Terms of Use. Contains information licensed under the Open Government Licence – New Brunswick (%s).',  # noqa: E241
    'http://www.snb.ca/e/2000/data-E.html':                                                                              'I. Terms of Use. Contains information licensed under the Open Government Licence – New Brunswick (%s).',  # noqa: E241
    'https://novascotia.ca/opendata/licence.asp':                                                                        'I. Terms of Use. Contains information licensed under the Open Government Licence – Nova Scotia (%s).',  # noqa: E241
    'https://geohub.lio.gov.on.ca/datasets/school-board-boundaries':                                                     'I. Terms of Use. Contains information licensed under the Open Government Licence – Ontario (%s).',  # noqa: E241
    'https://data.strathcona.ca/licence':                                                                                'I. Terms of Use. Contains information licensed under the Open Government Licence – Strathcona County (%s).',  # noqa: E241
    'https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-licence/':                            'I. Terms of Use. Contains information licensed under the Open Government Licence – Toronto (%s).',  # noqa: E241
    'https://data.winnipeg.ca/open-data-licence':                                                                        'I. Terms of Use. Contains information licensed under the Open Government Licence – Winnipeg (%s).',  # noqa: E241
    'https://open.yukon.ca/open-government-licence-yukon':                                                               'I. Terms of Use. Contains information licensed under the Open Government Licence – Yukon (%s).',  # noqa: E241
    # Text provided by license ("Open Government Licence" with corporation name).
    'https://data.calgary.ca/stories/s/u45n-7awa':                                                                       'I. Terms of Use. Contains information licensed under the Open Government Licence – City of Calgary (%s).',  # noqa: E241
    'https://data.edmonton.ca/stories/s/City-of-Edmonton-Open-Data-Terms-of-Use/msh8-if28/':                             'I. Terms of Use. Contains information licensed under the Open Government Licence – City of Edmonton (%s).',  # noqa: E241
    'https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-version-2-0':                         'I. Terms of Use. Contains information licensed under the Open Government Licence – City of Ottawa (%s).',  # noqa: E241
    'https://www.regina.ca/residents/open-government/open-government-licence/':                                          'I. Terms of Use. Contains information licensed under the Open Government Licence – City of Regina (%s).',  # noqa: E241
    'https://niagaraopendata.ca/pages/open-government-license-2-0-city-of-welland':                                      'I. Terms of Use. Contains information licensed under the Open Government Licence — City of Welland (%s).',  # noqa: E241
    'https://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html':                            'I. Terms of Use. Contains information licensed under the Open Government Licence – County of Grande Prairie (%s).',  # noqa: E241
    'https://map.oshawa.ca/OpenData/Open%20Government%20Licence%20version%202.0%20-%20Oshawa.pdf':                       'I. Terms of Use. Contains information licensed under the Open Government Licence – The Corporation of the City of Oshawa (%s).',  # noqa: E241
    'https://niagaraopendata.ca/pages/open-government-license-2-0-the-corporation-of-the-city-of-st-catharines':         'I. Terms of Use. Contains information licensed under the Open Government Licence — The Corporation of the City of St. Catharines (%s).',  # noqa: E241
    'https://citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf':                                                  'I. Terms of Use. Contains information licensed under the Open Government Licence – The Corporation of the City of Windsor (%s).',  # noqa: E241
    'https://www.arcgis.com/sharing/rest/content/items/2ffb1ce148804fe4ade2414e6ef10d21/data':                           'I. Terms of Use. Contains information licensed under the Open Government Licence – The Corporation of the Municipality of Chatham-Kent (%s).',  # noqa: E241
    'https://whitby.maps.arcgis.com/sharing/rest/content/items/223810efc31c40b3aff99dd74f809a97/data':                   'I. Terms of Use. Contains information licensed under the Open Government Licence – The Corporation of the Town of Whitby (%s).',  # noqa: E241
    'https://niagaraopendata.ca/pages/open-government-licence-2-0-fort-erie':                                            'I. Terms of Use. Contains information licensed under the Open Government Licence - Town of Fort Erie (%s).',  # noqa: E241
    'https://niagaraopendata.ca/pages/open-government-license-2-0-grimsby':                                              'I. Terms of Use. Contains information licensed under the Open Government Licence — Town of Grimsby (%s).',  # noqa: E241
    'https://www.oakville.ca/data/open_data_licence.html':                                                               'I. Terms of Use. Contains information licensed under the Open Government Licence — Town of Oakville (%s).',  # noqa: E241
    # Text provided by license ("Open Government Licence" with spelling variations).
    'https://www.halifax.ca/home/open-data/open-data-license':                                                           'I. Terms of Use. Contains information licenced under the Open Government Licence - Halifax (%s).',  # noqa: E241
    'https://www.nanaimo.ca/your-government/maps-data/open-data-catalogue/open-data-catalogue-licence':                  'I. Terms of Use. Contains information licenced under the Open Government Licence - Nanaimo (%s).',  # noqa: E241
    'https://niagaraopendata.ca/pages/open-government-license-2-0-town-of-lincoln':                                      'I. Terms of Use. Contains information licensed under the Open Government License — The Corporation of the Town of Lincoln (%s).',  # noqa: E241
    # Text provided by license ("Open Data Licence").
    'https://www.greatersudbury.ca/city-hall/open-government/open-data/licence/':                                        'I. Terms of Use. Contains information licensed under the Open Data Licence – City of Greater Sudbury (%s).',  # noqa: E241
    'https://www.cityofkingston.ca/documents/10180/144997/CityofKingston_OpenDataLicense.pdf':                           'I. Terms of Use. Contains information licensed under the Open Data Licence – City of Kingston (%s).',  # noqa: E241
    'https://www.newmarket.ca/TownGovernment/Documents/Newmarket_OpenData_Licence.pdf':                                  'I. Terms of Use. Contains information licensed under the Open Data Licence - Town of Newmarket (%s).',  # noqa: E241
    # Text provided by license ("public sector information").
    'http://data-norfolk.opendata.arcgis.com/pages/terms-of-use':                                                        "I. Terms of Use. Contains public sector Information made available under Norfolk County's Open Data Licence (%s).",  # noqa: E241
    'http://data-markham.opendata.arcgis.com/pages/terms-of-use':                                                        "I. Terms of Use. Contains public sector Information made available under the City of Markham’s Open Data Licence (%s).",  # noqa: E241
    'https://www.pickering.ca/en/city-hall/resources/OpenDataLicencePickeringV1.pdf':                                    "I. Terms of Use. Contains public sector Information made available under The City of Pickering's Open Data Licence (%s).",  # noqa: E241
    'http://townofajax.maps.arcgis.com/sharing/rest/content/items/22e2d8e248724d7cb0310dc2db675abd/data':                "I. Terms of Use. Contains public sector Information made available under The Corporation of the Town of Ajax's Open Data Licence (%s).",  # noqa: E241
    'https://www.durham.ca/en/regional-government/resources/Documents/OpenDataLicenceAgreement.pdf':                     "I. Terms of Use. Contains public sector Information made available under The Regional Municipality of Durham's Open Data Licence (%s).",  # noqa: E241
    'http://opendata.peelregion.ca/terms-of-use.aspx':                                                                   "I. Terms of Use. Contains public sector Information made available under The Regional Municipality of Peel's Open Data Licence - Version 1.0 (%s).",  # noqa: E241
    # Text provided by license.
    'https://www.elections.bc.ca/docs/EBC-Open-Data-Licence.pdf':                                                        'I. Terms of Use. Contains information licenced under the Elections BC Open Data Licence (%s).',  # noqa: E241
    'http://data.open.guelph.ca/pages/open-government-licence':                                                          'I. Terms of Use. Contains information provided by the City of Guelph under an open government license (%s).',  # noqa: E241
    'https://www.hamilton.ca/city-initiatives/strategies-actions/open-data-licence-terms-and-conditions':                "I. Terms of Use. Contains public sector Data made available under the City of Hamilton’s Open Data Licence (%s).",  # noqa: E241
    'https://www.milton.ca/en/townhall/resources/OpenDataAgreement.pdf':                                                 "I. Terms of Use. Contains public sector Datasets made available under the Town of Milton's Open Data License v.1 (%s).",  # noqa: E241
    'https://www.regionofwaterloo.ca/en/regional-government/open-data.aspx':                                             'I. Terms of Use. Contains information provided by the Regional Municipality of Waterloo under licence (%s).',  # noqa: E241
    # Text previously provided by license.
    'http://donnees.ville.montreal.qc.ca/portail/licence/':                                                              "I. Termes d'utilisation. Contient des données reproduites, modifiées, traduites ou distribuées « telles quelles » avec la permission de la Ville de Montréal (%s).",  # noqa: E241
    'http://www.electionspei.ca/apilicense':                                                                             'I. Terms of Use. This information is provided by Elections PEI under the Elections PEI Data License (%s).',  # noqa: E241
    # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
    'https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php': """Attribution: This data is provided by the Directeur général des élections du Québec (http://www.electionsquebec.qc.ca), reproduced according to the terms of the "Conditions d'utilisation de notre site Web" (%s). Copyright in the work belongs to the Government of Quebec.""",
    'https://smartcity.mississauga.ca/wp-content/uploads/2021/04/CityofMississauga_TermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Mississauga – Terms of Use” (%s).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    # @see Gowlings advice.
    'https://www.burlington.ca/en/services-for-you/resources/Ongoing_Projects/Open_Data/OpenDataBurlingtonTermsOfUseSeptember192011.pdf': 'I. Terms of Use. This work is provided under the terms of “Terms of Use for Open Data Burlington” (%s).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf': 'I. Attribution. This data is provided by GeoNB – www.snb.ca/geonb. This attribution does not constitute an endorsement by Service New Brunswick or its GeoNB partners.\n\nII. Warranty, Liability, Indemnity of Service New Brunswick and its GeoNB partners.\n1. Except as expressly provided in the “GeoNB License Agreement” (%s), this data is provided “As is” without any representations, warranties, guarantees or conditions, of any kind, whether expressed or implied, statutory or otherwise.\n2. Service New Brunswick (SNB) makes no representation or warranty of any kind with respect to the accuracy, usefulness, novelty, validity, scope, completeness or currency of the data and expressly disclaims any implied warranty of merchantability or fitness for a particular purpose of the data. SNB does not ensure or warrant compatibility with past, current or future versions of your browser to access the data.\n3. The Licensee shall have no recourse against SNB, nor its GeoNB partners, whether by way of any suit or action, for any loss, liability, damage or cost that the Licensee may suffer or incur at any time, by reason of the Licensee’s possession or use of the data.\n4. The Licensee shall indemnify SNB, and its GeoNB partners, and their officers, employees, agents and contractors from all claims alleging loss, costs, expenses, damages or injuries (including injuries resulting in death) arising out of the Licensee’s possession or use of the data.\n5. The Licensee shall license all individuals (or companies) who obtain data or derivative products from the Licensee the right to use the data or derivative products by way of a license agreement, and that agreement shall impose upon these individuals (or companies) the same terms and conditions as those contained in Section II of this agreement.\n6. The Licensee’s liability to indemnify SNB under this agreement shall not affect or prejudice SNB from exercising any other rights under law.\n7. SNB assumes no obligation to update the data. The data may be changed without notice to the Licensee.',
    'http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx': 'I. Terms of Use. This work is provided under the terms of “Open Data London – Terms of Use” (%s).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    # Kent Mewhort email (2012-02-10).
    'http://mli2.gov.mb.ca/app/register/app/index.php': '© 2001 Her Majesty the Queen in Right of Manitoba, as represented by the Minister of Conservation. All rights reserved. Distributed under the terms of the Manitoba Land Initiative Terms and Conditions of Use (%s).',
}

"""
The fuzzy templates for other licenses.
"""
terms_re = {
    # Creative Commons.
    'http://donnees.ville.quebec.qc.ca/licence.aspx': re.compile(r"\AI\. Terms of Use\. This material is licensed under a Creative Commons Attribution 4\.0 International License\. To view a copy of this license, visit http://creativecommons\.org/licenses/by/4\.0/legalcode\. It is attributed to .+, and the original version can be found at .+\.\Z"),
    # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
    'https://www.geosask.ca/Portal/jsp/terms_popup.jsp': re.compile(r"\AAttribution: (Source|Adapted from): Her Majesty In Right Of Saskatchewan or Information Services Corporation of Saskatchewan, [^.]+\. The incorporation of data sourced from Her Majesty In Right Of Saskatchewan and/or Information Services Corporation of Saskatchewan, within this product shall not be construed as constituting an endorsement by Her Majesty In Right Of Saskatchewan or Information Services Corporation of Saskatchewan of such product\.\Z"),
}

"""
Valid keys for a definition.py file.
"""
valid_keys = {
    # Added by boundaries.register.
    'file',
    # Used by represent-boundaries.
    'name',
    'singular',
    'domain',
    'last_updated',
    'slug_func',
    'name_func',
    'id_func',
    'is_valid_func',
    'authority',
    'source_url',
    'licence_url',
    'data_url',
    'extra',
    'notes',
    'encoding',
    # Used by tasks. Not validated.
    'prj',
    'skip_crc32',
    'basename',
}

"""
Authorities that are responsible for multiple shapefiles.
"""
authorities = [
    'Elections Prince Edward Island',
    'Regional Municipality of Peel',
    'Regional Municipality of Waterloo',
    'Ville de Montréal',
]

"""
Divisions with 'quartiers' instead of 'districts'.
"""
# @see `has_children` in `ca_municipal_subdivisions.rb` in `ocd-division-ids`
quartiers = [
    'ocd-division/country:ca/csd:2403005',  # Gaspé
    'ocd-division/country:ca/csd:2411040',  # Trois-Pistoles
    'ocd-division/country:ca/csd:2413095',  # Pohngamook
    'ocd-division/country:ca/csd:2434120',  # Lac-Sergent
    'ocd-division/country:ca/csd:2446080',  # Cowansville
    'ocd-division/country:ca/csd:2453050',  # Saint-Joseph-de-Sorel
    'ocd-division/country:ca/csd:2467025',  # Delson
    'ocd-division/country:ca/csd:2469055',  # Huntingdon
    'ocd-division/country:ca/csd:2483065',  # Maniwaki
    'ocd-division/country:ca/csd:2487090',  # La Sarre
    'ocd-division/country:ca/csd:2489040',  # Senne-Terre
    'ocd-division/country:ca/csd:2493005',  # Desbiens
    'ocd-division/country:ca/csd:2499060',  # Eeyou Istchee Baie-James
]

"""
Supplement `has_children` in `ocd-division-ids`, so that the spreadsheet task
determines a correct value for the "Shapefile?" column.
"""
municipal_subdivisions = {
    # ON
    '3501012': 'N',
    '3518013': 'N',
    '3519046': 'N',
    '3526043': 'N',
    '3531011': 'N',
    '3532042': 'N',
    '3534021': 'N',
    '3538030': 'N',
    '3548044': 'N',
    # MB
    '4602044': 'N',
    '4609029': 'N',
    '4622026': 'N',
    # YT
    '6001009': 'N',
    # NT
    '6106023': 'N',
}

default_expectation = {
    'OCD': '',
    'Geographic name': '',
    'Province or territory': '',
    'Geographic type': '',
    'Population': '',
    'URL': '',
    'Shapefile?': '',
    'Contact': '',
    'Request notes': '',
    'Received via': '',
    'Last boundary': '',
    'Next boundary': '',
    'Permission to distribute': '',
    'Response notes': '',
}
