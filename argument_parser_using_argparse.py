#Step1: Importing argparse
import argparse
#Step2: Creating an parser object
parser = argparse.ArgumentParser()
#Step3:Adding Arguments
parser.add_argument('-f',"--file",required = True, help = "name of a file")
#Step4: Parsing the argument parser
args = parser.parse_args()

file = open(args.file, 'r')
data = file.read()
print(data)
file.close()
