# word = input("Enter The word: ")    #1
# print(len(word))
#======================================================
# x = input ('Enter any your name: ')
# from collections import Count
# counts=Count(x)
# print (counts)
#======================================================
# string = input("Enter the string: ")
# string = string[0] + string[1:].replace(string[0],"$")
# print(string)
#=====================================================
a=input("ENTER THE STRING:")
n=len(a)
if n<=2:
   print("EMPTY STRING:")
else:
   print(a[0]+a[1]+a[-1]+a[-2])