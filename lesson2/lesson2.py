from lesson_2_data import courts, repondents

# ДЗ 3

#Task_one

def factorial(n: int) -> int:# аннотации типа возвращаемого значения функции, в этом случае принимает аргумент типа int и возвращает значение типа int
    result = 1  # переменная result со значением 1 вводится перед началом вычисления факториала, Это нужно, так как произведение чисел, начинающееся с 1
    for i in range(1,n + 1):  # используется для создания цикла, который перебирает значения от 1 до n включительно,  n обозначает некоторое целое число, до которого нужно выполнить цикл
        result *= i  # переменная result умножается на значение переменной i
    return result

print(factorial(int(input("Введите число:"))))

def max_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)
a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
c = int(input("Введите значение c:"))

print(max_of_three(a, b, c))

def area_of_right_triangle(a: float, b: float) -> float:
    return (float(1 / 2) * a * b)
a = float(input("Введите значение катета a:"))
b = float(input("Введите значение катета b:"))

print(area_of_right_triangle(a, b))



#Task two
def main():
    for repondent in repondents:
        if 'case_number' in repondent:
            case_number = repondent['case_number']
            court_code = case_number.split('-')[0]
            found_court = False
            for court in courts:
                if court_code == court['court_code']:
                    repondent['court_code'] = court['court_name']
                    found_court = True
                    break
            if not found_court:
                repondent['court_code'] = 'Неизвестный суд'
            name = repondent['short_name']
            inn = repondent['inn']
            ogrn = repondent['ogrn']
            address = repondent['address']
            case_number = repondent['case_number']
            print(f"Название суда: {repondent['court_code']}")
            print("Истец: Иванов Иван Иванович""\n""ИНН: 1236182357", "ОГРНИП: 218431927812733""\n""Адрес: 123534, г. Москва, ул. Водников, 13""\n\n"f"Ответчик: {name}""\n"f"ИНН: {inn}, ОГРН: {ogrn}""\n"f"Адрес: {address}""\n"f"Номер дела: {case_number}""\n\n")


if __name__ == "__main__":
    main()
    print("stop")
