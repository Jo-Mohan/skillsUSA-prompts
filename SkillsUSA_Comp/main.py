import collections
import os

#######################################################################
##                          PLEASE READ                              ##
##           Some computers have different requirements for          ##
## the linking to a file. If "Computer Programming Prompt\Info.txt"  ##
##      isn't found, please change those lines to just "Info.txt"    ##
#######################################################################



#file opened in read "r" mode
file = open("Computer Programming Prompt\Info.txt", "r")

#unpacks first 4 bytes of content into dequed list
file = [*file.read(4)]
message = collections.deque(file)


def encrypt():

    encoded = ""

    #checks if code only contains integers
    for i in range (len(message)):
        try:
            message[i] = (int(message[i])+7) % 10
        except:
            print("Please enter a 4 digit code consisting of only integers")
            return 
    
    #from import, slides list right 2 w/ wrapping
    message.rotate(2)

    #turns dequed collection back into string
    for i in range(len(message)):
        encoded += str(message[i])

    #reopens file in write mode
    file = open("Computer Programming Prompt\Info.txt", "r+")
    content = file.read()
    file.seek(0)
    file.write(encoded + "\n" + content)
   


def decrypt():

    decoded = ""

    #left 2 w/ wrapping
    message.rotate(-2)

    #checks if code only contains integers
    for i in range (len(message)):
        try:
            message[i] = (int(message[i]) + 3) % 10
        except:
            print("Please enter a 4 digit code consisting of only integers")
            return 

    # dequed to string
    for i in range(len(message)):
        decoded += str(message[i])

    file = open("Computer Programming Prompt\Info.txt", "r+")
    content = file.read()
    file.seek(0)
    file.write(decoded + "\n" + content)
   

#clear out the file
def empty():
    #file in write mode to turncate
    file = open("Computer Programming Prompt\Info.txt", "w")
    file.truncate(0)


def main():
    choice = input("Encrypt, Decrypt, Empty, or Exit: ")

    if choice.lower() == "encrypt":
        encrypt()
        main()
    elif choice.lower() == "decrypt":
        decrypt()
        main()
    elif choice.lower() == "empty":
        empty()
        main()
    elif choice.lower() == "exit":
        return
    else:
        print("Please choose one of the commands listed")

main()





#if(os.path.getsize("Computer Programming Prompt\Info.txt") == 0):
        #print("please enter a code")
        #return


