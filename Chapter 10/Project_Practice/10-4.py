# coding:utf-8

'''编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt中。确保这个文件中的每条记录都独占一行。'''

def input_name(names):
    with open('guest_book.txt','a') as file_object:
            file_object.write(names)

names = input("Please input your names: ")
while True:
    print(names + ", welcome to come here!")
    input_name(names)
    break



