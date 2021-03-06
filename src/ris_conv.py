import re
from csv import DictWriter

from config import *
from string_builder import StringBuilder


class RISConv:

    def __init__(self, file_path: str) -> None:
        self._entries = []
        self._tags_in_file = {}
        self._file_path = file_path

    def ris_to_dict(self) -> list:
        if not self._entries:
            with open(self._file_path, encoding=ENCONDING) as ris_file:
                new_entry_flag = True

                for line in ris_file:
                    line = line.strip()
                    if not line:
                        continue

                    if new_entry_flag:
                        self._entries.append({})
                        new_entry_flag = False

                    search = re.search('(\w{2})  - ?(.*)', line)
                    if search is None:
                        current_entry[name_tag].add(line)
                        continue

                    tag_start_pos = search.start()
                    if tag_start_pos != 0:
                        current_entry[name_tag].add(line[:tag_start_pos])

                    current_tag, tag_value = search.groups()
                    name_tag = TAG_KEY_MAPPING[current_tag]

                    if current_tag == END_REFERENCE_TAG:
                        new_entry_flag = True
                        continue

                    current_entry = self._entries[-1]

                    if current_tag == TYPE_TAG:
                        current_entry[name_tag] = TYPE_REFERENCE_MAPPING[tag_value]

                    elif current_tag == NOTE_TAG and tag_value.startswith(CITED_BY_TEXT):
                        name_tag = TAG_KEY_MAPPING[CITED_BY_TAG]
                        current_entry[name_tag] = re.search(':(\\d+)', tag_value).group(1)

                    elif name_tag not in current_entry:
                        current_entry[name_tag] = StringBuilder(tag_value)

                    else:
                        current_entry[name_tag].add(f'{SUB_DELIMITER}{tag_value}')

                    self._tags_in_file[name_tag] = True

        return self._entries

    def ris_to_csv(self, file_path: str) -> None:
        entries = self.ris_to_dict()
        with open(file_path, 'w', encoding=ENCONDING, newline='') as file:
            writer = DictWriter(file, self._tags_in_file, delimiter=CSV_DELIMITER)
            writer.writeheader()
            writer.writerows(entries)
