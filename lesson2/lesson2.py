from lesson_2_data import courts, repondents
"""
enumarate - нумерация выводимых данных
range () – это служебная функция для создания списка чисел. Список сгенерированных чисел полезен для логики итераций. 
"""


#Task two
def main():
    for repondent in repondents:
        if 'case_number' in repondent:
            case_number = repondent['case_number']
            court_code = case_number.split('-')[0]
            if court_code in courts:
                repondent['court_name'] = courts['court_code']and['court_name']
            else:
                repondent['court_name'] = 'Неизвестный суд'
            name = repondent['short_name']
            inn = repondent['inn']
            ogrn = repondent['ogrn']
            address = repondent['address']
            case_number = repondent['case_number']
            print(f"Код: {court_code}")
            print("Истец: Иванов Иван Иванович""\n""ИНН: 1236182357", "ОГРНИП: 218431927812733""\n""Адрес: 123534, г. Москва, ул. Водников, 13""\n\n"f"Ответчик: {name}""\n"f"ИНН: {inn}, ОГРН: {ogrn}""\n"f"Адрес: {address}""\n"f"Номер дела: {case_number}""\n\n")








if __name__ == "__main__":
    main()
    print("stop")
