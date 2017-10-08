import csv

list1 = []
list2 = []
list3 = []

def file_one(filename):
    with open(UPLOAD_FOLDER + str(filename), 'r', newline="") as file:
        line = csv.reader(file, delimiter=';', quotechar='|')
        for row in line:
            list1.append(row)


def file_two(filename):
    with open(UPLOAD_FOLDER + str(filename), 'r', newline="") as file:
        line = csv.reader(file, delimiter=';', quotechar='|')
        for row in line:
            list2.append(row)

def compare_list():
    f1 = int(input('Введите номер колонки первого файла для сравнения: '))
    f2 = int(input('Введите номер колонки второго файла для сравнения: '))
    f3 = int(input('Номер колонки куда перезаписываем: '))
    f4 = int(input('Номер колонки откуда перезаписываем: '))
    if len(list1) > len(list2):
        max_len = len(list1)
    else:
        max_len = len(list2)
    print(len(list1))
    print(len(list2))
    for i in range(len(list1)):
        for j in range(max_len):
            if list1[i][f1] == list2[j][f2] and list2[j][f2]:
                list1[i][f3] = list2[j][f4]
    print(len(list1))
    with open('3.csv', "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in list1:
            writer.writerow(row)
    print('Готово!')