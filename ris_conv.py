import re
from csv import DictWriter

from config import TAG_KEY_MAPPING


class RISConv:

    def __init__(self, file_path: str) -> None:
        self.data = []
        self.tags_in_file = {}
        self.file_path = file_path

    def ris_to_dict(self) -> list:
        if not self.data:
            with open(self.file_path, encoding='utf-8') as file:
                entries = [{}]
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    key = re.search('..', line).group()
                    name_key = TAG_KEY_MAPPING[key]

                    if key == 'ER':
                        entries.append({})
                        continue

                    entry = entries[-1]
                    value = re.search('- (.*)', line).group(1)
                    if key == 'N1' and 'Cited By' in value:
                        name_key = TAG_KEY_MAPPING['CB']
                        entry[name_key] = int(re.search(':(\\d+)', line).group(1))
                    elif name_key not in entry:
                        entry[name_key] = value
                    elif entry[name_key]:
                        entry[name_key] += f' | {value}'
                    self.tags_in_file[name_key] = None

                self.data = entries[:-1]

                for dic in self.data:
                    normalized_dict = self.tags_in_file.copy()
                    normalized_dict.update(dic)

        return self.data

    def ris_to_csv(self, file_path: str) -> None:
        rows = self.ris_to_dict()
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = DictWriter(file, self.tags_in_file, delimiter='\t')
            writer.writeheader()
            writer.writerows(rows)
