
# storing weights of all people
mom_w = 70
dad_w = 70
sis_w = 60
my_w = 60
# storing using list
# helpful when we have to process in an order
# lists are ordered and mutable
weights = [70, 70, 60, 60]
# storing using a dictionary
# helpful when we have to process each member randomly
# dictionaries are not ordered, but are mutable
weights = {
    "mom" : 70,
    "dad" : 70,
    "sis" : 60,
    "my" : 60,
}
# print(weights)

# stroing heights of all people in cms
mom_h = 170
dad_h = 172
sis_h = 175
my_h = 150
# lists
heights = [170, 172, 175, 150]
# print(type(heights))
# dictionary (in other prog lang it may be called a map)
heights = {
    "mom" : 170,
    "dad" : 172,
    "sis" : 175,
    "my" : 150,
}
# print(type(heights))

# these data structures can be nested too
bio = {
    "mom" : {"name": "alice", "weight": 70, "height": 170},
    "dad" : {"name": "brian", "weight": 70, "height": 172},
    "sis" : {"name": "lucy", "weight": 60, "height": 175},
    "my" : {"name": "victoria", "weight": 60, "height": 150}
}

# accessing those values:
# >>> bio['mom']
# {'name': 'alice', 'weight': 70, 'height': 170}
# >>> bio['mom']['height']
# 170