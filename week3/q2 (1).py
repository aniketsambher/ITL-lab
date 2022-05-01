import sys
# defines a global variable
a = 123
# defines a 'cat' function which takes a filename
def cat(filename):
    print(filename, '=======')
    f = open(filename, 'r')
    data=f.read(); 


    #############################
    f1 = open("output1.txt", "w+")
    data_1 = data[::-1]
    f1.write(data_1)
    f1.close()


    ####################################
    f.close()

def main():
   
    filename = "hi.txt"
    if filename == 'voldemort' or filename == 'vader':
        print('this file is very worrying')
        cat(filemane, 123, bad_variable)
    else:
        cat(filename)
    print('all done') 
    


if __name__ == '__main__':
    main()
