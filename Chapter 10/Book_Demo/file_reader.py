# coding=utf-8

# file_path =r'C:\Users\sks\Downloads\pi.digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)

# with open(file_path) as file_object:
#     for line in file_object:
#         print(line)
#
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# with open(file_path) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())


# with open(file_path) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))


with open(r'pi.digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
# print(pi_string)
# print(float(pi_string))
# print(len(pi_string))
# print(pi_string[:52] + '...')
# print(len(pi_string))
birthday = input('Enter your birthday,in the form mmddy:')
if birthday in pi_string:
    print('Your birthday appears in the digits of pi.')
else:
    print('Your birthday does not appear in the digits of pi. ')








