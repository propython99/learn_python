# generators hold state
def first_n(n):
    for i in range(n):
        yield i

gen = first_n(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # generator says, hey I am out of the stuff, can't give you anymore!
# for i in first_n(5):
#     print(i)