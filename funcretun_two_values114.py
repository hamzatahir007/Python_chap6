#funtion returning two values
def func (int1,int2):
    add = int1 + int2
    multiply = int1*int2
    return add, multiply

print(func(2,4)) #it gives in one tuples value

#to print alag alag value
add, multiply = func(1,4)
print(add)
print(multiply)

