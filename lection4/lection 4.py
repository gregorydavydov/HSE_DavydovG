from datetime import datetime

# ДЗ 7

class CourtCase:
    def __init__(self, case_number, case_participants, listening_datetimes, in_finished, verdict):
        self.case_number = case_number
        self.case_participants = case_participants
        self.listening_datetimes = listening_datetimes
        self.in_finished = in_finished
        self.verdict = verdict

    def set_a_listening_datetime(self): # Добавляет в список "listening_datetimes" судебное заседание


    def add_participant(self): # Добавляет в список "case_participants" ИНН участника


    def remove_participant(self): # Удаляет из список "case_participants" ИНН участника


    def make_a_decision(self): # Вынести решение по делу, добавить verdict и сменить атрибут "is_finished" на true







