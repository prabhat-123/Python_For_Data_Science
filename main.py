from functions.func import *
from dataset.movie_datasets import movie_datasets
from dataset.student_datasets import student_datasets
add = addition(5,4)
print("Result of addition is : {}".format(add))
sub = subtraction(5,4)
print("Result of subtraction is : {}".format(sub))
mul = multiplication(6,3)
print("Result of multiplication is : {}".format(mul))
div = division(55,11)
print("Result of division is : {}".format(div))
sq_5 = square(5)
print("Square of 5 is : {}".format(sq_5))
cu_10  = cube(10)
print("Cube of 10 is : {}".format(cu_10))

semester_freq_table = freq_table(datasets = student_datasets, index = 4)
print(semester_freq_table)
movie_genre_table = freq_table(datasets = movie_datasets, index = 1)
print(movie_genre_table)

