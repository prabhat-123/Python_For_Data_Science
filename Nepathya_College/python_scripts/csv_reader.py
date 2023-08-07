from functions.func import read_csv
from arg_parser import args
dataset = read_csv(args.csv)
print(dataset)