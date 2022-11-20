print('------Задание 1------')


# Задание 1
def change_lst(list_def=[]):
    first_element = list_def[0]
    list_def[0] = list_def[int(len(list_def) - 1)]
    list_def[int(len(list_def) - 1):int(len(list_def))] = [first_element]

    return list_def


print(change_lst([56, 'rtt', 1, 4, 5, 6, 7, 78, '79', 89, 'try']))

print('------Задание 2------')


# Задание 2
def to_dict(list_def_2=[]):
    print(dict((k, k) for k in list_def_2))


print(to_dict([56, 1, 3, 4, 2, 'ewer']))

print('------Задание 3------')


# Задание 3
def sum_range(start, end):
    start_curretnt = start
    if start > end:
        end = start_curretnt
    summa = 0
    for x in range(end + 1):
        summa += x

    return summa


print(sum_range(3, 1))

print('------Задание 4------')


# Задание 4
def read_last(lines, file):
    if isinstance(lines, int) and lines > 0:
        file_1 = open(file, 'r')
        lines_read = file_1.read().splitlines()
        lines_read_1 = lines_read[::-1]
        lines_read_2 = lines_read_1[0:lines]
        lines_read_3 = lines_read_2[::-1]
        print(lines_read_3)
        file_1.close()
    else:
        print('Число не целое или отрицательное')


read_last(3, 'task_4.txt')
