def process():
    return 10
    return 20
    return 30

res = process()
print(res)  #10


def disp():
    yield 10
    yield 20
    yield 30

res = disp()
print(res)   # generator object
print(res.__next__()) # 10
print(res.__next__()) # 20
print(res.__next__()) # 30
# print(res.__next__()) # StopIteration - calling more than available will raise exception