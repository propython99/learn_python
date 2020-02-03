# # learning functions - continuation

# def greet_friends(friends_list, greeting="hello"):
#     # greeting = "hey girl"
#     # friends_list = k_friends
#     for name in friends_list:
#         full_name_list = name.split(" ")
#         first_name = full_name_list[0]
#         first_letter = first_name[0]
#         print(greeting, first_letter)

# k_friends = ['keeru k', 'sruthi maddali', 'aparna ayyangari', 'deepika jalaja']
# s_friends = ['john smith', 'harry porrter', 'max sweeney', 'suresh jr']

# # greet_friends(greeting, friends_list)

# greet_friends(k_friends)
# greet_friends(s_friends, "hi buddy")

# greet_friends(greeting="hi there!", friends_list=s_friends)

# print("hello", "keerthi", end="\t", sep="\t")
# print("hello", "keerthi", sep="\t", end="\n"*20)
# print("hello", "keerthi", sep="\t", end="\n"*20)
# print("hello", "keerthi", "how", "are", "you", "doing", "these", "days")

def my_print_func(*args, **kwargs):
    print(args, kwargs, sep="\n")
    # for i in args:
    #     print(i, end=" ")
    # print()

my_print_func("hello", "keerthi", "how", "are", "you", "doing", "these", "days", hey="how are you", hi="hi there")