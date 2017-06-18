# coding:utf-8

'''replace the Python wtih Java'''

with open('learning_python.txt') as lp:
    contents = lp.readlines()

line_string = ''
for line in contents:
    line_string += line
    new_line_string = line_string.replace('Python','Java')
print(new_line_string)