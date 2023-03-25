from collections import defaultdict
import csv
import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent

RESULTS_DIR = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TITLE_NAMES = ['Статус', 'Количество']
PREFIX_NAME = 'status_summary_{}.csv'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)
        self.status_counts = defaultdict(int)

    def open_spider(self, spider):
        time = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_path = self.results_dir / PREFIX_NAME.format(time)
        self.output_file = csv.writer(
            open(file_path, 'w')
        )
        self.output_file.writerow(TITLE_NAMES)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        print(self.status_counts)
        self.status_counts['Total'] = sum(self.status_counts.values())
        self.output_file.writerows(self.status_counts.items())
