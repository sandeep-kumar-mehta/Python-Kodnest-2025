#Increasing Star Pattern
rows = int(input('Enter Number of Rows: ')) # taking an input

# 1st method

# row = int(input('Enter Rows: '))
# for i in range(1, row+1):
#     print("*" * i)


# 2nd method


for i in range(rows):
    print("* " * (i + 1))

# output: 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


#Number printing
# row = int(input('Enter Rows: '))
# for i in range(1, row+1):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()

# output
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

# Decreasing Star Pattern

# rows = int(input('Enter Number of Rows: '))

# for i in range(rows):
#     for j in range(5 - i):
#         print("*", end=" ")
#     print()

# output:
# Enter Number of Rows: 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
print(" ")  # Space between them

for i in range(rows):
    print("* " * (rows - i))


# output: 
# * * * * *
# * * * *
# * * *
# * *
# *

print(" ")  # Space between them

for i in range(rows):
    print("  " * (rows - i) + "* " * (2 * i + 1))

# output: 
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *


print(" ")  # Space between them

for i in range(rows):
    print("  " * (i + 1) + "* " * (2 * (rows - i) - 1))


# output :
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *



for i in range(rows):
    print("  " * (rows - i) + "* " * (i + 1) + "  " * (rows - i) + "* " * (i + 1))