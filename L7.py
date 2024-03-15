# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

# f = open("demo.txt", "a")
# f.write("Then I'll move to ML")
# f.close()

# f = open("demo.txt", "w")
# f.write("I'll learn JS")
# f.close()
#=================================================================
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learing file i/o\n")
#     f.write("using java\nI like programming in java\n")
with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)
    
with open("practice.txt","w") as f: