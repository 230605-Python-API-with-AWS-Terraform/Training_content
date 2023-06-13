"""

class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2

square_num = Squares(5)

for sq in square_num:
    print(sq)

print(next(square_num))

O/p:
1
4
9
16
25

-------------------------------------

my_li=[1,2,3,4,5]
my_it=iter(my_li)
while True:
    try:
        item=next(my_it)
        print(item)
    except StopIteration:
        break



def num_gen(n):
    for i in range(n):
        yield i

my_gen=num_gen(10)

print(tuple(my_gen))

for num in my_gen:
    print(num)



# Shallow copy vs deep copy
or_li=[1,2,3,4,5,[1,2,3]]

shal_cop=or_li[:]

shal_cop[5].append(10)
or_li[5].append(20)
print(or_li)
print(shal_cop)


"""
import copy


or_li=[1,2,[3,4]]
cop_li=copy.copy(or_li)

cop_li[2][1]=100


print(or_li)
print(cop_li)


deep_li=copy.deepcopy(or_li)
deep_li[2][1]=200
print(or_li)
print(deep_li)





