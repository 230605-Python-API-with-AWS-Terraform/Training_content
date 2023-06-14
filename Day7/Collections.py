
from collections import namedtuple

a=namedtuple('books','name , author , year')

sam=a('Learn to code',' Robert','2023')

print(sam)



from collections import Counter

num=[10,10,10,3,3,2,2,3,2,1]

c=Counter(num)
print(c)

def outer_function():
    x = 10  # Outer variable

    def inner_function():
        x += 5  # Modify the value of x from the outer function
        print(x)  # Access x from the outer function

    inner_function()  # Output: 15

outer_function()
