# Accept string from the user and display only those characters which are present at an even index
# def e3(str):
#     x = 1
#     for x in str:
#         print(str[])

def e3(str):
    for x in range(0, len(str)-1,2):     #(start,stop,step)
        print([x],str[x])

str = input("Enter a String, Please: ")
print("Original String: ")
print("Even index characters: ")

e3(str)