import csv

file_in = "Corp_Summary.csv"
file_out = 'hw2.csv'


def choice(file1: str, file2: str) -> dict:
    """Функция выбора команды"""
    inquiry = input()
    if inquiry == '1':
        return get_hierarchy(file1)
    elif inquiry == '2':
        return get_summary(file1)
    else:
        return write_summary(file1, file2)


def get_hierarchy(file: str) -> dict:
    """Функция выводит иерархию команд (департаменты и их команды)"""
    with open(file, newline='') as csvfile:
        f_read = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(f_read)
        ans = dict()
        for row in f_read:
            if row[2] not in ans.get(row[1], list()):
                ans.setdefault(row[1], list()).append(row[2])

    print('{:<13} {}'.format('Департамент', 'Команды'))
    for key, value in ans.items():
        print('{:<13} {}'.format(key, ', '.join(value)))
    return ans


def get_summary(file: str) -> dict:
    """Функция выводит сводный отчёт по департаментам: название, численность,
    "вилка" зарплат в виде мин – макс, среднюю зарплату"""
    with open(file, newline='') as csvfile:
        f_read = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(f_read)
        ans = dict()
        for row in f_read:
            sal = int(row[-1])
            ans.setdefault(row[1], [0, 1000000, 0, 0])[0] += 1
            if sal < ans.setdefault(row[1], [0, 1000000, 0, 0])[1]:
                ans.setdefault(row[1], [0, 1000000, 0, 0])[1] = sal
            else:
                if sal > ans.setdefault(row[1], [0, 1000000, 0, 0])[2]:
                    ans.setdefault(row[1], [0, 1000000, 0, 0])[2] = sal
            ans.setdefault(row[1], [0, 1000000, 0, 0])[-1] += sal
    print('{:<13} {:>12} {:>18}   {}'.format(
        'Департамент', 'Численность', 'Зарплатная вилка', 'Средняя зарплата'
        ))
    for key, value in ans.items():
        print('{:<13} {:>12} {:>9} - {}  {:>17}'.format(
            key, value[0], value[1], value[2], round(value[-1]/value[0], 2)
            ))
    return ans


def write_summary(file1: str, file2: str) -> dict:
    """Функция записывает в csv файл  сводный отчёт по департаментам: название,
    численность, "вилка" зарплат в виде мин – макс, среднюю зарплату"""
    with open(file1, newline='') as csvfile:
        f_read = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(f_read)
        ans = dict()
        for row in f_read:
            sal = int(row[-1])
            ans.setdefault(row[1], [0, 1000000, 0, 0])[0] += 1
            if sal < ans.setdefault(row[1], [0, 1000000, 0, 0])[1]:
                ans.setdefault(row[1], [0, 1000000, 0, 0])[1] = sal
            else:
                if sal > ans.setdefault(row[1], [0, 1000000, 0, 0])[2]:
                    ans.setdefault(row[1], [0, 1000000, 0, 0])[2] = sal
            ans.setdefault(row[1], [0, 1000000, 0, 0])[-1] += sal
    with open(file2, 'w') as csvfile:
        fieldnames = [
            'Департамент', 'Численность', 'Зарплатная вилка',
            'Средняя зарплата'
            ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in ans.items():
            writer.writerow({
                'Департамент': key,
                'Численность': value[0],
                'Зарплатная вилка': '-'.join(map(str, value[1:2])),
                'Средняя зарплата': round(value[-1]/value[0], 2)
                })
    print("Writing complete")
    return ans


if __name__ == '__main__':
    choice(file_in, file_out)
