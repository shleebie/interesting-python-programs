import math

# initiate end as 0

n = 0

# convert start and end to integer

start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

# create list

square_nums = []

for values in range(start,end):

    # first calculate square root
    
    s_root = math.sqrt(int(values))

    # if the value / square root equals itself, append to list

    if int(values) % s_root == 0:
        square_nums.append(str(values))

# when finished, shift list to a string with a space bar between

final_square_nums = " ".join(square_nums)

# print square numbers

print(final_square_nums)



