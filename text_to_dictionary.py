file = open('file.txt', 'r')
read_file = file.read()
print(read_file)
split_by_newline = read_file.split('\n')
print(split_by_newline)
print(len(split_by_newline))
bool_count_dict = {}
for item in split_by_newline:
    item = item.split('\t')
    if item[1] not in bool_count_dict:
        bool_count_dict[item[1]] = 1
    else:
        bool_count_dict[item[1]] += 1
print(bool_count_dict)