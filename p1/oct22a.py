__author__ = 'kcronyn'

print("this is my new program")

try:
    reply = -1
    while 0 != reply:
        reply = int(input("enter a positive integer, zero when done: "))

        if reply >= 0:
            print("your input doubled is", reply*2)
        else:
            print ("not valid input")
except:
    print ("you did not enter a valid response")
