"Variable Expressions" 


print('python comparision operators assignment')
Apple_Rate=int(input('Rate of the apple :'))
Qty=int(input ("Qty: "))


#Shop 1 

subtotal=Apple_Rate*Qty

print('Sub Total : ',subtotal)

Discount=0.10

Shop_1_Result=subtotal-(subtotal*Discount)

print('Total : ', Shop_1_Result)

# shop 2

pineapple_rate=int(input("rate of Pineapple: "))

shop_2_Result=Apple_Rate+pineapple_rate 

print('total : ', shop_2_Result)

Result=(Shop_1_Result>=shop_2_Result, "profit")

print(Result)


# """
# print("A"+9)
# print(1+2)
# # Data Types casting: -
# """
# city = "hyderabad"
# age = 34
# temparature = 28.3 
# check = True
# C = 4+3j
# # print(type(city))
# # print(type(age))
# # print(type(temparature))
# # print(type(check))
# # print(type(C))
# # P = int("b")
# # print(P)
# R = int("4")
# print(type(R))
# print(R)
# Q = str(250)
# print(type(Q))
# A = int(25.3)
# print(A)
# print(type(A))

# # if condition implementation in python
# age = int(input("enter your age: "))
# if age > 18:
#     print("Allow him to the chamber")
# elif age>=16 and age < 18:
#     print("additional info required")
# else:
#     print("you are not allowed as your age is below 16")