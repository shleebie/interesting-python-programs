# initiate

sentence = input(f"Please enter a sentence: ")

# split sentence into a list

sentence = sentence.split()

# check for duplicates

duplicates = []

for removing_duplicates in sentence:
    while removing_duplicates not in duplicates:
        duplicates.append(removing_duplicates)

# reverses the list

duplicates.reverse()

# use join to turn a list into a string.

duplicates = ", ".join(duplicates)

# print outcome as reverse
print(f"Unique words: {duplicates}")
