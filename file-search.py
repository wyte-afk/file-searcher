import os.path

file = input('Enter The File Name : ')

open(file , 'w')
print(os.path.isfile(file))