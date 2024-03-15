#function definition
# def calc_sum(a,b): #parameters
#     return a+b
# sum = calc_sum(1,2) #function call #arguments
# print(sum)

#====================================================================

# Loves = ["Prokrity","Anonna","Shanchari","Dhara"]
# cities=["Shahbug","Motijheel","Farmgate","Maymenshingh","Bankura"]

# def print_len(list):
#     print(len(list))
    
# print_len(Loves)
# print_len(cities)


#average of 3 functions

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(3,2,1)

#====================================================================

# #recursion
# def show(n):
#     if(n== 0):
#         return
#     print(n)
#     show(n-1)
# show(5)


# def fact(n):
#     if(n==1 or n == 0):
#         return 1
#     return fact(n-1)*n
# print(fact(4))


def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)
fruits = ["Mango","Litchi","Apple","Banana"]
print_list(fruits)
#====================================================================

    
