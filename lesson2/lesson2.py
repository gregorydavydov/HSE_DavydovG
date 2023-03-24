from lesson_2_data import courts, repondents
"""
enumarate - нумерация выводимых данных
range () – это служебная функция для создания списка чисел. Список сгенерированных чисел полезен для логики итераций. 
"""
def main():
    count = 0
    for i, repondent in enumerate(repondents):
        print(i, repondent["inn"])

if __name__ == "__main__":
    main()
    print("stop")
