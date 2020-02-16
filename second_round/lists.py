class Student:
    pass


s1 = Student()
s2 = Student()
s3 = Student()
# print(type(s1))

# list properties:
# 1. ordered
# 2. mutable (changeable)
# 3. duplicates allowed
# english_scores = [ 10, 10, 10, 20, 10, 20, 20, 10, 20, 20]
###########################################
# int
# float
# bool
# str
# mixed_types = [10, "oranges", "fine", "mountains", True, False, 5.5, s1, s2]

###########################################

# print([ 10, 10, 10, 20, 10, 20, 20, 10, 20, 20])
# print(english_scores)

###########################################
# monthly_spending = [100, 200, 150]
# [150, 200, 100]
# jan = first item of monthly_spending
# feb = second item of monthly_spending
# mar = third item of monthly_spending

###########################################

# CRUD:
# 1. read
# 2. inserting
# 3. updating
# 4. deleting

###########################################

# main data structures in python:
# lists
# dictionaries
# # sets
# # tuples

###########################################


# english_scores = [ 10, 20, 25]

# [ 10,   20,     25]
#     0   1       2

# 1. read
        # for first item:
        # print(english_scores[0])

        # 2nd item:
        # print(english_scores[1])

        # 3rd item:
        # print(english_scores[2])

        # Accessing range of items: For example, 2nd and 3rd items:
        # print(english_scores[1:3]) # left value included, right value excluded

        # print(english_scores[3]) # gives IndexError (list index out of range)
        # 1:3
        # 1, 2, not(3)

        # If we want all items till the end starting in the middle:
        # english_scores = [ 10, 10, 10, 20, 10, 20, 20, 10, 20, 20]
        # print(english_scores[5:])

        # If we want all items from the beginning of the list till some point in the middle:
        # english_scores = [ 10, 11, 12, 28, 15, 21, 22, 9, 20, 7]
        # print(english_scores[0:4]) # [ 10, 11, 12, 28]
        # print(english_scores[:4]) # [ 10, 11, 12, 28]

        # value order:     10, 11, 12, 28, 15, 21, 22, 9, 20, 7
        # index order:      0,  1,  2,  3,  4,  5,  6, 7,  8, 9


        # 193
        # 192
        # 1:

        # 0, 1, 2, 3,.....192 --> 193 elements

        # # finding length of a list:
            # english_scores = [ 10, 10, 10, 20, 10, 20, 20, 10, 20, 20]
            # print(len(english_scores))

        # english_scores = [ 10, 11, 12, 20, 17, 18, 16, 7, 8, 4, 24, 3]
        # print all except first item in the list:
        # print(english_scores[1:])
        # print(english_scores[1:10])
        # print(english_scores[1:len(english_scores)]) # because len(english_scores) evaluates to 10 for this list

        # print(len(english_scores))
        # english_scores = [ 10, 11, 12]
        # # english_scores[len(english_scores)]
        # length = len(english_scores)



        # negative indexing (to help with navigating the list from the rear end of the list)
            # value order:   10, 11, 12
            # + index order:  0,  1,  2
            # - index order: -3, -2, -1

            # english_scores[0]
            # english_scores[1]
            # # print(english_scores[len(english_scores)-1]) # gives last item
            # print(english_scores[-2]) # gives the last item



            # print(english_scores[0])
            # print(english_scores[-3])


            # indexing of strings works the same way as lists

            # fruit = "apple"

            # # value order:            a,   p,  p,  l,  e
            # # positive index order:   0,   1,  2,  3,  4
            # # negative index order:   -5, -4, -3, -2, -1
            # print(fruit[-3:])

        # 2. inserting an item into a list
            # first_list = [5, 28, 90]
            # first_list.append(83)
            # print(first_list)

            # second_list = [73, 28, 50] # [5, 28, 90, 73, 28, 50]
            # first_list.extend(second_list)
            # print(first_list)

            # first_list.append([73, 28, 50])
            # print(first_list)

            # first_list.append(73, 28, 50) # gives TypeError: append() takes exactly one argument (3 given)



            # 3. updating
            # first_list = [5, 28, 90]
            # first_list[0] = 30

            # 4. deleting
            # first_list = [5, 28, 5, 90]
            # first_list.remove(5)
            # modified_list = first_list
            # print(modified_list)


            # # 5. sorting:
            # a = {5,28,5,90, 78, 81, 38, 28, 39, 63, 73} # sets are not ordered
            # print(a)
            # a = [5,28,5,90, 78, 81, 38, 28, 39, 63, 73]
            # a.sort(reverse=True)
            # print(a)

            # a = ["cherries", "apples", "bananas", "dragon fruit"]
            # print(a)
            # a.sort()
            # print(a)
            # a.sort(reverse=True)
            # print(a)

            # # 6. counting
            # a = [5,28,5,90, 78, 81, 38, 28, 39, 63, 73]
            # print(a.count(28))

