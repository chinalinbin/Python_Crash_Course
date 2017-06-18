# coding:utf-8


'''编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中'''


def reason(resons):
    with open('programming.txt', 'w+') as answer:
        answer.write(reasons)
    with open('programming.txt', 'a') as answer:
        answer.write(reasons)
        answer.close()

done = False
while not done:
    reasons = input('Why do you love programming?\nAnswer:')
    reason(reasons)