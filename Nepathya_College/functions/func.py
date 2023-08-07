from csv import reader

def addition(a, b):
    result = a + b
    return result

def subtraction(a, b):
    result = a - b
    return result

def multiplication(a, b):
    result = a * b
    return result

def division(a, b):
    result = a /b
    return result

def square(num):
    return num * num

def cube(num):
    return num**3


def freq_table(datasets, index):
    freq_dict = {}
    for item in datasets[1:]:
        if item[index] not in freq_dict:
            freq_dict[item[index]] = 1
        else:
            freq_dict[item[index]] += 1
    return freq_dict


def read_csv(file):

    f = open(file)
    data = reader(f)
    dataset = list(data)
    f.close()
    return dataset