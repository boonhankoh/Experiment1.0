from otree.api import *






class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    app_to_pay = models.StringField
    charity_to_pay = models.StringField

# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        import random
        participant = player.participant
        apps = ['stage1_final', 'stage2_2test', 'stage3']
        app_to_pay = random.choice(apps)
        participant.payoff = participant.app_payoffs[app_to_pay]
        player.app_to_pay = app_to_pay

        charity = ['stage2_2test', 'stage3']
        charity_to_pay = random.choice(charity)
        player.charity_to_pay = charity_to_pay



page_sequence = [PaymentInfo]
