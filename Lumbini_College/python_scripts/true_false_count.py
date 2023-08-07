file = open('file.txt', 'r')
file_read = file.read()
data = file_read.split('\n')
true_false_count = {}
for item in data:
    new_item = item.split('\t')
    if new_item[1] not in true_false_count:
        true_false_count[new_item[1]] = 1
    else:
        true_false_count[new_item[1]] += 1
file.close()
print(true_false_count)