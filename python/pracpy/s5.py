# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

# for x in range(0,100,5):
#     print(x)

def div5(list):
    for x in list:
        if x % 5 == 0:
            print(x)

list = [1,20,25,65,456,856,5000,45620,10000000,15555555]
print("the list : " + str(list))
print("divisible of 5 on the list: ")
div5(list)
