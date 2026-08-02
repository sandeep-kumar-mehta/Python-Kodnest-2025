rows = int(input('Enter Number of Rows: ')) # taking an input


for i in range(rows):
    print("  " * (rows - i) + "* " * (i + 1))
    
for i in range(1, rows):
    print("  " * (i + 1) + "* " * (rows - i))