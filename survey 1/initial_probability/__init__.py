from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'initial_probability'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_probability_1_1 = models.FloatField(min=0, max=100, label='')
    final_probability_1_2 = models.FloatField(min=0, max=100, label='')
    final_probability_1_3 = models.FloatField(min=0, max=100, label='')
    final_probability_2_1 = models.FloatField(min=0, max=100, label='')
    final_probability_2_2 = models.FloatField(min=0, max=100, label='')
    final_probability_2_3 = models.FloatField(min=0, max=100, label='')
    final_probability_3_1 = models.FloatField(min=0, max=100, label='')
    final_probability_3_2 = models.FloatField(min=0, max=100, label='')
    final_probability_3_3 = models.FloatField(min=0, max=100, label='')
    final_probability_4_1 = models.FloatField(min=0, max=100, label='')
    final_probability_4_2 = models.FloatField(min=0, max=100, label='')
    final_probability_4_3 = models.FloatField(min=0, max=100, label='')
    final_probability_5_1 = models.FloatField(min=0, max=100, label='')
    final_probability_5_2 = models.FloatField(min=0, max=100, label='')
    final_probability_5_3 = models.FloatField(min=0, max=100, label='')
    final_probability_6_1 = models.FloatField(min=0, max=100, label='')
    final_probability_6_2 = models.FloatField(min=0, max=100, label='')
    final_probability_6_3 = models.FloatField(min=0, max=100, label='')
    final_probability_7_1 = models.FloatField(min=0, max=100, label='')
    final_probability_7_2 = models.FloatField(min=0, max=100, label='')
    final_probability_7_3 = models.FloatField(min=0, max=100, label='')
    final_probability_8_1 = models.FloatField(min=0, max=100, label='')
    final_probability_8_2 = models.FloatField(min=0, max=100, label='')
    final_probability_8_3 = models.FloatField(min=0, max=100, label='')


# PAGES
class InitialProbability1(Page):
    form_model = 'player'
    form_fields = ['final_probability_1_1', 'final_probability_1_2', 'final_probability_1_3']


class InitialProbability2(Page):
    form_model = 'player'
    form_fields = ['final_probability_2_1', 'final_probability_2_2', 'final_probability_2_3']


class InitialProbability3(Page):
    form_model = 'player'
    form_fields = ['final_probability_3_1', 'final_probability_3_2', 'final_probability_3_3']


class InitialProbability4(Page):
    form_model = 'player'
    form_fields = ['final_probability_4_1', 'final_probability_4_2', 'final_probability_4_3']


class InitialProbability5(Page):
    form_model = 'player'
    form_fields = ['final_probability_5_1', 'final_probability_5_2', 'final_probability_5_3']


class InitialProbability6(Page):
    form_model = 'player'
    form_fields = ['final_probability_6_1', 'final_probability_6_2', 'final_probability_6_3']


class InitialProbability7(Page):
    form_model = 'player'
    form_fields = ['final_probability_7_1', 'final_probability_7_2', 'final_probability_7_3']


class InitialProbability8(Page):
    form_model = 'player'
    form_fields = ['final_probability_8_1', 'final_probability_8_2', 'final_probability_8_3']


class Results(Page):
    pass


page_sequence = [InitialProbability1, InitialProbability2, InitialProbability3,
                 InitialProbability4, InitialProbability5, InitialProbability6,
                 InitialProbability7, InitialProbability8]
