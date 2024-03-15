# # count = 1
# # while count <= 5:
# #     print("Hello")
# #     count += 1
# #========================================================
# #ques1   
# # i = 1
# # while i <= 100:
# #     print("Khaise",i)
# #     i += 1

# #ques2
# # i = 100
# # while i >= 1:
# #     print("Khaise",i)
# #     i -= 1

# #ques3
# # n=int(input('Enter a number : '))
# # i = 1
# # while i <= 10:
# #     print(n*i)
# #     i += 1

# #ques4
# # nums=[1,4,9,16,25,36,49,64,81,100]
# # idx = 0
# # while idx < len(nums):
# #     print(nums[idx])
# #     idx += 1

# nums=[1,4,9,16,25,36,49,64,81,100]
# x=36
# idx = 0
# while idx < len(nums):
#     if(nums[idx]==x):
#         print("Found at idx:  ",idx) 
            # break   
#     else:
#         print("Searching...")
#===========================================================

#contiune
i =1
while i <= 10:
    if(i%2 != 0):
        i+=1
        continue #skip
    print(i)
    i +=1