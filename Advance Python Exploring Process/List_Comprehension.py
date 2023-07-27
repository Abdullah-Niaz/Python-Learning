x = [1,2,3,4,5,6,7,8,9]
obj1 = [y for y in x if y % 2==0]
obj2 = [y for y in x if y % 2==1]
print("Even Numbers: ", obj1, "\nOdd Numbers: ",obj2)

doc = print.__doc__
print(doc)