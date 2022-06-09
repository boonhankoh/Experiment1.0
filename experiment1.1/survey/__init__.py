from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        label='What is your gender?',
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
            [4, 'Prefer not to say']
        ],
        widget=widgets.RadioSelect,
    )
    ethnicity = models.IntegerField(
        choices=[
        [1, 'White'],
        [2, 'Asian or Asian British'],
        [3, 'Black, Black British,Caribbean or African'],
        [4, 'Mixed or multiple ethnic groups'],
        [5, 'Other'],
        [6, 'Prefer no to say']
        ],
        label='Which is your ethinic group?',
        widget=widgets.RadioSelect,
    )
    employment_status = models.IntegerField(
        label='Please select your current employment status.',
        choices=[
            [1, 'Employed (full-time)'],
            [2, 'Employed (part-time)'],
            [3, 'Unpaid work'],
            [4, 'Unemployed']
        ],
        widget=widgets.RadioSelect,
    )
    strength_ciswo = models.IntegerField(
        choices=[
            [0, 'Strongly disagree'],
            [1, 'Weakly disagree'],
            [2, 'Neither agree nor disagree'],
            [3, 'Weakly agree'],
            [4, 'Strongly agree']
        ],
        widget=widgets.RadioSelectHorizontal,
        label= ''
    )
    strength_ember = models.IntegerField(
        choices=[
            [0, 'Strongly disagree'],
            [1, 'Weakly disagree'],
            [2, 'Neither agree nor disagree'],
            [3, 'Weakly agree'],
            [4, 'Strongly agree']
        ],
        widget=widgets.RadioSelectHorizontal,
        label=''
    )
    strength_care = models.IntegerField(
        choices=[
            [0, 'Strongly disagree'],
            [1, 'Weakly disagree'],
            [2, 'Neither agree nor disagree'],
            [3, 'Weakly agree'],
            [4, 'Strongly agree']
        ],
        widget=widgets.RadioSelectHorizontal,
        label=''
    )
    strength_bpas = models.IntegerField(
        choices=[
            [0, 'Strongly disagree'],
            [1, 'Weakly disagree'],
            [2, 'Neither agree nor disagree'],
            [3, 'Weakly agree'],
            [4, 'Strongly agree']
        ],
        widget=widgets.RadioSelectHorizontal,
        label=''
    )



# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'ethnicity', 'employment_status']


class Mission_strength(Page):
    form_model = 'player'
    form_fields = ['strength_ciswo', 'strength_ember', 'strength_care', 'strength_bpas']



page_sequence = [Mission_strength, Demographics]
