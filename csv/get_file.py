import csv, cfg

list1 = []
list2 = []


def file_one(filename):
    with open(cfg.UPLOAD_FOLDER + str(filename), 'r', newline="") as file:
        line = csv.reader(file, delimiter=';', quotechar='|')
        for row in line:
            list1.append(row)


def file_two(filename):
    with open(cfg.UPLOAD_FOLDER + str(filename), 'r', newline="") as file:
        line = csv.reader(file, delimiter=';', quotechar='|')
        for row in line:
            list2.append(row)


def compare_list(f1, f2, f3, f4):
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
