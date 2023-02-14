
# hello, test, Python
str_list = ['hello', 'test', 'Python']
result = ""
for i in str_list:
    if len(result) != 0:
        result += ", "
    result += i
print(result)

