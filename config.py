from collections import defaultdict


NOTE_TAG = 'N1'

CITED_BY_TAG = 'CB'
CITED_BY_TEXT = 'Cited By'

END_REFERENCE_TAG = 'ER'

CSV_DELIMITER = '\t'

TAG_KEY_MAPPING = defaultdict(
    lambda: 'unknown_tag',
    {
        'TY': 'type_of_reference',
        'A1': 'first_authors',
        'A2': 'secondary_authors',
        'A3': 'tertiary_authors',
        'A4': 'subsidiary_authors',
        'AB': 'abstract',
        'AD': 'author_address',
        'AN': 'accession_number',
        'AU': 'authors',
        'C1': 'custom1',
        'C2': 'custom2',
        'C3': 'custom3',
        'C4': 'custom4',
        'C5': 'custom5',
        'C6': 'custom6',
        'C7': 'custom7',
        'C8': 'custom8',
        'CA': 'caption',
        'CB': 'cited_by',
        'CN': 'call_number',
        'CY': 'place_published',
        'DA': 'date',
        'DB': 'name_of_database',
        'DO': 'doi',
        'DP': 'database_provider',
        'ET': 'edition',
        'EP': 'end_page',
        'ID': 'id',
        'IS': 'number',
        'J2': 'alternate_title1',
        'JA': 'alternate_title2',
        'JF': 'alternate_title3',
        'JO': 'journal_name',
        'KW': 'keywords',
        'L1': 'file_attachments1',
        'L2': 'file_attachments2',
        'L4': 'figure',
        'LA': 'language',
        'LB': 'label',
        'M1': 'note',
        'M3': 'type_of_work',
        'N1': 'notes',
        'N2': 'abstract',
        'NV': 'number_of_Volumes',
        'OP': 'original_publication',
        'PB': 'publisher',
        'PY': 'year',
        'RI': 'reviewed_item',
        'RN': 'research_notes',
        'RP': 'reprint_edition',
        'SE': 'version',
        'SN': 'issn',
        'SP': 'start_page',
        'ST': 'short_title',
        'T1': 'primary_title',
        'T2': 'secondary_title',
        'T3': 'tertiary_title',
        'TA': 'translated_author',
        'TI': 'title',
        'TT': 'translated_title',
        'UR': 'url',
        'VL': 'volume',
        'Y1': 'publication_year',
        'Y2': 'access_date',
        'ER': 'end_of_reference',
        'UK': 'unknown_tag',
    }
)