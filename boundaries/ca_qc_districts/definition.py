# coding: utf-8
import re
from datetime import date

import boundaries

# Noting that the "union" merge strategy fails with:
#
#     GEOS_ERROR: TopologyException: found non-noded intersection between
#     LINESTRING (...) and LINESTRING (...)
#
#     django.contrib.gis.geos.error.GEOSException: Could not initialize GEOS Geometry with given input.
#
# So, we instead use the "combine" merge strategy.

# Generated by sets.rb and then edited.
sets = {
    10043: ["Rimouski", "districts"],
    10070: ["Saint-Fabien", "districts"],
    1023: ["Les Îles-de-la-Madeleine", "districts"],
    11040: ["Trois-Pistoles", "quartiers"],
    12015: ["Saint-Antonin", "districts"],
    12072: ["Rivière-du-Loup", "districts"],
    13073: ["Témiscouata-sur-le-Lac", "districts"],
    13095: ["Pohénégamook", "quartiers"],
    15013: ["La Malbaie", "districts"],
    15035: ["Clermont", "districts"],
    15058: ["Saint-Siméon", "districts"],
    16013: ["Baie-Saint-Paul", "districts"],
    16055: ["Saint-Urbain", "districts"],
    17055: ["Saint-Aubert", "districts"],
    18050: ["Montmagny", "districts"],
    19055: ["Sainte-Claire", "districts"],
    19068: ["Saint-Henri", "districts"],
    19097: ["Saint-Charles-de-Bellechasse", "districts"],
    19105: ["Beaumont", "districts"],
    2005: ["Percé", "districts"],
    2010: ["Sainte-Thérèse-de-Gaspé", "districts"],
    2015: ["Grande-Rivière", "districts"],
    2028: ["Chandler", "districts"],
    2047: ["Port-Daniel—Gascons", "districts"],
    21010: ["Saint-Ferréol-les-Neiges", "districts"],
    21045: ["Boischatel", "districts"],
    22005: ["Sainte-Catherine-de-la-Jacques-Cartier", "districts"],
    22010: ["Fossambault-sur-le-Lac", "districts"],
    22015: ["Lac-Saint-Joseph", "districts"],
    22035: ["Stoneham-et-Tewkesbury", "districts"],
    22040: ["Lac-Beauport", "districts"],
    22045: ["Sainte-Brigitte-de-Laval", "districts"],
    23027: ["Québec", "districts"],
    23057: ["L'Ancienne-Lorette", "districts"],
    23072: ["Saint-Augustin-de-Desmaures", "districts"],
    25213: ["Lévis", "districts"],
    26030: ["Sainte-Marie", "districts"],
    26063: ["Saint-Isidore", "districts"],
    27028: ["Beauceville", "districts"],
    27043: ["Saint-Joseph-de-Beauce", "districts"],
    29073: ["Saint-Georges", "districts"],
    30010: ["Notre-Dame-des-Bois", "districts"],
    30025: ["Frontenac", "districts"],
    30030: ["Lac-Mégantic", "districts"],
    30045: ["Nantes", "districts"],
    3005: ["Gaspé", "quartiers"],
    3010: ["Cloridorme", "districts"],
    31015: ["Disraeli", "districts"],
    31056: ["Adstock", "districts"],
    31084: ["Thetford Mines", "districts"],
    31122: ["East Broughton", "districts"],
    32013: ["Saint-Ferdinand", "districts"],
    32033: ["Princeville", "districts"],
    32040: ["Plessisville", "districts"],
    32065: ["Lyster", "districts"],
    33045: ["Saint-Agapit", "districts"],
    33052: ["Saint-Flavien", "districts"],
    34030: ["Cap-Santé", "districts"],
    34038: ["Saint-Basile", "districts"],
    34120: ["Lac-Sergent", "quartiers"],
    35027: ["Saint-Tite", "districts"],
    36033: ["Shawinigan", "districts"],
    37067: ["Trois-Rivières", "districts"],
    37230: ["Saint-Maurice", "districts"],
    37235: ["Notre-Dame-du-Mont-Carmel", "districts"],
    39060: ["Saint-Christophe-d'Arthabaska", "districts"],
    39062: ["Victoriaville", "districts"],
    4037: ["Sainte-Anne-des-Monts", "districts"],
    41038: ["Cookshire-Eaton", "districts"],
    41098: ["Weedon", "districts"],
    42020: ["Saint-François-Xavier-de-Brompton", "districts"],
    42025: ["Saint-Denis-de-Brompton", "districts"],
    42032: ["Racine", "districts"],
    42098: ["Richmond", "districts"],
    42100: ["Saint-Claude", "districts"],
    42110: ["Cleveland", "districts"],
    43027: ["Sherbrooke", "districts"],
    44071: ["Compton", "districts"],
    45060: ["Sainte-Catherine-de-Hatley", "districts"],
    45072: ["Magog", "districts"],
    46050: ["Dunham", "districts"],
    46058: ["Sutton", "districts"],
    46075: ["Lac-Brome", "districts"],
    46078: ["Bromont", "districts"],
    46080: ["Cowansville", "quartiers"],
    46112: ["Farnham", "districts"],
    47017: ["Granby", "districts"],
    47025: ["Waterloo", "districts"],
    47047: ["Roxton Pond", "districts"],
    48028: ["Acton Vale", "districts"],
    49048: ["Saint-Germain-de-Grantham", "districts"],
    49058: ["Drummondville", "districts"],
    49070: ["Saint-Cyrille-de-Wendover", "districts"],
    50042: ["Saint-Léonard-d'Aston", "districts"],
    51015: ["Louiseville", "districts"],
    52007: ["Lavaltrie", "districts"],
    52017: ["Lanoraie", "districts"],
    52035: ["Berthierville", "districts"],
    52040: ["Sainte-Geneviève-de-Berthier", "districts"],
    52045: ["Saint-Ignace-de-Loyola", "districts"],
    52080: ["Saint-Gabriel", "districts"],
    52095: ["Mandeville", "districts"],
    53040: ["Saint-Roch-de-Richelieu", "districts"],
    53050: ["Saint-Joseph-de-Sorel", "quartiers"],
    53052: ["Sorel-Tracy", "districts"],
    53065: ["Sainte-Anne-de-Sorel", "districts"],
    54008: ["Saint-Pie", "districts"],
    54017: ["Saint-Damase", "districts"],
    54048: ["Saint-Hyacinthe", "districts"],
    54060: ["Saint-Dominique", "districts"],
    55008: ["Ange-Gardien", "districts"],
    55023: ["Saint-Césaire", "districts"],
    55037: ["Rougemont", "districts"],
    55048: ["Marieville", "districts"],
    55057: ["Richelieu", "districts"],
    56083: ["Saint-Jean-sur-Richelieu", "districts"],
    57005: ["Chambly", "districts"],
    57010: ["Carignan", "districts"],
    57020: ["Saint-Basile-le-Grand", "districts"],
    57025: ["McMasterville", "districts"],
    57030: ["Otterburn Park", "districts"],
    57033: ["Saint-Jean-Baptiste", "districts"],
    57035: ["Mont-Saint-Hilaire", "districts"],
    57040: ["Beloeil", "districts"],
    57045: ["Saint-Mathieu-de-Beloeil", "districts"],
    58007: ["Brossard", "districts"],
    58012: ["Saint-Lambert", "districts"],
    58033: ["Boucherville", "districts"],
    58037: ["Saint-Bruno-de-Montarville", "districts"],
    58227: ["Longueuil", "districts"],
    59010: ["Sainte-Julie", "districts"],
    59015: ["Saint-Amable", "districts"],
    59020: ["Varennes", "districts"],
    59025: ["Verchères", "districts"],
    59035: ["Contrecoeur", "districts"],
    60005: ["Charlemagne", "districts"],
    60013: ["Repentigny", "districts"],
    60028: ["L'Assomption", "districts"],
    60035: ["L'Épiphanie", "districts"],
    61025: ["Joliette", "districts"],
    61027: ["Saint-Thomas", "districts"],
    61030: ["Notre-Dame-des-Prairies", "districts"],
    61040: ["Saint-Ambroise-de-Kildare", "districts"],
    61050: ["Sainte-Mélanie", "districts"],
    62007: ["Saint-Félix-de-Valois", "districts"],
    62025: ["Saint-Alphonse-Rodriguez", "districts"],
    62037: ["Rawdon", "districts"],
    62047: ["Chertsey", "districts"],
    62060: ["Saint-Donat", "districts"],
    62075: ["Saint-Damien", "districts"],
    63030: ["Saint-Esprit", "districts"],
    63035: ["Saint-Roch-de-l'Achigan", "districts"],
    63048: ["Saint-Lin—Laurentides", "districts"],
    63055: ["Saint-Calixte", "districts"],
    63060: ["Sainte-Julienne", "districts"],
    64008: ["Terrebonne", "districts"],
    64015: ["Mascouche", "districts"],
    65005: ["Laval", "districts"],
    66007: ["Montréal-Est", "districts"],
    66023: ["Montréal", "districts"],
    66032: ["Westmount", "districts"],
    66058: ["Côte-Saint-Luc", "districts"],
    66072: ["Mont-Royal", "districts"],
    66087: ["Dorval", "districts"],
    66097: ["Pointe-Claire", "districts"],
    66102: ["Kirkland", "districts"],
    66107: ["Beaconsfield", "districts"],
    66117: ["Sainte-Anne-de-Bellevue", "districts"],
    66127: ["Senneville", "districts"],
    66142: ["Dollard-Des Ormeaux", "districts"],
    67010: ["Saint-Philippe", "districts"],
    67015: ["La Prairie", "districts"],
    67020: ["Candiac", "districts"],
    67025: ["Delson", "quartiers"],
    67030: ["Sainte-Catherine", "districts"],
    67035: ["Saint-Constant", "districts"],
    67045: ["Mercier", "districts"],
    67050: ["Châteauguay", "districts"],
    67055: ["Léry", "districts"],
    68020: ["Sainte-Clotilde", "districts"],
    68050: ["Saint-Michel", "districts"],
    68055: ["Saint-Rémi", "districts"],
    69017: ["Saint-Chrysostome", "districts"],
    69055: ["Huntingdon", "quartiers"],
    69070: ["Saint-Anicet", "districts"],
    70012: ["Sainte-Martine", "districts"],
    70022: ["Beauharnois", "districts"],
    70035: ["Saint-Louis-de-Gonzague", "districts"],
    70040: ["Saint-Stanislas-de-Kostka", "districts"],
    70052: ["Salaberry-de-Valleyfield", "districts"],
    7018: ["Causapscal", "districts"],
    7047: ["Amqui", "districts"],
    7057: ["Lac-au-Saumon", "districts"],
    71025: ["Saint-Zotique", "districts"],
    71033: ["Les Coteaux", "districts"],
    71040: ["Coteau-du-Lac", "districts"],
    71050: ["Les Cèdres", "districts"],
    71060: ["L'Île-Perrot", "districts"],
    71065: ["Notre-Dame-de-l'Île-Perrot", "districts"],
    71070: ["Pincourt", "districts"],
    71083: ["Vaudreuil-Dorion", "districts"],
    71100: ["Hudson", "districts"],
    71105: ["Saint-Lazare", "districts"],
    71133: ["Rigaud", "districts"],
    72005: ["Saint-Eustache", "districts"],
    72010: ["Deux-Montagnes", "districts"],
    72015: ["Sainte-Marthe-sur-le-Lac", "districts"],
    72020: ["Pointe-Calumet", "districts"],
    72025: ["Saint-Joseph-du-Lac", "districts"],
    72032: ["Oka", "districts"],
    72043: ["Saint-Placide", "districts"],
    73005: ["Boisbriand", "districts"],
    73010: ["Sainte-Thérèse", "districts"],
    73015: ["Blainville", "districts"],
    73035: ["Sainte-Anne-des-Plaines", "districts"],
    74005: ["Mirabel", "districts"],
    75005: ["Saint-Colomban", "districts"],
    75017: ["Saint-Jérôme", "districts"],
    75028: ["Sainte-Sophie", "districts"],
    75040: ["Prévost", "districts"],
    76008: ["Saint-André-d'Argenteuil", "districts"],
    76020: ["Lachute", "districts"],
    76043: ["Brownsburg-Chatham", "districts"],
    77022: ["Sainte-Adèle", "districts"],
    77035: ["Sainte-Anne-des-Lacs", "districts"],
    77055: ["Lac-des-Seize-Îles", "districts"],
    77060: ["Wentworth-Nord", "districts"],
    78010: ["Val-David", "districts"],
    78047: ["Saint-Faustin—Lac-Carré", "districts"],
    78055: ["Montcalm", "districts"],
    78070: ["Amherst", "districts"],
    78095: ["Lac-Supérieur", "districts"],
    78102: ["Mont-Tremblant", "districts"],
    79078: ["Lac-des-Écorces", "districts"],
    8053: ["Matane", "districts"],
    81017: ["Gatineau", "districts"],
    82005: ["L'Ange-Gardien", "districts"],
    82015: ["Val-des-Monts", "districts"],
    82020: ["Cantley", "districts"],
    82025: ["Chelsea", "districts"],
    82030: ["Pontiac", "districts"],
    82035: ["La Pêche", "districts"],
    83065: ["Maniwaki", "quartiers"],
    85045: ["Saint-Bruno-de-Guigues", "districts"],
    86042: ["Rouyn-Noranda", "districts"],
    87058: ["Macamic", "districts"],
    87090: ["La Sarre", "quartiers"],
    88022: ["Barraute", "districts"],
    89008: ["Val-d'Or", "districts"],
    89015: ["Malartic", "districts"],
    89040: ["Senneterre", "quartiers"],
    90012: ["La Tuque", "districts"],
    9077: ["Mont-Joli", "districts"],
    93005: ["Desbiens", "quartiers"],
    93012: ["Métabetchouan—Lac-à-la-Croix", "districts"],
    93020: ["Hébertville", "districts"],
    93030: ["Saint-Bruno", "districts"],
    93035: ["Saint-Gédéon", "districts"],
    93042: ["Alma", "districts"],
    93045: ["Saint-Nazaire", "districts"],
    93065: ["L'Ascension-de-Notre-Seigneur", "districts"],
    93070: ["Saint-Henri-de-Taillon", "districts"],
    94068: ["Saguenay", "districts"],
    94235: ["Saint-Fulgence", "districts"],
    94240: ["Saint-Honoré", "districts"],
    94245: ["Saint-David-de-Falardeau", "districts"],
    94255: ["Saint-Ambroise", "districts"],
    96020: ["Baie-Comeau", "districts"],
    96025: ["Pointe-Lebel", "districts"],
    96030: ["Pointe-aux-Outardes", "districts"],
    96040: ["Ragueneau", "districts"],
    97007: ["Sept-Îles", "districts"],
    99060: ["Eeyou Istchee Baie-James", "quartiers"],
}


# Check the names with (replace `CODE`):
# ogrinfo -al -geom=NO boundaries/ca_qc_districts | grep -B6 CODE | grep NM_DIS | sort
def district_namer(f):
    import boundaries
    type_id = f.get('NO_DIS')
    code = f.get('CO_MUNCP')
    name = f.get('NM_DIS')

    # Québec
    if code == 23027:
        return {
            # Hyphens.
            'Cap-Rouge-Laurentien': 'Cap-Rouge—Laurentien',
            'Chute-Montmorency-Seigneurial': 'Chute-Montmorency—Seigneurial',
            'Lac-Saint-Charles-Saint-Émile': 'Lac-Saint-Charles—Saint-Émile',
            'Montcalm-Saint-Sacrement': 'Montcalm—Saint-Sacrement',
            'Saint-Louis-Sillery': 'Saint-Louis—Sillery',
            'Saint-Roch-Saint-Sauveur': 'Saint-Roch—Saint-Sauveur',
        }.get(name, name)

    # Sherbrooke
    elif code == 43027:
        # https://cartes.ville.sherbrooke.qc.ca/monarrondissementenligne/
        return {
            1.10: 'Deauville',
            1.20: 'Rock Forest',
            1.30: 'Saint-Élie',
            1.40: 'Brompton',
            2.10: 'Hôtel-Dieu',
            2.20: 'Desranleau',
            2.30: 'Quatre-Saisons',
            2.40: 'Pin-Solitaire',
            3.10: 'Uplands',
            3.20: 'Fairview',
            4.10: 'Université',
            4.20: 'Ascot',
            4.30: 'Lac-des-Nations',
            4.40: 'Golf',
            4.50: 'Carrefour',
        }[type_id]

    # Longueuil
    elif code == 58227:
        return re.sub(r"\b(?:d'|de |du |des )", '', name)

    # Montréal
    elif code == 66023:
        return {
            'Est (Pierrefonds-Roxboro)': 'Bois-de-Liesse',
            'Ouest (Pierrefonds-Roxboro)': 'Cap-Saint-Jacques',
            'St-Henri-Petite-Bourgogne-Pte-St-Charles': 'Saint-Henri—Petite-Bourgogne—Pointe-Saint-Charles',
            'Étienne-Desmarteaux': 'Étienne-Desmarteau',
            # Articles.
            "d'Ahuntsic": 'Ahuntsic',
            'de Bordeaux-Cartierville': 'Bordeaux-Cartierville',
            'de Saint-Sulpice': 'Saint-Sulpice',
            'du Sault-au-Récollet': 'Sault-au-Récollet',
            # Hyphens.
            "Champlain-L'Île-des-Soeurs": "Champlain—L'Île-des-Soeurs",
            'Maisonneuve-Longue-Pointe': 'Maisonneuve—Longue-Pointe',
            'Saint-Paul-Émard': 'Saint-Paul—Émard',
        }.get(name, name)

    # Pointe-Claire
    elif code == 66097:
            # Check if required with:
            # ogrinfo -al -geom=NO boundaries/ca_qc_districts | grep '/ '
        return name.replace('/ ', '/')

    # Gatineau
    elif code == 81017:
        return {
            # Hyphens.
            'de Hull-Val-Tétreau': 'de Hull—Val-Tétreau',
            'de Saint-Raymond-Vanier': 'de Saint-Raymond—Vanier',
            'de Wright-Parc-de-la-Montagne': 'de Wright—Parc-de-la-Montagne',
            'du Plateau-Manoir-des-Trembles': 'du Plateau—Manoir-des-Trembles',
        }.get(name, name)

    else:
        if name:
            # Check if required with:
            # ogrinfo -al -geom=NO boundaries/ca_qc_districts | grep ' no '
            if 'District no ' in name:
                return f.get('NM_DIS').replace(' no ', ' ')  # Baie-Saint-Paul
            else:
                return boundaries.clean_attr('NM_DIS')(f)
        elif f.get('MODE_SUFRG') == 'Q':
            return 'Quartier %s' % int(type_id)
        else:
            return 'District %s' % int(type_id)


def borough_namer(f):
    import boundaries
    code = f.get('CO_MUNCP')
    name = f.get('NM_ARON')

    # Sherbrooke
    if code == 43027:
        return 'Arrondissement %s' % int(f.get('NO_ARON'))

    # Montréal
    elif code == 66023:
        return {
            'Le Plateau-Mont-Royal': 'Plateau-Mont-Royal',
            'Le Sud-Ouest': 'Sud-Ouest',
            'Pierrefond-Roxboro': 'Pierrefonds-Roxboro',
            'Rosemont--La-Petite-Patrie': 'Rosemont—La Petite-Patrie',
        }.get(name, boundaries.clean_attr('NM_ARON')(f))

    else:
        return boundaries.clean_attr('NM_ARON')(f)


# Check if required with:
# ogrinfo -al -geom=NO boundaries/ca_qc_districts | grep -A9 ' 1\.10'
def district_ider(f):
    if f.get('CO_MUNCP') in (43027, 66023):  # Sherbrooke, Montréal
        return f.get('NO_DIS')  # e.g. "1.10"
    else:
        return int(f.get('NO_DIS'))


for geographic_code, (name, type) in sets.items():
    geographic_codes = [geographic_code]

    boundaries.register('%s %s' % (name, type),
        domain='%s, QC' % name,
        last_updated=date(2017, 11, 30),
        name_func=district_namer,
        id_func=district_ider,
        authority='Directeur général des élections du Québec',
        licence_url='https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='utf-8',
        extra={'division_id': 'ocd-division/country:ca/csd:24%05d' % geographic_code},
        is_valid_func=lambda f, geographic_codes=geographic_codes: int(f.get('CO_MUNCP')) in geographic_codes,
        notes='Load the shapefile manually:\nfab alpheus update_boundaries:args="-r --merge combine -d data/shapefiles/public/boundaries/ca_qc_districts"',
    )

boundaries.register('Paroisse de Plessisville districts',
    domain='Plessisville, QC',
    last_updated=date(2017, 11, 30),
    name_func=district_namer,
    id_func=district_ider,
    authority='Directeur général des élections du Québec',
    licence_url='https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:2432045'},
    is_valid_func=lambda f: int(f.get('CO_MUNCP')) == 32045,
)

# Check the names with (replace `CODE`):
# ogrinfo -al -geom=NO boundaries/ca_qc_districts | grep -B3 CODE | sort | uniq
# Check the identifiers with:
# ogrinfo -al -geom=NO boundaries/ca_qc_districts | grep -B4 CODE
municipalities_with_boroughs = [
    {
        'name': 'Lévis',
        'geographic_code': 25213,
        'boroughs': {
            'ocd-division/country:ca/csd:2425213/borough:1': 'Desjardins',
            'ocd-division/country:ca/csd:2425213/borough:2': 'Les Chutes-de-la-Chaudière-Est',
            'ocd-division/country:ca/csd:2425213/borough:3': 'Les Chutes-de-la-Chaudière-Ouest',
        },
    },
    {
        'name': 'Longueuil',
        'geographic_code': 58227,
        'boroughs': {
            'ocd-division/country:ca/csd:2458227/borough:1': 'Le Vieux-Longueuil',
            'ocd-division/country:ca/csd:2458227/borough:2': 'Greenfield Park',
            'ocd-division/country:ca/csd:2458227/borough:3': 'Saint-Hubert',
        },
    },
    {
        'name': 'Montréal',
        'geographic_code': 66023,
        'boroughs': {
            'ocd-division/country:ca/csd:2466023/borough:1': "Ahuntsic-Cartierville",
            'ocd-division/country:ca/csd:2466023/borough:2': "Anjou",
            'ocd-division/country:ca/csd:2466023/borough:3': "Côte-des-Neiges—Notre-Dame-de-Grâce",
            'ocd-division/country:ca/csd:2466023/borough:4': "Lachine",
            'ocd-division/country:ca/csd:2466023/borough:5': "LaSalle",
            'ocd-division/country:ca/csd:2466023/borough:6': "L'Île-Bizard—Sainte-Geneviève",
            'ocd-division/country:ca/csd:2466023/borough:7': "Mercier—Hochelaga-Maisonneuve",
            'ocd-division/country:ca/csd:2466023/borough:8': "Montréal-Nord",
            'ocd-division/country:ca/csd:2466023/borough:9': "Outremont",
            'ocd-division/country:ca/csd:2466023/borough:10': "Pierrefonds-Roxboro",
            'ocd-division/country:ca/csd:2466023/borough:11': "Plateau-Mont-Royal",
            'ocd-division/country:ca/csd:2466023/borough:12': "Rivière-des-Prairies—Pointe-aux-Trembles",
            'ocd-division/country:ca/csd:2466023/borough:13': "Rosemont—La Petite-Patrie",
            'ocd-division/country:ca/csd:2466023/borough:14': "Saint-Laurent",
            'ocd-division/country:ca/csd:2466023/borough:15': "Saint-Léonard",
            'ocd-division/country:ca/csd:2466023/borough:16': "Sud-Ouest",
            'ocd-division/country:ca/csd:2466023/borough:17': "Verdun",
            'ocd-division/country:ca/csd:2466023/borough:18': "Ville-Marie",
            'ocd-division/country:ca/csd:2466023/borough:19': "Villeray—Saint-Michel—Parc-Extension",
        },
    },
    {
        'name': 'Québec',
        'geographic_code': 23027,
        'boroughs': {
            'ocd-division/country:ca/csd:2423027/borough:1': 'La Cité-Limoilou',
            'ocd-division/country:ca/csd:2423027/borough:2': 'Les Rivières',
            'ocd-division/country:ca/csd:2423027/borough:3': 'Sainte-Foy—Sillery—Cap-Rouge',
            'ocd-division/country:ca/csd:2423027/borough:4': 'Charlesbourg',
            'ocd-division/country:ca/csd:2423027/borough:5': 'Beauport',
            'ocd-division/country:ca/csd:2423027/borough:6': 'La Haute-Saint-Charles',
        },
    },
    {
        'name': 'Saguenay',
        'geographic_code': 94068,
        'boroughs': {
            'ocd-division/country:ca/csd:2494068/borough:1': 'Chicoutimi',
            'ocd-division/country:ca/csd:2494068/borough:2': 'Jonquière',
            'ocd-division/country:ca/csd:2494068/borough:3': 'La Baie',
        },
    },
    {
        'name': 'Sherbrooke',
        'geographic_code': 43027,
        'boroughs': {
            'ocd-division/country:ca/csd:2443027/borough:1': 'Arrondissement 1',
            'ocd-division/country:ca/csd:2443027/borough:2': 'Arrondissement 2',
            'ocd-division/country:ca/csd:2443027/borough:3': 'Arrondissement 3',
            'ocd-division/country:ca/csd:2443027/borough:4': 'Arrondissement 4',
        },
    },
]

# @see http://www.toponymie.gouv.qc.ca/ct/toponymie-municipale/municipalites-arrondissements/arrondissement.aspx
# @see http://www.mamrot.gouv.qc.ca/repertoire-des-municipalites/fiche/arrondissement/?tx_mamrotrepertoire_pi1[order]=asc_nom_mun
for municipality in municipalities_with_boroughs:
    geographic_code = municipality['geographic_code']
    geographic_name = municipality['name']

    for division_id, name in municipality['boroughs'].items():
        subdivision_id = int(division_id.rsplit(':', 1)[-1])

        boundaries.register('%s districts' % name,
            domain='%s, %s, QC' % (name, geographic_name),
            last_updated=date(2017, 11, 30),
            name_func=district_namer,
            id_func=district_ider,
            authority='Directeur général des élections du Québec',
            licence_url='https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
            encoding='utf-8',
            extra={'division_id': division_id},
            is_valid_func=lambda f, geographic_code=geographic_code, subdivision_id=subdivision_id: int(f.get('CO_MUNCP')) == geographic_code and int(f.get('NO_ARON')) == subdivision_id,
            notes='Load the shapefile manually:\nfab alpheus update_boundaries:args="-r --merge combine -d data/shapefiles/public/boundaries/ca_qc_districts"',
        )

    boundaries.register('%s boroughs' % geographic_name,
        domain='%s, QC' % geographic_name,
        last_updated=date(2017, 11, 30),
        name_func=borough_namer,
        id_func=lambda f: int(f.get('NO_ARON')),
        authority='Directeur général des élections du Québec',
        licence_url='https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='utf-8',
        extra={'division_id': 'ocd-division/country:ca/csd:24%05d' % geographic_code},
        is_valid_func=lambda f, geographic_code=geographic_code: int(f.get('CO_MUNCP')) == geographic_code,
        notes='Load the shapefile manually:\nfab alpheus update_boundaries:args="-r --merge combine -d data/shapefiles/public/boundaries/ca_qc_districts"',
    )
