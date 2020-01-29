a = 'hi'
b = 'keeru'
c = '!'
l = [a, b, c]

# print(l)
# print("_".join(a+b+c))
print(type(a+b+c))
# print(" ".join(l))
# type(l)

### split ###
# using dot to split the ip address
ip = "10.78.8.1"
print(ip.split("."))

# using slash to split the path
path = "/home/user/development/learn_python"
output = path.split("/")
print(output)

# using letters from the english alphabet
my_word = "tell me hello"
output = my_word.split("l")
print(output)

# using two characters
my_word = "tell me hello"
output = my_word.split("ll")
print(output)

# can be used to split a paragraph using new lines
para = """tell me who that funny person is.
please tell me.
he must have done other funny things in life."""
output = para.split("\n")
print(output)



######################################################
############ Length of a string or an iterable #######
######################################################

word = "keeru"
length = len(word)
print(length)

l = [1,102,2028]
length_of_list = len(l)
print(length_of_list)

d = {"mom": 10, "dad": 5, "sis": 3, "bro": '8'}
print(len(d))


######################################################
############ in keyword #######
############ also useful to find membership inside iterables like:
############ lists, dicts, sets, etc. #######
######################################################

print("kee" in "keeru")


######################################################
############ indexes of the strings #######
######################################################


