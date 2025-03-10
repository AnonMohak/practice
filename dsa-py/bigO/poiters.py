num1 = 11
num2 = num1

print('Before Update')
print(num1)
print(num2)

print(id(num1))
print(id(num2))

print('After Update')

num2 = 22

print(num1)
print(num2)

#int are immutable
print(id(num1))
print(id(num2))


#############################################################################

dict1 = {
            'value' : 11
        }

dict2 = dict1

print('Before Update')
print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))

dict2['value'] = 22

print('After Update')
print(dict1)
print(dict2)

#dict are mutable
print(id(dict1))
print(id(dict2))

##ALSO IF NO VARIABLE POINTS TO A VALUE IN MEMORY ADDRESS, WE DONT HAVE ANY WAY TO ACCESS IT. SO PYTHON AUTOMATICALLY REMOVES IT AND THIS IS CALLED GARBAGE COLLECTION.
