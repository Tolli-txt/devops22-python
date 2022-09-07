# EXERCISE THREE - BOOLEAN OPERATIONS

x = True
y = False
z = True

boolean_list = [x, y, z]

#1.1 any()
result = any(boolean_list)
print(result)

#1.2
print("Checking with 'if-else statements'.")
def boolFunc():
    if (x, y, z) == True:
        return True
    else:
        return False

result1 = boolFunc()
print(result1)

print("Checking with 'all() function'.")
result_1 = all(boolean_list)
print(result_1)

#1.3



#1.4
def boolFunc2():
    if (x, y, z) == False:
        return False
    else:
        return True

result2 = boolFunc2()
print(result2)

