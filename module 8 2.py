

def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы -{num}')

    return result,incorrect_data


def calculate_average(numbers):
    #if isinstance(numbers,int):
        #return None
    try:
        average = personal_sum(numbers)
        return average[0] / (len(numbers) - average[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')



print(f'Результат 1: {calculate_average("1,2,3")}')
print(f'Результат 2: {calculate_average([1,"Строка",3,'Ещё Строка'])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42,15,36,13])}')












