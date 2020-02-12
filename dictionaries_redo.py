# # revisiting lists
# # l = [2018, 2019, 2020]

# # 2018    2019    2020
# # 0       1       2

# # l[0]

# # simple dictionary


# # keys are mostly strings, integers, floats
# # they have to be "hashable"
# # values can be of any type.
# # they can be simpler types like ints, strings, floats, etc.
# # they can also be complex types like
# # lists, dictionaries, tuples, or user-defined types (classes)

# # d = {"key": "value"}
# # d["key"]

# d = {   "name": "keeru", 
#         "zip": 21810,
#         }

# # print(d["name"])
# # print(d["zip"])


# keeru =  {  
#             "married": True,
#             "gender": "F",
#             "age": 25,
#             "lang": ["English", "Telugu"],
#             "comp_know": ["python", "linux", "sql", "git"],
#             "email" : "keeru@keeru.com",
#             "address" : "GA"
#             }

# keeru["married"] 

# # for k,v in keeru.items():
# #     print(k)

# # print(keeru["age"])
# # print(keeru["comp_know"])

# # print(type(keeru["comp_know"]))

# # print(keeru)

# for k,v in keeru.items():
#     if type(v) not in [int, str, list]:
#         print(k, type(v), sep="\t\t\t\t")



people = {
    "keeru": {  
                "married": True,
                "gender": "F",
                "age": 25,
                "lang": ["English", "Telugu"],
                "comp_know": ["python", "linux", "sql", "git"],
                "email" : "keeru@keeru.com",
                "address" : "GA"
                },
    "sunny": {  
                "married": True,
                "gender": "M",
                "age": 16,
                "lang": ["English", "Telugu"],
                "comp_know": ["python", "linux", "sql", "git", "php"],
                "email" : "sunny@keeru.com",
                "address" : "AL"
                }
}

# people = { "keeru": "value 1", "sunny": "value 2"}

for k,v in people.items():
    print(k, len(people[k]["comp_know"]))
