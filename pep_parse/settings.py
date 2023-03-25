BOT_NAME = 'pep_parse'

SPIDER_NAME = 'pep_parse.spiders'

SPIDER_MODULES = [SPIDER_NAME]
NEWSPIDER_MODULE = SPIDER_NAME
RESULTS_DIR = 'results'

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
