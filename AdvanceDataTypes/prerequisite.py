s1 = "This is a test. This test is simple.".replace('.'," ").split()
print(s1)
di = {}
for word in s1:
    if word in di:
        di[word] = di[word] + 1
    else:
        di[word] = 1 
# print(di - dictionary)
for key in di.keys():
    print(f'{key}: {di[key]}')