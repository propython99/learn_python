# User-defined functions

def hello_friends(friend_list):
# friend_list = k_friends
    for name in friend_list:
        full_name_list = name.split(" ")
        first_name = full_name_list[0]
        first_letter = first_name[0]
        print("hello", first_letter)


# hello("keeru")

# people = {
#     "keeru": {  
#                 "married": True,
#                 "gender": "F",
#                 "age": 25,
#                 "lang": ["English", "Telugu"],
#                 "comp_know": ["python", "linux", "sql", "git"]
#                 "email" : "keeru@keeru.com"
#                 "address" : "GA"
#                 },
#     "sunny": {  
#                 "married": True,
#                 "gender": "M",
#                 "age": 16,
#                 "lang": ["English", "Telugu"],
#                 "comp_know": ["python", "linux", "sql", "git", "php"]
#                 "email" : "sunny@keeru.com"
#                 "address" : "AL"
#                 }
# }

k_friends = ['keeru k', 'sruthi maddali', 'aparna ayyangari', 'deepika jalaja']
s_friends = ['john smith', 'harry porrter', 'max sweeney', 'suresh jr']
# print(type(s_friends))

# for name in k_friends:
#     full_name_list = name.split(" ")
#     first_name = full_name_list[0]
#     first_letter = first_name[0]
#     print("hello", first_letter)
hello_friends(k_friends)

# for name in s_friends:
#     full_name_list = name.split(" ")
#     first_name = full_name_list[0]
#     first_letter = first_name[0]
#     print("hello", first_letter)
hello_friends(s_friends)


# name = 'keeru'
# print(name[0])

# Iteration: 1
# starts with zeroth element of the list
# fr_name = k_friends[0]

# Iteration: 2
# proceeds to the next element of the list
# fr_name = k_friends[1]

# Iteration: 3
# proceeds to the next element of the list
# fr_name = k_friends[2]

# Iteration: 4
# proceeds to the next element of the list
# fr_name = k_friends[3]

# for name in ['keeru k', 'sruthi maddali', 'aparna ayyangari', 'deepika jalaja']:
#     full_name_list = name.split(" ")
#     first_name = full_name_list[0]
#     first_letter = first_name[0]
#     print("hello", first_letter)