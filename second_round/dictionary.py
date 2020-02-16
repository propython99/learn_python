# used to store key-value pairs
# keys must be hasable (example: string, int, float, bool.) Lists and tuples are not hashable.
# dicts are not ordered

# english_scores = [10, 12, 15,]
#                   s1, s2, s3
# print(english_scores)


# science_scores = [25, 22, 21]
#                   s2, s3, s1

# science_scores = {
#     "s3" : 23,
#     "s1" : 21, 
#     "s2" : 25,
#     "apples": "goats",
#     0: "universe",
#     5.3 : "peter",
#     True : "Ram"
#     [1,2] : 51829
# }


# Reading (keys must be hasable)
# print(science_scores)
# s3 = "apples"
# print(science_scores['s3'])



# inserting or creating a key-value pair
# science_scores = {
#     "s3" : 23,
#     "s1" : 21, 
#     "s2" : 25,
# }

# science_scores['s4'] = 32
# print(science_scores)

# hashing helps in retrieving data in a big dictionary
# s3
# s328943 

# # updating
# science_scores = {
#     "s3" : 23,
#     "s1" : 21, 
#     "s2" : 25,
# }
# science_scores['s3'] = 28
# print(science_scores)


# deleting
science_scores = {
    "s3" : 23,
    "s1" : 21, 
    "s2" : 25,
}
# del science_scores["s3"]
# print(science_scores)
science_scores.pop("s3")
print(science_scores)
