# 1 x 2 = 2
# 2 x 3 = 6
# 3 x 4 = 12
# 4 x 5 = 20
# …
# …
# …
# 49 x 50 = 2450

# print("Hello pronic numbers")
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number ")) 


# for i in range(num1, num2):
#     #print(i)
#     #print(i + 1)

#     product = i * (i + 1)
#     #print(product)

#     print(f"- {i} x {i+1} = {product}")



#make a program where:
# you ask the user to type a number
# determine whether that number is a pronic number


num = int(input("Type a number: "))
is_pronic = False

for i in range(1, num):
    
    product = i * (i + 1)
    
    if product == num:
        print("This is a pronic number")
        is_pronic = True
        break

if is_pronic == False:
    print("this is not a pronic number")
