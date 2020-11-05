#looping in tuples
#tuple with one elements
#tuple without paranthesis
#tuple un packing
# list inside tuples
#some functions that you can use with tuples

mixed = (1,2,3,4,5,6)

#for loop and tuples 
# for i in mixed:
#     print(i)
#note you can used while loop



#tuple with one elements
# number = (1,)   #in tuples , is constant after statment
# words = ('word',)
# print(type(number))
# print(type(words))



#tuple without paranthesis
# giutars = 'yamaha' , 'baton rouge' , 'taylor'
# print(type(giutars))




#tuple un packing
giutarist = ('hamza tahir' , 'fahad aftab' , 'talha tahir')
giutarist1 , giutarist2 , giutarist3 = giutarist
# print(giutarist3)



# list inside tuples
favorites = ('hamza' , 'ahmed', ['tokyo' , 'china'])
favorites[2].pop()
favorites[2].append('we made it')
# print(favorites)



#some more function in tuples
print(sum(mixed))