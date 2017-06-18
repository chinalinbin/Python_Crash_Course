# coding:utf-8


'''编写一个程序后，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。'''

def input_name(names):
    filename = 'guest.txt'
    with open(filename,'w') as file_object:
        file_object.write(names)

names = input("please input your names:")
print(names)
input_name(names)





