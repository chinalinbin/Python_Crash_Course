# coding:utf-8

def count_words(filename):
    '''count words in the txt'''
    try:
        with open(filename,'rb') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)

    else:
        # count words in this txt
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

# filename = 'alice.txt'
# count_words(filename)

filenames = ["alice.txt","sddhartha.txt","moby_dick.txt","little_women.txt"]
# print(filenames)
for filename in filenames:
    count_words(filename)


