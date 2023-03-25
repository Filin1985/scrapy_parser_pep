import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

from .settings import RESULTS_DIR


BASE_DIR = Path(__file__).parent


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TITLE_NAMES = ['Статус', 'Количество']
TOTAL_NAME = 'Total'
PREFIX_NAME = 'status_summary_{}.csv'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_path = self.results_dir / PREFIX_NAME.format(time)
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(f, dialect='unix').writerows([
                ('Статус', 'Количество'),
                *self.status_counts.items(),
                ('Total', sum(self.status_counts.values())),
            ])
