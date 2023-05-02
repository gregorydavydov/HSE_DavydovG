
# ДЗ 7

class CourtCase:
    def __init__(self, case_number, case_participants, listening_datetimes, in_finished, verdict):
        self.case_number = case_number
        self.case_participants = case_participants
        self.listening_datetimes = listening_datetimes
        self.in_finished = in_finished
        self.verdict = verdict

    def set_a_listening_datetime(self, new_time):  # Добавляет в список "listening_datetimes" судебное заседание
        self.listening_datetimes = []
        if new_time not in self.listening_datetimes:
            self.listening_datetimes.append(new_time)

    def add_participant(self, inn):  # Добавляет в списка "case_participants" ИНН участника
        self.case_participants = []
        if inn not in self.case_participants:
            self.case_participants.append(inn)

    def remove_participant(self, inn):  # Удаляет из списка "case_participants" ИНН участника
        if inn in self.case_participants:
            self.case_participants.remove(inn)

    def make_a_decision(self,
                        decide):  # Вынести решение по делу, добавить verdict и сменить атрибут "is_finished" на true
        self.in_finished = False
        verdict = ''
        if decide != self.in_finished:
            self.verdict = 'Решение вступило в силу'
        else:
            self.verdict = 'Решение не вступило в силу'


a = CourtCase(case_number='А40-183194/2015', case_participants=[], listening_datetimes=[], in_finished=False, verdict='')
a.case_number
a.set_a_listening_datetime('01-05-2023')
a.listening_datetimes
a.add_participant('862202483517')
a.add_participant('862202483518')
a.remove_participant('862202483518')
a.case_participants
a.make_a_decision(False)
a.verdict




#ДЗ 8

class DistanceSell:
  def __init__(self, list_products, period_refuse):
    self.list_products = list_products
    self.period_refuse = period_refuse
  def type_products(self, type):
    self.list_products = ['medicine','cosmetic','textile','domestic chemicals','furniture','technically complex', 'non-periodic publications', 'animals']
    if type not in self.list_products:
      print('Товар подлежит обмену или возврату')
    else:
      print('Товар не подлежит обмену или возврату')
  def refuse_product(self, period_receipt):
    self.period_refuse < 7
    if period_receipt <= self.period_refuse:
      print('Срок возврата не пропущен')
    else:
      print('Пропущен срок возврата')

a = DistanceSell(list_products=[], period_refuse=7)
a.type_products('shoes')
a.refuse_product(3)



