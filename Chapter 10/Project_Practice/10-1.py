# coding:utf-8

'''read and input from learning_python.txt'''

# with open('learning_python.txt') as lp:
#     contents = lp.read()
# print(contents)

# with open('learning_python.txt') as lp:
#     # contents = lp.read()
#     for content in lp:
#         print(content.rstrip())

with open('learning_python.txt') as lp:
    lines = lp.readlines()

line_string = ''
for line in lines:
    line_string += line.strip()
print(line_string)
print(len(line_string))



