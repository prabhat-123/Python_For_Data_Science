import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-n1',"--num1",required = False, help = "first number")
parser.add_argument('-n2',"--num2",required = False, help = "second number")
parser.add_argument('-c', "--csv", required = False, help = "name of csv file")

args = parser.parse_args()
