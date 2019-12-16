# Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum
#mine
def e2(x,y):
    z = x * y
    if z> 1000:
        return x + y
    else:
        return z

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

res = e2(x,y)

print(res)

#sol
# # def multiplication_or_sum(num1, num2):
# #       product = num1 *num2
# #   if product < 1000:
# #     return product
# #   else:
# #     return num1 +num2

# # number1 = int(input("Enter first number "))
# # number2 = int(input("Enter second number"))

# # result = multiplication_or_sum(number1, number2)
# # print("The result is", result)
