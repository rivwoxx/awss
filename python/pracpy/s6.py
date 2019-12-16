# # Return the number of times that the string “Emma” appears anywhere in the given string
# Given string is “Emma is a good developer. Emma is also a writer” and output should be 2.

def count(str1):
    x = 0
    for y in range(len(str1)-1):
        x += str1[y:y+4] == 'Emma'
    return x


str1 = 'Emma is a good developer. Emma is also a writer'
x = count(str1)
print(x)
