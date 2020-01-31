a = [1, 3, 8, 10]
sum = 0

# for loop
# they are used for iterating over an iterable
# sum of all elements in the list
print("Iterating a loop......")
for i in range(len(a)):
    # print(i+1, sum)
    sum += a[i] # sum = sum + a[i]

print(sum)


# iterating a dictionary
print("Iterating a dictionary......")
d = {   "mom": 60,
        "dad": 70
        }
sum_weights = 0

for k,v in d.items():
    sum_weights += v

print(sum_weights)


# iterating a string
print("Iterating a string......")
sentence = "harry, how long have you been waiting"
num_r = 0
num_e = 0
other_char = 0

# find the number of r's and e's in the sentence
for i in range(len(sentence)):
    if sentence[i] == 'r':
        num_r += 1
    elif sentence[i] == 'e':
        num_e += 1
    else:
        other_char += 1
    # if not sentence[i] == 'e' and not sentence[i] == 'r':
    #     other_char += 1
        

print(f"number of r's in the sentence: {num_r}")
print(f"number of e's in the sentence: {num_e}")
print(f"number of other chars in the sentence: {other_char}")