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
            new_entry_flag = True
            with open(self._file_path, encoding='utf-8') as ris_file:

                for line in ris_file:
                    line = line.strip()
                    if not line:
                        continue
                    elif new_entry_flag:
                        self._entries.append({})
                        new_entry_flag = False

                    current_tag, tag_value = re.search('(.*)  - ?(.*)', line).groups()
                    name_tag = TAG_KEY_MAPPING[current_tag]

                    if current_tag == END_REFERENCE_TAG:
                        new_entry_flag = True
                        continue

                    current_entry = self._entries[-1]
                    if current_tag == NOTE_TAG and CITED_BY_TEXT in tag_value:
                        name_tag = TAG_KEY_MAPPING[CITED_BY_TAG]
                        current_entry[name_tag] = re.search(':(\\d+)', tag_value).group(1)
                    elif name_tag not in current_entry:
                        current_entry[name_tag] = StringBuilder(tag_value)
                    elif current_entry[name_tag]:
                        current_entry[name_tag].add(f' | {tag_value}')
                    self._tags_in_file[name_tag] = True

        return self._entries

    def ris_to_csv(self, file_path: str) -> None:
        entries = self.ris_to_dict()
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = DictWriter(file, self._tags_in_file, delimiter=CSV_DELIMITER)
            writer.writeheader()
            writer.writerows(entries)
