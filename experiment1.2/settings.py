import itertools
from os import environ



SESSION_CONFIGS = (
    dict(
        name='Experiment_V1', app_sequence=['welcome', 'stage1_final', 'mission_pe', 'stage2_2test', 'stage3', 'survey',
                                         'payment_info'],
        num_demo_participants=6
    ),
    dict(
        name='slider',
        app_sequence=['stage2_2test'],
    num_demo_participants=1
    ),
)

#FUNCTIONS


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'CISWO',
    'Ember',
    'CARE',
    'BPAS',
    'treatment',
    'penalty',
    'charity_order',
    'is_dropout',
    'app_payoffs',
    'charity_donations',
    's1_num_correct',
]
SESSION_FIELDS = ['params']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
"""


SECRET_KEY = '2307692050879'

INSTALLED_APPS = ['otree''slider_task']
